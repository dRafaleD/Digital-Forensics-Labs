# Gün 19 — Uçuculuk Sırası ve Delil Toplama Önceliği

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Uçuculuk Sırası ve Delil Toplama Önceliği** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Deliller farklı hızlarda kaybolur: önce bellek ve ağ durumu, sonra disk, en sonda yedekler.
2. En uçucu kaynaktan başla; eşitlik halinde delil değerine bak.
3. Her toplama eylemi sistemi değiştirir; ne yaptığını, ne zaman ve hangi araçla yaptığını kaydet.

## Kavramsal ayrımlar
- Uçuculuk delilin ne kadar hızlı kaybolduğunu, değer ise vakaya ne kadar katkı sağladığını anlatır.
- Katı bir sıra varsayılandır, yasa değildir: hukuki veya güvenlik kısıtları sırayı değiştirebilir.
- Toplanan bir kalıntı ancak kaynağı ve hash'i kaydedildiyse işe yarar.

## Lab uygulaması
Önce `volatility_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 volatility_demo.py
~~~


## Görevler
1. Demoyu çalıştırmadan önce toplama sırasını tahmin et.
2. Çalıştırıp çıktıyı tahminle karşılaştır.
3. 90 gün saklanan `Cloud audit logs` kaynağını ekle ve sıradaki yerine karar ver.
4. Aynı değerdeki kısa ömürlü kaynağın uzun ömürlüden sonra toplanmadığını doğrulayan bir assertion ekle.
5. Düşük uçuculuktaki bir kaynağın önce toplanması gereken bir durum anlat ve nedenini yaz.
6. RAM topladıktan sonra vaka günlüğüne yazacağın notu yaz.

## Kısa sınav
1. Girdi nereden geliyor ve onu kim kontrol ediyor?
2. Doğrudan gözlenen ile çıkarım yapılan arasındaki fark nedir?
3. Hangi varsayımlar gerçek sistemde geçerli olmayabilir?
4. Hangi kanıt tek başına yetersiz kalır?
5. Bir otomatik test neyi kontrol etmeli?

## Etik ve sınırlamalar
Yalnızca izinli sistemlerde ve sentetik verilerle çalış. Bu örnek tam bir tespit veya koruma ürünü değildir.
