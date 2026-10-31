# Gün 25 — Windows Oturum Açma Türleri ve Uzak Oturum Triage'ı

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Windows Oturum Açma Türleri ve Uzak Oturum Triage'ı** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Oturum olaylarında bir logon türü bulunur: 2 etkileşimli, 3 ağ, 10 uzak etkileşimli (RDP) oturumdur.
2. Dış bir adresten gelen veya olağandışı saatteki tür 10, incelenmesi gereken güçlü bir ipucudur.
3. Hikâyenin tamamını görmek için başarılı oturumları önceki başarısızlıklar ve kaynak adresle eşleştir.

## Kavramsal ayrımlar
- Yöneticiler meşru olarak RDP kullanır; bağlam belirler.
- Logon türleri, onları üreten denetim politikası kadar eksiksizdir.
- Eksik olaylar günlüklemenin kapalı olduğu anlamına gelebilir, hiçbir şey olmadığı anlamına değil.

## Lab uygulaması
Önce `logon_types_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 logon_types_demo.py
~~~


## Görevler
1. Hangi olayların işaretleneceğini tahmin et.
2. Demoyu çalıştırıp her nedeni not et.
3. Dahili bir yönetici RDP oturumu ekle ve neden işaretlenmediğini açıkla.
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
