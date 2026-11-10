# Gün 34 — USN ve Süreç-Dosya Telemetrisini Saat Belirsizliğiyle İlişkilendirme

[English](notes.md) · [Türkçe](notes.tr.md) · [Sentetik ilişkilendirme](correlate_demo.py)

## 33. günün devamı
Bir dosyanın `$UsnJrnl` kaydında oluşturulduğunu veya değiştirildiğini görmek, o işlemi **kimin başlattığını** doğrudan söylemez. Süreç ve dosya olaylarına ilişkin başka loglar da toplayabiliriz. Fakat **aynı zamana yakın olmak, aynı nedene sahip olmak demek değildir**.

## Hangi verileri karşılaştıracağız?
Programda üç çeşit hayalî USN-benzeri kayıt bulunuyor: dosya referansı, değişiklik sebebi, zaman damgası ve kanıt ID'si. Ayrı bir kaynak ise dosya ile ilişkilendirilmiş süreç olaylarını bildiriyor.

**Dikkat:** Gerçek Sysmon, Windows Event Log ve NTFS kaynaklarının alanları birbirinin aynısı değildir. Örnekteki ortak `file_ref` alanı özellikle kolaylaştırılmıştır; bunu gerçek sistemlerde her logda varmış gibi kabul edemeyiz.

**Zaman belirsizliği:** İki kaynağın saatleri birebir eşleşmeyebilir. Örnekte `±2 saniye` tolerans kullanıyoruz. Gerçek vakalarda bu değeri olayları eşleştirmek için keyfî seçmek yerine saat senkronizasyonu ve toplama bilgileriyle gerekçelendirmek gerekir.

## Karar kategorileri
- **Aday yok:** Eşleşen süreç-dosya kaydı bulunmadı; başlatıcı bilinmiyor.
- **Bir aday:** Zaman ve nesne kimliğine göre olası bağlantı var; **aktör kanıtlanmış değil**.
- **Birden fazla aday:** İlişki belirsiz; seçenekleri ve olası çelişkileri gizleme.

## Uygulama
```bash
python3 correlate_demo.py
```
Program üç durumu da üreten sentetik olayları kullanır. Kaynak kayıtlarını değiştirmeden adayları listeler ve beklenen durumları `assert` ile kontrol eder. Gerçek disk/Windows loguna erişmez.

## Alıştırmalar
1. USN değerinin neden doğrudan zaman damgası olmadığını anlat.
2. Saatlerden biri 90 saniye ilerideyse hangi eşleşmeler kaybolabilir?
3. Bir dosya yazımının hangi süreçten kaynaklandığını anlamak için hangi **bağımsız kanıtlar** gerekir?
4. Sadece dosya adına göre eşleştirme neden yanıltıcı?
5. Kaynak ID, orijinal saat, normalleştirilmiş saat, gözlem, çıkarım ve belirsizliği içeren rapor tasarla.
6. Araştırmada doğruluk/duyarlılık ölçmek için neden gerçek aktörü bilinen senaryolar gereklidir?

## Sınırlar
Bu bir NTFS veya Sysmon parser'ı değildir. Dosya referanslarının geçerliliği volume ve yaşam döngüsüyle sınırlıdır. Log eksikliği, saat kayması ve aktör belirsizliği gerçek adli analizde mutlaka değerlendirilmelidir.
