# Gün 27 — İndirme Geçmişi ve Dosya Oluşturma Korelasyonu

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **İndirme Geçmişi ve Dosya Oluşturma Korelasyonu** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. İndirme klasöründe oluşan bir dosyanın birkaç saniye içinde bir tarayıcı indirme kaydı olmalıdır.
2. Eşleşen kaydı olmayan bir dosya kopyalama, arşiv veya başka bir program gibi farklı bir yoldan gelmiş olabilir.
3. Yol ve zaman penceresi üzerinden eşleştir ve toleransı açıkça belirt.

## Kavramsal ayrımlar
- Eksik bir kayıt farklı bir kökenden değil, temizlenmiş geçmişten kaynaklanıyor olabilir.
- Kaynaklar arası saat farkları gereken toleransı genişletir.
- Hem eşleşen hem eşleşmeyen dosyaları belgele.

## Lab uygulaması
Önce `download_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 download_demo.py
~~~


## Görevler
1. Hangi dosyaların indirme kaydı olmadığını tahmin et.
2. Demoyu çalıştırıp eşleşmeleri not et.
3. Toleransı 1 saniyeye düşür ve etkisini anlat.
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
