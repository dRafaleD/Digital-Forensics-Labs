# Gün 30 — Shell Geçmişi Kalıntıları ve Komut Zaman Çizelgesi

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Shell Geçmişi Kalıntıları ve Komut Zaman Çizelgesi** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Bir shell geçmiş dosyası komutları kaydedebilir ve zaman damgalarıyla yazılanların zaman çizelgesine dönüşür.
2. Tek tek komutlar yerine, bir dosya getirme, çalıştırılabilir yapma ve çalıştırma gibi dizilere bak.
3. Geçmişi kullanıcının kendi shell'i yazar; bu yüzden eksik olabilir, düzenlenmiş olabilir veya hiç kaydedilmemiş olabilir.

## Kavramsal ayrımlar
- Bir dizi ipucudur; yöneticiler ve geliştiriciler bunu meşru olarak çalıştırır.
- Geçmişin olmaması zayıf bir kanıttır, hiçbir şey olmadığının kanıtı değil.
- Zaman çizelgesi kurmadan önce epoch zamanlarını UTC'ye çevir.

## Lab uygulaması
Önce `history_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 history_demo.py
~~~


## Görevler
1. Hangi komut penceresinin işaretleneceğini tahmin et.
2. Demoyu çalıştırıp işaretlenen dizinin zaman damgalarını not et.
3. Pencereyi 10 dakikaya genişlet ve etkisini anlat.
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
