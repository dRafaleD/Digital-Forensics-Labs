# Gün 26 — Kararlı Takma Adlarla Rapor Karartma

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Kararlı Takma Adlarla Rapor Karartma** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Kullanıcı adı ve adres gibi tanımlayıcıları hikâye okunabilir kalsın diye kararlı takma adlarla değiştir.
2. İnsanlar tahminleri hash'leyerek takma adları geri çözemesin diye anahtarlı hash kullan.
3. Eşleme anahtarını ve özgün delili paylaşılan raporun dışında, kontrollü depoda tut.

## Kavramsal ayrımlar
- Takma adlar kimliği korur ama ilişkilendirmeye izin verir; hem fayda hem risk budur.
- Karartma yalnızca gövde metnini değil, metaveriyi, dosya adlarını ve ekran görüntülerini de kapsamalıdır.
- Yalnızca sentetik veriyle test et.

## Lab uygulaması
Önce `redact_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 redact_demo.py
~~~


## Görevler
1. Tekrarlanan kullanıcı adı için takma adı tahmin et.
2. Demoyu çalıştırıp özgün isimlerin kalktığını doğrula.
3. Anahtarı değiştir ve takma adlara ne olduğunu anlat.
4. Bir güvenlik özelliği için assertion ekle.
5. Bir negatif senaryo ve bir yanlış pozitif ihtimali yaz.
6. Bağımsız bir doğrulama yöntemi öner.

## Kısa sınav
1. Girdi nereden geliyor ve onu kim kontrol ediyor?
2. Doğrudan gözlenen ile çıkarım yapılan arasındaki fark nedir?
3. Hangi varsayımlar gerçek sistemde geçerli olmayabilir?
4. Hangi kanıt tek başına yetersiz kalır?
5. Bir otomatik test neyi kontrol etmeli?

## Etik ve sınırlamalar
Yalnızca izinli sistemlerde ve sentetik verilerle çalış. Bu örnek tam bir tespit veya koruma ürünü değildir.
