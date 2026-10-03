# Gün 4 — Silinen Dosyalar, Filesystem Metadata ve File Carving Temelleri

## Hedefler
Filesystem seviyesinde “silme” işleminin ne anlama geldiğini, metadata tabanlı recovery ile file carving farkını, disposable bir image üzerinde güvenli çalışmayı, hash ile delil bütünlüğünü korumayı ve bulguların neyi kanıtlayıp neyi kanıtlamadığını öğrenmek.

## 1. Silmek güvenli biçimde yok etmek değildir
Bir dosya silindiğinde çoğu durumda filesystem'in içeriğe işaret eden metadata'sı kaldırılır veya değiştirilir. Veri blokları yeniden kullanılana kadar bazı byte'lar kalabilir. Recovery; filesystem davranışına, sonraki yazma işlemlerine, fragmentation'a, depolama teknolojisine ve acquisition kalitesine bağlıdır.

“Silindi, kesin kurtarılır” veya “byte bulundu, dosyayı şu kişi oluşturdu/sildi” sonucu çıkarma.

## 2. Metadata tabanlı recovery
Filesystem; isim, directory entry, inode/MFT benzeri kayıt, allocation durumu, boyut ve timestamp gibi bilgiler tutar. Yeterli metadata kaldıysa araçlar recovered content'i filesystem bağlamıyla ilişkilendirebilir.

EXT ailesinde inode dosya metadata'sı ve block referanslarını; directory entry ise isim ile inode numarası arasındaki ilişkiyi temsil eder. Silme bu ilişkileri ve allocation durumunu değiştirir.

## 3. File carving nedir?
Carving, aktif filesystem metadata'sına güvenmek yerine raw veri içinde tanınabilir dosya yapıları/signature'ları arar.

Avantaj:
- directory metadata kaybolduğunda içerik bulabilir
- unallocated/raw bölgelerde çalışabilir

Sınırlamalar:
- filename/path kaybolabilir
- timestamp bulunmayabilir
- fragmentation recovery'yi bozabilir
- signature false positive üretebilir
- bulunan byte'lar tek başına attribution kanıtı değildir

## 4. Forensic workflow
1. disposable evidence image oluştur/acquire et
2. SHA-256 hesapla
3. working copy oluştur
4. working copy hash'ini doğrula
5. kopyayı analiz et
6. komutları ve bulguları kaydet
7. gerektiğinde korunan kaynağın hash'ini tekrar doğrula

## 5. Güvenli local lab
Bu lab fiziksel diske değil küçük bir image dosyasına uygulanır.

Linux araçları:
- `dd`
- `mkfs.ext4`
- `debugfs`
- `sha256sum`
- opsiyonel `file`, `xxd`, `strings`

32 MiB image:
```bash
mkdir -p day4-lab
cd day4-lab
dd if=/dev/zero of=evidence.img bs=1M count=32 status=progress
mkfs.ext4 -F evidence.img
sha256sum evidence.img | tee evidence-before.sha256
cp evidence.img working.img
sha256sum working.img
```
Başlangıçta iki hash eşleşmelidir.

## 6. Mount etmeden kontrollü test dosyaları ekle
```bash
printf 'FORENSICS_DAY4_MARKER_A\nCase: training-only\n' > note-a.txt
printf 'FORENSICS_DAY4_MARKER_B\nDeleted sample\n' > note-b.txt
```

Yalnızca **working image** üzerinde write mode:
```bash
debugfs -w working.img
```
debugfs içinde:
```text
mkdir /case
write note-a.txt /case/note-a.txt
write note-b.txt /case/note-b.txt
ls -l /case
stat /case/note-b.txt
rm /case/note-b.txt
ls -l /case
quit
```
Silmeden önce mümkünse inode numarasını kaydet.

Orijinal `evidence.img` değişmeden kalır. `working.img` olay simülasyonu için bilerek değiştirilir.

## 7. Silinme artifact'larını incele
```bash
debugfs -R 'ls -l /case' working.img
debugfs -R 'lsdel' working.img
```
Filesystem/araç sürümüne göre davranış değişebilir. `lsdel` çıktısını recovery garantisi olarak değil gözlem olarak yorumla.

Unique marker'ı ara:
```bash
grep -a -b 'FORENSICS_DAY4_MARKER_B' working.img
strings -a -t d working.img | grep 'FORENSICS_DAY4_MARKER'
```
Marker bulunursa kontrollü image içinde byte'ların hâlâ keşfedilebilir olduğunu gösterir. Tek başına orijinal filename, path, timestamp veya kullanıcıyı kanıtlamaz.

## 8. Raw byte incelemesi
`grep -a -b` offset verirse `xxd` gibi bir hex viewer ile offset çevresindeki küçük alanı incele. Okumayı sınırlı tut ve offset'i rapora yaz. Böylece filesystem bilgisi ile raw storage arasında bağlantı kurarsın.

## 9. Metadata recovery ve carving karşılaştırması
| Soru | Metadata tabanlı recovery | Carving |
|---|---|---|
| Filesystem kayıtlarını kullanır mı? | Genellikle | Zorunlu değil |
| Filename/path koruyabilir mi? | Bazen | Genellikle hayır |
| Directory entry yoksa çalışabilir mi? | Bazen | Potansiyel olarak |
| Fragmentation etkiler mi? | Evet | Çoğu zaman ciddi |
| Tek başına attribution kanıtı mı? | Hayır | Hayır |

## 10. Integrity kontrolü
Korunan kaynağı doğrula:
```bash
sha256sum -c evidence-before.sha256
```
Sonra working image:
```bash
sha256sum working.img
```
Working copy'nin hash'i değişmelidir çünkü bilerek dosya ekleyip sildin. Bunun neden korunan orijinal açısından integrity failure olmadığını açıkla.

## 11. Tekrar soruları
1. Silinen veri neden bazen diskte kalabilir?
2. EXT'te inode ve directory entry'nin rolleri nedir?
3. Carving neden filename ve timestamp kaybedebilir?
4. Fragmentation carving'i nasıl etkiler?
5. Kontrollü lab'de unique marker neden faydalıdır?
6. Eşleşen SHA-256 neyi kanıtlar, neyi kanıtlamaz?
7. Neden original yerine working copy analiz edilir?
8. “Byte bulundu” ile “bu dosya şu path'te şu zamanda vardı” sonuçlarını neden ayırmalıyız?

## 12. Rapor şablonu
- image adı ve boyutu
- original SHA-256
- working copy başlangıç SHA-256
- kullanılan komutlar
- inode/metadata gözlemleri
- marker offset'leri
- recovered content
- final working-copy SHA-256
- sınırlamalar
- confidence seviyesiyle sonuç

## Günün özeti
Deleted-file forensics; filesystem metadata, allocation durumu ve raw byte'ların birlikte yorumlanmasıdır. Recovery sihir değildir. Her sonuç gözlenebilir delile, integrity kontrolüne ve açıkça belirtilmiş sınırlamalara dayanmalıdır.
