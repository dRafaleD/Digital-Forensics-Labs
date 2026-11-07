# Gün 31 — Saat Kayması ve Zaman Çizelgesi Belirsizliği

[English](notes.md) · [Türkçe](notes.tr.md) · [Uygulama](clock_skew_demo.py)

## Öğrenme amacı

Zararsız yerel veriyle **Saat Kayması ve Zaman Çizelgesi Belirsizliği** konusunun güven sınırlarını ve kanıt değerlendirmesini öğren.

## Temel kavramlar

1. Farklı sistemlerden gelen kayıtlar UTC olsa bile cihazların saat kaymaları farklı olabilir.

2. Kaynak zaman damgasını, bilinen düzeltmeyi ve güven düzeyini kaydet; orijinal delili sessizce değiştirme.

3. Belirsizlik aralıkları çakışıyorsa iki olayın kesin sırası söylenemez; raporda sonuçsuz olarak belirt.

## Güvenli pratik

Önce kaynak kodunu oku ve sonucu tahmin et:

```bash
python clock_skew_demo.py
```

Çıktı sentetiktir; gerçek sisteme komut gönderilmez.

## Görevler

1. Girdi verisini ve güvenilmeyen alanları belirle.
2. Bir negatif ya da sınır örneği ekleyip test et.
3. Gözlem ve yorum farkını açıkla.
4. Gerçek ortamda hangi doğrulamaların gerektiğini yaz.

## Kontrol soruları

- Tek gösterge yeterli mi?
- Yanlış pozitif veya eksik kayıt nasıl oluşabilir?
- Sonucu tekrar üretmek için hangi girdileri saklamalısın?

## Güvenlik ve sınırlamalar

Bu çalışma gerçek malware, bulut hesabı, sistem müdahalesi veya dış ağ gerektirmez. Modelin basitliği gerçek platformla birebir eşitlik iddiası taşımaz.
