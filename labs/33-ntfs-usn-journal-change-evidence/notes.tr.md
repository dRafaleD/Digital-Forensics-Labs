# Gün 33 — NTFS USN Journal: Dosya Değişikliği ve Aktör Atfı Ayrımı

[English](notes.md) · [Türkçe](notes.tr.md) · [Sentetik zaman çizelgesi](usn_timeline_demo.py)

## Bir dosyanın değişmesi, kimin değiştirdiğini söylemez
32. günde farklı kaynakların aynı olay için çelişkili bilgi verebileceğini görmüştük. Bugün Windows NTFS üzerindeki **değişiklik günlüğü** kavramına geçiyoruz: `$UsnJrnl`. Bu günlük bir dosya/dizin nesnesindeki değişiklikleri gösterebilir. Ancak tek başına **hangi kullanıcının, uygulamanın veya sürecin işlemi başlattığını** kanıtlamaz.

## Alanları yorumlamak
Gerçek USN kayıtlarında dosya referansı, üst dizin referansı, değişiklik sebebi bayrakları, ad ve zaman bilgisi bulunabilir.

- **USN değeri:** Belirli journal içindeki konum/sıralama bilgisidir; doğrudan zaman damgası değildir ve `+1` artan basit olay sayacı olarak düşünülmemelidir.
- **Reason bayrakları:** Dosya oluşturma, veri uzatma, kapatma gibi değişiklik türleri hakkında ipucu verir. Gerçekte bit alanları şeklindedir, tek bir basit etiket olmayabilir.
- **Dosya adı:** Benzersiz kimlik değildir. Farklı dosya nesneleri aynı ismi taşıyabilir.
- **Eksik geçmiş:** Journal'ın dönmesi, saklama kapasitesi veya toplama koşulları nedeniyle eski kayıtlar bulunmayabilir. USN sayıları arasındaki boşluk **tek başına silme/sahtecilik kanıtı değildir**.

## Çevrimdışı uygulama
```bash
python3 usn_timeline_demo.py
```
Program gerçek Windows diskine erişmez. `model.bin` adlı hayalî dosyaya ait oluşturma, veri değiştirme ve kapatma kayıtları üretir. Daha sonra **aynı adı taşıyan ama dosya referansı farklı** ikinci bir nesne ekler. Kayıtları dosya referansına göre gruplayıp USN sırasına dizer. Son raporda **başlatıcı: bilinmiyor** yazar.

## Alıştırmalar
1. Hangi olaylar aynı dosya referansına ait, hangileri ayrı?
2. Daha büyük USN değeri neden tek başına daha geç duvar saati zamanını kanıtlamaz?
3. `FILE_CREATE` olayı gerçekten bir **indirmeyi** kanıtlar mı?
4. Aktör atfı için Sysmon, süreç oluşturma kayıtları, tarayıcı geçmişi ve `Zone.Identifier` gibi hangi kaynaklar yardımcı olabilir?
5. Günlük geçmişinin bir kısmı kaybolmuşsa raporunda belirsizliği nasıl gösterirsin?
6. “Gözlenen iz”, “yorum”, “ek kanıt” ve “güven düzeyi” başlıklı bir tablo hazırla.

## Adli sınırlar
Tek bir USN izinden **insan**, **otomasyon**, **yapay zekâ ajanı** veya **zararlı** sonucuna varma. Gerçek olayda yetkili toplama yöntemi, dosya bütünlüğü ve kaynakların karşılıklı doğrulanması gerekir. Bu dosya bir NTFS parser'ı değildir.
