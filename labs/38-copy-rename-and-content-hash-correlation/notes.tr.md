# Gün 38 — Kopyalama, Yeniden Adlandırma ve Dosya Hash'i Korelasyonu

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](identity_hash_demo.py)

## 37. günden devam
Dosya yolu ile kimliğinin aynı olmadığını öğrendik. Şimdi **SHA-256 içerik özeti** de ekliyoruz. İki dosyanın aynı içeriğe sahip olması, mutlaka birinin diğerinden kopyalandığı anlamına gelmez.

**SAME_IDENTITY:** aynı disk birimi ve file ID; yol değişebilir.
**CONTENT_MATCH_ONLY:** dosya kimliği ayrı ama içerik özeti aynı; kopyalama ihtimali var, kanıt değil.
**PATH_REUSED:** aynı yol artık başka nesneye ait.
**TIME_REVERSED:** gözlenen olay, bu oyuncak zaman çizelgesindeki kaynak olaydan önce.
**NO_MATCH:** diğer ilişkiler bulunamadı.

Bu ayrımlar, tek başına aktör veya sebep-sonuç ilişkisi kurmaz. Gerçek adli incelemede NTFS kayıtları, zaman kaynakları, dosya referanslarının tekrar kullanımı ve delil bütünlüğü beraber değerlendirilir.

## Çalıştırma
~~~bash
python3 labs/38-copy-rename-and-content-hash-correlation/identity_hash_demo.py
~~~

## Alıştırmalar
Aynı hash neden kopyalama ispatı değildir? Dosya adı yeniden kullanılırsa ne olur? Dosya yolu, ID ve hash birlikte neden önemlidir?

## Sınırlar
Tamamen sentetik Python kayıtlarıdır; gerçek dosya veya disk incelenmez.
