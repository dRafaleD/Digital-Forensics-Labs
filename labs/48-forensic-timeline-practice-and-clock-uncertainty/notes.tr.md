# Gün 48 — Uygulama Günü: Adli Zaman Çizelgesi ve Saat Belirsizliği

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](timeline.py)

Hayalî indirme kaydı 10:00:00 UTC ve ±2 saniye belirsizlik içeriyor. Diğer zamanları UTC'ye çevir ve olası zaman aralıklarını karşılaştır. Bir olayın en geç zamanı diğerinin en erken zamanından önceyse BEFORE; aralıklar kesişiyorsa ORDER_UNCERTAIN.

| Diğer gözlem | İndirme kaydının ilişkisi |
|---|---|
| 10:00:10 UTC | BEFORE |
| 09:59:50 UTC | AFTER |
| 13:00:00 +03:00 | ORDER_UNCERTAIN |
| 10:00:04 UTC ±2 sn | ORDER_UNCERTAIN |
| 10:00:05 UTC ±2 sn | BEFORE |
| Saat dilimi yok | INVALID_TIME |

**Alıştırmalar:** 12 sonucu tahmin et, üç saati elle UTC'ye çevir, belirsizliği 5 saniyeye çıkarıp sınır örneklerini yeniden değerlendir, belirsizliği belirten kısa zaman çizelgesi yaz. Zaman sırasından eylemi yapan kişiyi çıkarma.

Beklenen son satır: 12/12 timeline cases passed. Gerçek log veya sistem erişimi yoktur.

## Çalıştır
```bash
python3 labs/48-forensic-timeline-practice-and-clock-uncertainty/timeline.py
```
