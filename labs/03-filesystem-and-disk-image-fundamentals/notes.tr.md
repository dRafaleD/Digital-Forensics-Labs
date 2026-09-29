# Gün 3 — Filesystem ve Disk Image Temelleri

[🇬🇧 English](notes.md) | [🇹🇷 Türkçe](notes.tr.md)

## Amaç

Filesystem image'ın ne olduğunu, adli bilişim analizinde neden mümkün olduğunca orijinal medyayı doğrudan değiştirmek yerine alınmış bir image üzerinde çalışıldığını ve küçük, zararsız bir EXT4 image'ın bütünlüğünü koruyarak nasıl inceleneceğini öğrenmek.

Bu lab:

- block device ve filesystem
- logical file ile raw storage farkı
- disk/filesystem image
- acquisition ve analysis farkı
- image hashing
- EXT4 temelleri
- read-only inceleme
- `file`, `dumpe2fs`, `debugfs`
- analiz öncesi/sonrası evidence integrity

konularını içerir.

Gerçek bir diskin image'ını almıyoruz. Tamamen yerel ve küçük bir training image oluşturuyoruz.

## 1. Storage katmanları

Başlangıç için şu modeli kullan:

```text
physical / virtual storage
          ↓
partition
          ↓
filesystem
          ↓
directory ve file
          ↓
application data
```

Bu katmanlar ilişkili fakat aynı şey değildir.

Disk partition table içerebilir. Partition bir filesystem içerebilir. Filesystem ise file, directory, metadata ve allocation bilgisini düzenler.

## 2. Filesystem nedir?

Filesystem, data ve metadata'nın storage üzerinde nasıl organize edildiğini belirler.

Örnekler:

- EXT4
- NTFS
- FAT32
- exFAT
- XFS

Filesystem yalnızca filename tutmaz. Türüne göre:

- directory structure
- timestamp
- owner
- permission
- allocation information
- filesystem-specific metadata

gibi bilgiler de bulunabilir.

Bu yüzden filesystem analysis, normal file manager ile klasör açmaktan daha fazla bilgi sağlayabilir.

## 3. Disk/filesystem image nedir?

Forensic image, inceleme için elde edilmiş storage temsilidir.

```text
source media
     ↓ acquisition
image file
     ↓ verification
working analysis
```

Acquisition yöntemine ve formata göre image tüm device'ı, bir partition'ı veya başka bir storage scope'u temsil edebilir.

Bu lab özel olarak oluşturduğumuz küçük raw filesystem image kullanır.

## 4. Logical copy ve image farkı

Normal file copy seçilmiş dosyalara odaklanır:

```text
folder/file -> copied file
```

Image ise acquisition scope'u içindeki daha düşük seviye filesystem/storage yapılarını koruyabilir.

```text
logical copy != raw/filesystem image
```

Biri her durumda diğerinden “daha iyi” değildir. Doğru acquisition yöntemi investigation, yetki, system state ve evidence gereksinimine bağlıdır.

## 5. Zararsız seed data oluştur

```bash
mkdir -p lab03-work/seed
cd lab03-work
```

İki training file:

```bash
printf "Digital Forensics Lab 03\nEvidence: harmless training file\n" > seed/note.txt
printf "case_id=DF-LAB-003\nstatus=training\n" > seed/case.txt
```

Kontrol:

```bash
ls -l seed
sha256sum seed/*
```

## 6. Küçük EXT4 image oluştur

32 MiB normal file:

```bash
truncate -s 32M lab-disk.img
```

Sadece oluşturduğumuz bu regular file'ı EXT4 olarak formatla ve seed klasöründeki dosyaları içine ekle:

```bash
mkfs.ext4 -q -L DF_LAB03 -d seed lab-disk.img
```

Çok önemli güvenlik kuralı:

> Bu komutu yalnızca oluşturduğun lab image ile kullan. `lab-disk.img` yerine gerçek disk veya partition yazma.

Yanlış target'ı formatlamak veri kaybına neden olabilir.

## 7. Image integrity baseline oluştur

Training image oluştuktan sonra onu evidence image gibi düşün.

SHA-256:

```bash
sha256sum lab-disk.img
```

Sonucu kaydet:

```bash
sha256sum lab-disk.img > lab-disk.sha256
```

Bundan sonra image'ı değiştirmemeye çalış.

Day 1 ile bağlantısı:

```text
create/acquire
     ↓
hash
     ↓
preserve
     ↓
analyze
     ↓
verify again
```

## 8. Image'ı tanımla

```bash
file lab-disk.img
```

Output EXT filesystem olduğunu göstermelidir.

Bu yalnızca ilk identification adımıdır; tek başına tam forensic conclusion değildir.

## 9. EXT4 metadata incele

`dumpe2fs` varsa:

```bash
dumpe2fs -h lab-disk.img
```

Şu alanları bulmaya çalış:

- filesystem volume name
- filesystem UUID
- filesystem features
- block size
- inode count
- block count
- creation information

Her alanı ezberlemeye çalışma. Önce filesystem'in ne tür metadata sunduğunu gör.

## 10. Block ve inode fikri

EXT filesystem'ler storage'ı block'lara ayırır ve filesystem object'lerini açıklamak için inode yapıları kullanır.

Basit model:

```text
directory entry
     ↓
inode
     ↓
metadata + file data referansları
     ↓
data blocks
```

Inode doğrudan “filename” değildir. Directory entry isim ile inode number arasında ilişki kurar.

Bu fark ileride deleted file ve filesystem artifact analizinde önemli olacak.

## 11. Mount etmeden incele

`debugfs`, EXT filesystem image'ını doğrudan inceleyebilir.

Root directory:

```bash
debugfs -R "ls -l /" lab-disk.img
```

Training file:

```bash
debugfs -R "cat /note.txt" lab-disk.img
```

İkinci file:

```bash
debugfs -R "cat /case.txt" lab-disk.img
```

Böylece image'ı normal klasör gibi mount etmeden içindeki dosyaları inceleyebilirsin.

## 12. Opsiyonel read-only mount

Linux lab makinesinde istersen:

```bash
mkdir -p mountpoint
sudo mount -o loop,ro lab-disk.img mountpoint
ls -la mountpoint
cat mountpoint/note.txt
sudo umount mountpoint
```

Önemli option:

```text
ro = read-only
```

Forensic çalışmada gereksiz write işlemlerini azaltmak temel alışkanlıklardan biridir.

Software read-only mount eğitim için faydalıdır. Profesyonel acquisition süreçlerinde ayrıca hardware/software write blocker ve özel forensic tool'lar kullanılabilir.

## 13. İnceleme sonrası tekrar doğrula

```bash
sha256sum -c lab-disk.sha256
```

Beklenen:

```text
lab-disk.img: OK
```

Hash aynıysa image byte'ları baseline ile aynıdır.

Day 1'deki sınırlamayı unutma: hash byte'ların bilinen baseline ile aynı olduğunu gösterebilir; evidence'ı kimin kullandığını veya acquisition'ın doğru yapıldığını tek başına açıklamaz.

## 14. Read-only neden önemli?

Evidence'ı normal araçlarla açmak; OS, filesystem, mount mode veya application davranışına göre bazı write işlemlerine neden olabilir.

Örneğin metadata veya application-generated file değişebilir.

Forensic düşünce:

```text
sadece:
"Bunu açabilir miyim?"

değil:

"Bu işlem evidence'ı değiştirir mi?"
```

sorusunu da sor.

## 15. Acquisition ve analysis

### Acquisition
Evidence temsilini mümkün olduğunca değişikliği azaltarak elde etmek ve süreci belgelemek.

### Verification
Hash ve kayıtlarla analiz edilen image'ın baseline ile aynı olduğunu doğrulamak.

### Analysis
Doğrulanmış copy/image'ı uygun araçlarla incelemek.

### Reporting
Neyin, nasıl gözlemlendiğini ve sınırlamaları belgelemek.

## 16. Evidence notları

Bu labdaki `image-analysis-template.txt` dosyasına:

- image name
- image size
- SHA-256
- filesystem type
- volume label
- kullanılan tools
- read-only status
- observations
- final verification

bilgilerini yazabilirsin.

İleride daha formal case documentation'a geçebiliriz.

## 17. Bu lab neyi kanıtlamaz?

Image içinde `note.txt` bulmak yalnızca examination'ın desteklediği şeyi söyler.

Tek başına şunları kanıtlamaz:

- dosyayı kimin oluşturduğu,
- bilgisayarı kimin kullandığı,
- dosyanın neden bulunduğu,
- timestamp'in kesin olarak insan aktivitesini gösterdiği,
- original acquisition'ın hukuki/prosedürel olarak doğru olduğu.

Forensic raporlama dikkatli ifade gerektirir.

Desteksiz:

> “Kullanıcı bu dosyayı oluşturdu.”

yerine evidence'ın desteklediği:

> “İncelenen image içinde note.txt adlı bir dosya bulundu.”

gibi ifade daha doğrudur.

## 18. Forensics bağlantısı

Filesystem image sayesinde analyst:

- file/directory
- filesystem metadata
- allocation structure
- timestamp
- ileride deleted-file artifact
- filesystem-specific evidence

inceleyebilir.

Amaç original storage'ı normal çalışma diski gibi kullanmadan analiz yapmaktır.

## Mini lab workflow

```text
zararsız seed file oluştur
        ↓
EXT4 training image oluştur
        ↓
SHA-256 baseline al
        ↓
filesystem'i identify et
        ↓
metadata incele
        ↓
debugfs ile file oku
        ↓
opsiyonel read-only mount
        ↓
SHA-256 tekrar doğrula
        ↓
gözlemleri belgeleyin
```

## Alıştırmalar

1. 32 MiB training image oluştur.
2. SHA-256 değerini kaydet.
3. `file` ile filesystem'i tanımla.
4. `dumpe2fs -h` ile volume label'ı bul.
5. `debugfs` ile root directory'yi listele.
6. Image'ı mount etmeden `note.txt` içeriğini oku.
7. `debugfs` output'unda bir inode number kaydet.
8. İstersen image'ı read-only mount edip incele.
9. Analizden sonra original image hash'ini doğrula.
10. Logical file copy ile filesystem image farkını kendi cümlenle açıkla.

## Sorular

1. Filesystem nedir?
2. Filesystem/disk image nedir?
3. Evidence image neden hash'lenir?
4. Read-only examination neyi önlemeye çalışır?
5. EXT filesystem'de inode'un temel görevi nedir?
6. Inode ile filename aynı şey midir?
7. Acquisition ve analysis neden ayrı aşamalardır?
8. Değişmeyen SHA-256 neyi gösterir, neyi göstermez?
9. Bu labda neden gerçek device'ları formatlamamalısın?
10. Forensic conclusion neden dikkatli yazılmalıdır?

## Ana çıkarım

```text
storage
   ↓
filesystem
   ↓
forensic image
   ↓
hash + preserve
   ↓
read-only examination
   ↓
verify + document
```

En önemli şey komut syntax'ını ezberlemek değil; evidence'ı korumak ve gözleminin gerçekten neyi desteklediğini bilmektir.
