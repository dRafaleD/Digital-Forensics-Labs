# Gün 22 — Zaman Damgası Anomalileri ve Stomping Göstergeleri

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Zaman Damgası Anomalileri ve Stomping Göstergeleri** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Zaman damgaları değiştirilebilir; tek bir değere güvenmek yerine iç çelişkileri ara.
2. Kırmızı bayraklar: değiştirme zamanından sonraki oluşturma zamanı, sıfır alt-saniye hassasiyeti ve işletim sisteminin çıkışından önceki bir zaman.
3. Sonuca varmadan önce iki bağımsız zaman kaynağını karşılaştır (dosya sistemi ile günlük ya da log gibi).

## Kavramsal ayrımlar
- Kopyalama işlemi meşru olarak değiştirmeden sonraki oluşturma zamanı üretir; bu bir ipucudur, kurcalama kanıtı değil.
- Sıfır nanosaniye, kaba zaman saklayan bir araçtan veya dosya sisteminden gelebilir.
- Her anomaliyi, onu üreten kural ve dayandığı veriyle birlikte belgele.

## Lab uygulaması
Önce `stomp_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 stomp_demo.py
~~~


## Görevler
1. Hangi sentetik kayıtların hangi nedenle bayrak alacağını tahmin et.
2. Demoyu çalıştırıp dosya başına bayrakları not et.
3. Normal bir kopyadan oluşan bir kayıt ekle ve neden bayraklandığını açıkla.
4. Temiz bir kaydın bayrak üretmediğini doğrulayan bir assertion ekle.
5. Meşru bir kopyayı stomping'den nasıl ayıracağını anlat.
6. Bir zaman damgasını doğrulayacak bağımsız bir kaynak adlandır (günlük, olay logu, yedek).

## Kısa sınav
1. Girdi nereden geliyor ve onu kim kontrol ediyor?
2. Doğrudan gözlenen ile çıkarım yapılan arasındaki fark nedir?
3. Hangi varsayımlar gerçek sistemde geçerli olmayabilir?
4. Hangi kanıt tek başına yetersiz kalır?
5. Bir otomatik test neyi kontrol etmeli?

## Etik ve sınırlamalar
Yalnızca izinli sistemlerde ve sentetik verilerle çalış. Bu örnek tam bir tespit veya koruma ürünü değildir.
