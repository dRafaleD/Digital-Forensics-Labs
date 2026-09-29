# Gün 2 — Metadata, Timestamp ve Timeline Temelleri

[🇬🇧 English](notes.md) | [🇹🇷 Türkçe](notes.tr.md)

## Amaç

File metadata ve timestamp'lerin activity reconstruction için nasıl kullanılabileceğini öğrenmek; aynı zamanda timestamp'lerin mutlak gerçek değil, yorumlanması gereken evidence olduğunu anlamak.

Bu labda:

- file metadata
- MACB tarzı timestamp terminolojisi
- `stat`
- `touch`
- timestamp karşılaştırma
- basit timeline oluşturma
- timezone farkındalığı
- metadata sınırlamaları
- observation documentation

konularını işleyeceğiz.

## 1. Metadata nedir?

Metadata, başka bir veriyi tanımlayan veridir.

Bir dosya için şunları içerebilir:

- filename
- size
- owner
- permissions
- timestamps
- filesystem identifier'ları
- extended attribute'lar

Bazı file format'ları ayrıca kendi internal metadata'sını taşır; örneğin image EXIF veya document properties.

Filesystem metadata ile file-format metadata farklı evidence kaynaklarıdır.

## 2. Temel timestamp kavramları

Linux'ta `stat` şunları gösterebilir:

```text
Access
Modify
Change
Birth
```

Başlangıç seviyesi anlamları:

- **Access time (atime):** mount/options davranışına bağlı olarak içeriğin son erişim zamanı.
- **Modify time (mtime):** file content'in son değiştirildiği zaman.
- **Change time (ctime):** inode metadata/content status değişim zamanı.
- **Birth/creation time:** filesystem destekliyorsa object creation zamanı.

Önemli:

> Linux `ctime`, "creation time" değildir.

Inode **change** time anlamına gelir.

## 3. stat ile metadata incele

```bash
stat evidence/timeline-sample.txt
```

Şunları kaydet:

- file size
- permissions
- owner/group
- Access
- Modify
- Change
- varsa Birth

Filesystem her alanı göstermeyebilir.

## 4. Baseline oluştur

Önce hash:

```bash
sha256sum evidence/timeline-sample.txt
```

Sonra metadata:

```bash
stat evidence/timeline-sample.txt > before-stat.txt
```

Controlled change öncesi baseline elde etmiş olursun.

## 5. Working copy üzerinde değişiklik

```bash
cp evidence/timeline-sample.txt evidence/timeline-working.txt
```

Metadata:

```bash
stat evidence/timeline-working.txt
```

Zararsız satır ekle:

```bash
echo "Controlled modification" >> evidence/timeline-working.txt
```

Tekrar:

```bash
stat evidence/timeline-working.txt
sha256sum evidence/timeline-working.txt
```

Hangi timestamp'lerin değiştiğini gözlemle.

## 6. Sadece metadata değişikliği

Working copy permission'ını değiştir:

```bash
chmod 600 evidence/timeline-working.txt
```

Sonra:

```bash
stat evidence/timeline-working.txt
```

Sor:

- File content değişti mi?
- SHA-256 değişti mi?
- Metadata timestamp'leri değişti mi?

Bu, content değişmeden filesystem metadata'nın değişebileceğini gösterir.

## 7. touch ve timestamp

`touch` timestamp'leri güncelleyebilir:

```bash
touch evidence/timeline-working.txt
stat evidence/timeline-working.txt
```

Forensics açısından önemlidir çünkü timestamp normal sistem davranışı veya bilinçli işlem sonucunda değiştirilebilir.

Bu yüzden:

> Timestamp, başka evidence ile correlate edilmesi gereken bir observation'dır.

## 8. Timezone farkındalığı

Birden fazla sistemin timestamp'lerini timezone dikkate almadan karşılaştırırsan timeline yanlış yorumlanabilir.

Şunları kaydet:

- timezone
- UTC offset
- tool local time mı UTC mi gösteriyor
- timestamp'ler farklı sistemlerden mi geliyor

Örnek:

```text
2026-09-29 10:00 UTC
2026-09-29 13:00 UTC+03
```

Aynı anı ifade edebilir.

## 9. Basit forensic timeline

```text
Time                Event
------------------  ------------------------------
10:02:14            File copied
10:03:01            Working copy modified
10:03:20            SHA-256 recalculated
10:04:10            Permissions changed
```

Bu labda yaptığın işlemleri manuel kaydet.

Amaç event ordering pratiği yapmak; tam bir forensic timeline sistemi kurmak değil.

## 10. File metadata ve content ayrımı

```text
content hash -> file byte'larını tanımlar
metadata     -> filesystem/file attribute'larını tanımlar
```

İki dosyanın hash'i aynı olabilir ama:

- filename
- path
- owner
- permissions
- timestamps

farklı olabilir.

Copy işleminde bu sık görülür.

## 11. İsteğe bağlı file-format metadata

`exiftool` kuruluysa:

```bash
exiftool evidence/timeline-sample.txt
```

Text file çok fazla internal metadata içermeyebilir. İleride safe image/document ile embedded metadata çalışabiliriz.

Embedded metadata'nın da editlenebilir veya silinebilir olduğunu unutma.

## 12. Metadata sınırlamaları

Timestamp ve metadata şunlardan etkilenebilir:

- copying
- archive extraction
- filesystem davranışı
- mount options
- backup/restore tools
- application behavior
- manual modification
- clock drift
- timezone farkları

Mümkün olduğunda forensic conclusion birden fazla evidence source ile desteklenmelidir.

## 13. Mini workflow

```text
1. Original sample'ı hashle
2. stat output kaydet
3. Working copy oluştur
4. Working copy'yi değiştir
5. Tekrar hashle
6. Timestamp'leri karşılaştır
7. Permissions değiştir
8. Timestamp'leri tekrar karşılaştır
9. Küçük timeline oluştur
10. Limitasyonları belgeley
```

## 14. Sorular

1. Metadata nedir?
2. mtime ve ctime farkı nedir?
3. Linux ctime neden creation time değildir?
4. File content değişmeden metadata değişebilir mi?
5. Aynı SHA-256'a sahip iki dosyanın timestamp'leri farklı olabilir mi?
6. Timeline analizinde timezone neden önemlidir?
7. Timestamp neden başka evidence ile correlate edilmelidir?
8. `touch` forensic labda neyi gösterebilir?

## Ana çıkarım

```text
metadata
   +
timestamps
   +
hashes
   +
documented actions
   ↓
daha iyi event reconstruction
```

Tek bir timestamp'i bütün hikâye olarak görme.
