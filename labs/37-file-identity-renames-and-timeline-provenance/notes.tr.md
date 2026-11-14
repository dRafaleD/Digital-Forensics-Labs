# Gün 37 — Dosya Kimliği, Yeniden Adlandırma ve Zaman Çizelgesi

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](identity_timeline.py)

## 36. günden devam
İndirme ve süreç olaylarını yalnızca **dosya yolu** ve zamana göre eşleştirmek yetersiz olabilir. Dosya yeniden adlandırılırsa yolu değişir ama aynı nesne kalabilir. Eski yolu daha sonra başka bir dosya da kullanabilir.

Bu örnekte **dosya kimliği**, `(volume, file_id)` ikilisidir. `volume` birim kimliğini, `file_id` o birimdeki nesne referansını temsil eder. Aynı sayısal kimlik farklı birimde aynı dosyayı göstermez.

## Çalıştırma
```bash
python3 labs/37-file-identity-renames-and-timeline-provenance/identity_timeline.py
```
Yedi kontrol; ad değişimini, farklı birim çakışmasını ve eski yolun farklı nesneyle kullanılmasını gösterir.

## Sorular
Kopyalama ile yeniden adlandırmanın farkı ne? Dosya kimliği neden birimle beraber tutulmalı? Eşleşen kimlik, işlemi başlatan kişiyi kanıtlar mı?

## Sınırlar
Tüm kayıtlar hayalîdir. Gerçek NTFS referansları yeniden kullanılabilir; bu örnek aktör atfı ve nedensellik kanıtlamaz.
