# Gün 1 — Dijital Delil, Bütünlük ve Hashing

[🇬🇧 English](notes.md) | [🇹🇷 Türkçe](notes.tr.md)

## Amaç

İlk adli bilişim alışkanlığını öğrenmek: **analiz etmeden önce delili korumak**.

Bu labda:

- digital evidence
- original ve working copy
- acquisition ve analysis farkı
- evidence integrity
- cryptographic hash
- SHA-256
- chain of custody kavramı
- tekrar edilebilir doğrulama

konularını işleyeceğiz.

## 1. Dijital delil nedir?

Digital evidence, bir inceleme veya araştırma sorusunu cevaplamaya yardımcı olabilecek dijital formdaki bilgidir.

Örnekler:

- dosyalar
- loglar
- disk image'ları
- memory capture'ları
- browser artifact'ları
- network capture'ları
- metadata
- timestamp'ler

Her dosya otomatik olarak delil değildir. Bir soru veya investigation ile ilişkili hale geldiğinde anlam kazanır.

## 2. Önce koru, sonra analiz et

Temel forensic prensiplerden biri original materyali gereksiz yere değiştirmemektir.

Basit model:

```text
original evidence
      ↓
koru
      ↓
working copy oluştur
      ↓
copy'yi doğrula
      ↓
copy üzerinde analiz yap
```

Profesyonel workflow'larda acquisition özel araç ve prosedürler içerebilir. İlk labda integrity mantığını net görmek için zararsız bir text dosyası kullanıyoruz.

## 3. Original ve working copy

Bu labda:

```text
evidence/original.txt
```

dosyasını original evidence olarak düşüneceğiz.

Working copy:

```bash
cp evidence/original.txt evidence/working-copy.txt
```

Deneylerini original yerine working copy üzerinde yap.

## 4. Cryptographic hash nedir?

Hash function input verisini alıp fixed-size bir digest üretir.

```text
file bytes
   ↓
SHA-256
   ↓
digest
```

Dosya değişirse digest de normalde değişir.

Hash, iki byte stream'in aynı olup olmadığını kontrol etmek için çok kullanışlıdır.

## 5. SHA-256 hesapla

Linux:

```bash
sha256sum evidence/original.txt
sha256sum evidence/working-copy.txt
```

Dosyalar birebir kopyaysa SHA-256 değerleri eşleşmelidir.

Verification file:

```bash
sha256sum evidence/original.txt > hashes.sha256
```

Sonradan kontrol:

```bash
sha256sum -c hashes.sha256
```

Beklenen:

```text
evidence/original.txt: OK
```

## 6. Integrity deneyi

Önce hashleri kaydet:

```bash
sha256sum evidence/original.txt evidence/working-copy.txt
```

Sonra **yalnızca working copy'yi** değiştir:

```bash
echo "Training modification" >> evidence/working-copy.txt
```

Tekrar hash:

```bash
sha256sum evidence/original.txt evidence/working-copy.txt
```

Artık digest'ler farklı olmalıdır.

Bu şu prensibi gösterir:

> Hash, byte'ların değiştiğini göstermeye yardımcı olabilir.

Ancak dosyanın **neden** veya **kim tarafından** değiştirildiğini söylemez.

## 7. Hash filename değildir

İki farklı isimli dosya aynı içeriğe sahip olabilir:

```text
original.txt
copy.txt
```

Byte'lar aynıysa SHA-256 da aynıdır.

Aynı filename'e sahip iki dosyanın içeriği farklıysa hashleri de farklı olabilir.

Forensics'te yalnızca filename değil, gerçek veri önemlidir.

## 8. Acquisition ve analysis

### Acquisition

İncelenecek verinin forensic copy veya capture'ını elde etme aşamasıdır.

### Analysis

Elde edilen veri üzerinde investigation sorularını cevaplamak için yapılan incelemedir.

Bu iki aşamayı kavramsal olarak ayırmak source materyali korumaya ve workflow'u belgelemeye yardımcı olur.

## 9. Chain of custody

Chain of custody; evidence'ın nasıl collect edildiği, transfer edildiği, saklandığı ve kimler tarafından işlendiğinin kaydıdır.

Basit training log:

```text
Evidence ID:
Description:
Collected by:
Date/time:
Source:
Hash:
Copy created:
Analysis notes:
```

Amaç traceability sağlamaktır.

Hash integrity hakkında bilgi verir ama documentation'ın yerine geçmez.

## 10. Basit evidence log oluştur

```text
evidence-log.txt
```

Örnek:

```text
Evidence ID: DF-LAB-001
Description: Harmless training text file
Source: Local lab repository
Original file: evidence/original.txt
Hash algorithm: SHA-256
Original SHA-256: <kendi sonucunu yaz>
Working copy: evidence/working-copy.txt
Notes: Working copy used for modification experiment
```

Başkasının hash sonucunu kopyalama; kendi makinen üzerinde üret.

## 11. Neden SHA-256?

SHA-256 yaygın olarak bulunur ve bu eğitim bağlamında integrity verification için uygundur.

MD5 ve SHA-1 forensic tooling veya eski datasetlerde hâlâ karşına çıkabilir; ancak bilinen collision zayıflıkları vardır ve modern collision-resistant tercih olarak görülmemelidir.

Bu repoda aksi belirtilmedikçe SHA-256 kullanacağız.

## 12. Faydalı komutlar

Metadata:

```bash
stat evidence/original.txt
```

Byte-by-byte karşılaştırma:

```bash
cmp evidence/original.txt evidence/working-copy.txt
```

Output yoksa `cmp` fark bulmamıştır.

Working copy'yi değiştirdikten sonra tekrar dene.

## 13. Mini lab workflow

```text
1. Original'i incele
2. Original'i hashle
3. Copy oluştur
4. Copy'yi hashle
5. Hashlerin eşleştiğini doğrula
6. Bilgiyi kaydet
7. Sadece copy'yi değiştir
8. Tekrar hashle
9. Farkı gözlemle
10. Original'i değiştirme
```

## 14. Sorular

1. Original evidence neden korunmalıdır?
2. Acquisition ve analysis arasındaki fark nedir?
3. Eşleşen SHA-256 hash ne söyler?
4. Hash dosyayı kimin değiştirdiğini kanıtlar mı?
5. Neden deneyler working copy üzerinde yapılmalıdır?
6. Filename neden tek başına file identity için yeterli değildir?
7. Chain-of-custody documentation ne işe yarar?
8. MD5 ve SHA-1 neden modern collision-resistant hash olarak tercih edilmez?

## Ana çıkarım

İlk forensic alışkanlık "dosyayı aç ve kurcalamaya başla" değildir.

```text
preserve
   ↓
copy
   ↓
hash
   ↓
verify
   ↓
document
   ↓
analyze
```

İyi bir forensic workflow original veriyi korur ve yaptığın işlemleri tekrar üretilebilir ve açıklanabilir hale getirir.
