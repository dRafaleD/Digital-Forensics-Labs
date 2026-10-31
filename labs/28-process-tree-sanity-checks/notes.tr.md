# Gün 28 — Süreç Ağacı Tutarlılık Kontrolleri

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Süreç Ağacı Tutarlılık Kontrolleri** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Bilinen sistem süreçlerinin beklenen ebeveynleri vardır; farklı bir ebeveyn kontrol edilmesi gereken bir ipucudur.
2. Ebeveyn PID'si listede bulunmayan süreç, ebeveyni çıkmış öksüz bir süreç olabilir.
3. Yalnızca ada değil; ebeveyn, yol ve başlangıç zamanını birlikte kontrol et.

## Kavramsal ayrımlar
- Başlatıcı çıktıktan sonra öksüz süreçler normaldir.
- PID'ler yeniden kullanılır; gerçek veride PID ile başlangıç zamanını birlikte eşle.
- Bellek görüntüsü bir andır ve zaten sonlanmış süreçleri kaçırır.

## Lab uygulaması
Önce `proctree_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 proctree_demo.py
~~~


## Görevler
1. Hangi süreçlerin işaretleneceğini tahmin et.
2. Demoyu çalıştırıp her işaretin nedenini not et.
3. Meşru bir öksüz süreç ekle ve onu nasıl eleyeceğini anlat.
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
