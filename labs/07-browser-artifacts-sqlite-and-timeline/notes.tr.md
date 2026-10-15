# Gün 7 — Tarayıcı İzleri, SQLite Geçmişi ve Zaman Çizelgesi

[🇬🇧 English](notes.md) | [🇹🇷 Türkçe](notes.tr.md)

## Amaç
İzinli dijital delillerde tarayıcı geçmişi, indirmeler, SQLite veri yapısı, hash ve zaman çizelgesi analizini sentetik verilerle öğrenmek. Gerçek tarayıcı profilleri okunmaz.

## 1. Delil toplama ve bütünlük
Orijinal dosyayı koru. Çalışma kopyası oluştur; kaynak ve kopyanın SHA-256 değerlerini, dosya yollarını, saati ve araç sürümünü kaydet. SQLite veritabanı kullanımdayken değişebilir; tutarlı kopya alma yöntemini belgelemek gerekir.

## 2. Tarayıcı izleri
Geçmiş, indirme, cache, cookie ve profil kayıtları aynı şeyi kanıtlamaz. Tarayıcı sürümleri farklı dosya konumları ve şemalar kullanabilir.

## 3. SQLite
Sentetik veritabanında visits ve downloads tabloları bulunur. SELECT, ORDER BY ve sorgu filtreleriyle kayıtları incele. Veritabanının varlığı tek başına kullanıcı eylemi kanıtı değildir.

## 4. Zaman
Bu eğitim ISO 8601 ve +03:00 offset kullanır. Gerçek tarayıcılar farklı epoch ve birim kullanabilir. Dönüştürmeden önce formatı doğrula; kaynak timestamp'i koru.

## 5. Timeline correlation
09:14 ziyaret ve 09:15 indirme kaydı birbirine yakın olsa da nedensellik veya bir insanın niyetini kanıtlamaz. Senkronizasyon ve arka plan isteklerini düşün.

## 6. Attribution sınırları
Bir URL'nin veritabanında görülmesi belirli kişinin siteyi bilerek ziyaret ettiğini kesin göstermez. Kullanıcı profili, cihaz paylaşımı, otomatik trafik ve kayıt bütünlüğü değerlendirilmeli.

## 7. Negatif delil
Geçmiş kaydının olmaması ziyaretin hiç olmadığına dair kesin kanıt değildir. Silme, gizli mod, geçmiş saklama süresi ve toplama eksikliği olabilir.

## 8. Uygulama
```bash
python3 create_history.py
python3 analyze_history.py
sha256sum training_history.sqlite
```
Yalnızca bu labın sentetik verisini kullan.

## 9. Test matrisi
- Veritabanı üretimi iki tablo oluşturmalı.
- Ziyaretler zaman sırasına dizilmeli.
- Downloads satırı kendi timestamp'ini taşımalı.
- Okuma script'i veritabanını değiştirmemeli.
- Kaynak/kopya hash karşılaştırması yapılmalı.

## 10. Mini challenge
Ziyaret ile indirme kaydını tek timeline'da göster. Bir örnek direct observation, bir supported inference ve iki belirsizlik yaz. Sorgunu ve hash'i rapora ekle.

## Alıştırmalar
1. Sentetik veritabanını üret.
2. Dosya hash'i al.
3. Şemayı incele.
4. SELECT ile visits oku.
5. Downloads oku.
6. Zaman sırasına göre sırala.
7. İki tabloyu tek timeline'da birleştir.
8. Bir çalışma kopyası oluştur.
9. Hash kontrolü yap.
10. Örnek rapor yaz.
11. Kayıt yokluğunun iki açıklamasını yaz.
12. Gerçek profil dosyası açmadan analizi tekrar et.

## Tekrar soruları
1. SQLite nedir?
2. Tarayıcıda hangi izler kalabilir?
3. Hash ne işe yarar?
4. Orijinal veri neden korunmalı?
5. Read-only sorgu neden önemlidir?
6. Timezone neden kaydedilir?
7. Epoch farklılıkları hangi riski yaratır?
8. Ziyaret kaydı neyi kanıtlar?
9. Ziyaret kaydı neyi kanıtlamaz?
10. İndirme ile ziyaret nasıl ilişkilendirilebilir?
11. Correlation nedensellik midir?
12. Gizli mod hangi yorum hatasına yol açabilir?
13. Tarayıcı sürümleri niçin önemlidir?
14. Kopyanın bütünlüğü nasıl doğrulanır?
15. Hangi kaynak bilgileri raporlanmalıdır?
16. Eksik delil nasıl ifade edilmelidir?

## Ana çıkarım
Tarayıcı artifact'ları ipucu sunar; güvenilir adli çıkarım için kaynak bütünlüğü, zaman normalizasyonu ve belirsizliklerin açıkça kaydedilmesi gerekir.
