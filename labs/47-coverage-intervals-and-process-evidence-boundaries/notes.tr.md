# Gün 47 — Kapsama Aralıkları ve Süreç Kanıtı Sınırları

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](coverage_intervals.py)

46. günde sensörün kapsama durumunu tek bir boolean değerle ifade ettik. Bugün [başlangıç,bitiş) aralıklarını kullanıyoruz. Bitişik veya örtüşen aralıklar inceleme penceresini tamamen kapsayabilir; bir birimlik boşluk bile PARTIAL_COVERAGE sonucunu doğurur. Hiç kayıt olmaması olayın yaşanmadığını kanıtlamaz.

**Sorular:** Toplama zaman aralığı neden önemlidir? Saat kayması aralıkları nasıl etkiler? Eksik kapsama neden temiz sistem demek değildir?

Yalnızca hayalî aralıklar ve parent etiketleri kullanılır; gerçek log veya host erişimi yoktur.

## Çalıştır
```bash
python3 labs/47-coverage-intervals-and-process-evidence-boundaries/coverage_intervals.py
```
