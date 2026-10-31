# Gün 24 — E-posta Başlığı Hop Sırası ve Zaman Damgası Kontrolleri

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **E-posta Başlığı Hop Sırası ve Zaman Damgası Kontrolleri** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Her posta sunucusu en üste bir `Received` satırı ekler; alttan okumak göndericiden alıcıya yolu gösterir.
2. Yol boyunca zaman damgaları azalmamalıdır; azalma saat kayması veya sahte satır anlamına gelir.
3. Yalnızca güvendiğin sunucuların eklediği satırlar güvenilirdir; alt satırları gönderen taklit edebilir.

## Kavramsal ayrımlar
- Küçük negatif farklar genelde sunucular arası saat kaymasıdır, sahtecilik değil.
- Geçerli bir hop zinciri mesaj içeriğinin gerçek olduğunu kanıtlamaz.
- Analiz ettiğin her başlığın kaynağını kaydet.

## Lab uygulaması
Önce `headers_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 headers_demo.py
~~~


## Görevler
1. Hangi hop çiftinin sıra dışı olduğunu tahmin et.
2. Demoyu çalıştırıp boşlukların büyüklüğünü karşılaştır.
3. Tolere edilen kaymayı 5 saniye yap ve etkisini anlat.
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
