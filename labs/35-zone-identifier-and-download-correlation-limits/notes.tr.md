# Gün 35 — Zone.Identifier ve İndirme Geçmişi Korelasyonunun Sınırları

[English](notes.md) · [Türkçe](notes.tr.md) · [Sentetik korelasyon](download_correlation_demo.py)

## 34. günden devam
34. günde USN benzeri dosya kayıtlarını süreç olaylarıyla zaman bakımından eşleştirdik. Yakın zamanlı iki olayın **tek başına neden-sonuç ilişkisi** kurmadığını gördük. Şimdi Windows'ta indirilen dosyalar için iki veri kaynağını inceleyeceğiz:

- **Tarayıcı indirme geçmişi:** Tarayıcının kaydettiği hedef dosya yolu, zaman ve kaynak adresi gibi bilgiler.
- **Zone.Identifier (Mark-of-the-Web):** NTFS üzerinde bazen dosyaya eklenen **Alternate Data Stream (ADS)**. ZoneId=3 gibi bir değer Internet bölgesiyle ilişkiyi gösterebilir; bazı durumlarda kaynak URL bilgisi de bulunabilir.

**Önemli:** Zone.Identifier her dosyada zorunlu olarak bulunmaz. Uygulama, Windows politikası, dosyanın kopyalandığı sistem, dosya açma/çıkarma işlemi ve dosya sistemi bu izi etkileyebilir. Zone.Identifier'ın varlığı, belirli bir insanın veya yapay zekâ ajanının dosyayı indirdiğini kanıtlamaz.

## Korelasyon nasıl yapılır?
Oyuncak modelde dosya yolu ve kayıt zamanı üzerinden adaylar eşleştirilir. ±2 saniyelik pencere sadece **örnek amaçlıdır**, gerçek saat sapmasını temsil etmez.

Üç olası sonuç:
1. **Tek aday:** Bir tarayıcı olayı Zone.Identifier gözlemiyle zaman ve yolda uyuşuyor. Bu **olası ilişki** demektir.
2. **Birden çok aday:** Hangi kaydın ilişkili olduğu belirsiz.
3. **Aday yok:** Eldeki iki veri kaynağı üzerinden ilişki kurulamadı.

Dosyanın yeniden adlandırılması, kopyalanması, içerik değiştirilmesi veya kaydın eksik toplanması sonuçları etkileyebilir. Dosya adı tek başına kalıcı kimlik değildir.

## Çalıştır
~~~bash
python3 download_correlation_demo.py
~~~

Program gerçek diski, ADS'yi veya tarayıcı geçmişini **okumaz**. Kurgusal kayıtlar üzerinden tek/çok/sıfır aday durumlarını hesaplar, assert ile denetler ve **başlatıcı: bilinmiyor** bilgisini korur.

## Görevler
1. Zone.Identifier bulunmaması neden indirme gerçekleşmediğini kanıtlamaz?
2. Internet zone işareti neyi söyler, neyi söylemez?
3. Aynı isimde iki dosya varsa hangi karışıklık doğar?
4. SHA-256, dosya referansı ve normalize edilmiş zaman gibi ek alanlar ne kadar yardımcı olur?
5. NTFS dışındaki bir dosya sistemine kopyalamak hangi izleri etkileyebilir?
6. Aktör atfı çalışmasında Sysmon, süreç kayıtları, USN, Prefetch ve tarayıcı geçmişini nasıl birbirinden bağımsız kaynaklar olarak kullanırsın?

## Sınırlar
Bu bir adli veri toplama aracı ya da Windows artifact parser'ı değildir. Sadece sentetik veri vardır; zaman yakınlığından kesin kullanıcı/otomasyon/ajan/zararlı atfı yapılamaz.
