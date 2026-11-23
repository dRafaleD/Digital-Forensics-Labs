# Gün 46 — Süreç Soy Ağacı, Kapsama Alanı ve Kanıt Yokluğu

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](coverage_demo.py)

## 45. günden devam
Önceki gün aynı logu taşıyan iki relay'in bağımsız kaynak olmadığını gördük. Bu kez **log kaynağının gerçekten kayıt topladığı zaman aralığı** önemli.

**Coverage (kapsama):** bir sensörün ilgili olayı gözlemleyebilecek durumda olması. **Absence of evidence:** kaydın bulunmaması; olayın kesinlikle yaşanmadığı anlamına gelmez. **Provenance:** kaydın gerçek kökeni.

Kaynak kapalıysa o kaynaktan log gelmemesi bir şey kanıtlamaz. İki bağımsız sensör aynı parent süreci raporlarsa `CORROBORATED_CONTEXT`, eksik kapsama varsa `LIMITED_COVERAGE`, hiç olumlu veri yoksa `NO_POSITIVE_EVIDENCE` sonucunu veriyoruz.

## Çalıştır
```bash
python3 labs/46-process-lineage-coverage-and-absence-of-evidence/coverage_demo.py
```

## Sorular
Kapalı sensörün sessizliği neden delil değildir? Bağımsız sensörler neden farklı kaynaklardan doğrulanmalı? Kanıt olmaması ile olayın olmadığının kanıtı arasındaki fark ne?

## Sınırlar
Gerçek Windows/Sysmon kaydı veya kişi bilgisi içermez.
