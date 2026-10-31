# Gün 23 — Program Çalıştırma Kalıntıları ve Olağandışı Yollar

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Program Çalıştırma Kalıntıları ve Olağandışı Yollar** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Çalıştırma kalıntıları hangi programın ne sıklıkla ve ne zaman çalıştığını kaydeder; bu zaman çizelgesi için yararlıdır.
2. Temp veya indirme klasörleri gibi olağandışı konumlar, özellikle nadir çalışan dosyalar için daha yakından incelenmeyi hak eder.
3. Bir kalıntı programın başlatıldığını kanıtlar; ne yaptığını veya kimin başlattığını değil.

## Kavramsal ayrımlar
- Yazılım yükleyicileri ve güncellemeler meşru olarak temp yollarından çalışır.
- Kalıntılar silinebilir veya zamanla düşer; yokluk zayıf bir kanıttır.
- Sonuca varmadan önce loglar ve dosya sistemi zamanlarıyla ilişkilendir.

## Lab uygulaması
Önce `execution_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 execution_demo.py
~~~


## Görevler
1. Hangi sentetik kayıtların işaretleneceğini tahmin et.
2. Demoyu çalıştırıp her işaretin nedenini not et.
3. Temp yolunda meşru bir yükleyici ekle ve onu nasıl eleyeceğini anlat.
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
