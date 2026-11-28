# Gün 52 — Delil Grafiği Kenar Kaynakları ve Çelişki Raporları

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](edge_review.py)

51. günde erişilebilirlik ve karşılaştırılamayan olayları inceledik. Bugün sıralama iddialarının kaynak etiketlerini saklayıp doğrudan ters yönlü kenarları raporluyoruz; kazanan kaynak seçmiyoruz. Aynı kaynağın tekrarları tekilleştirilir. Sekiz senaryoda çelişkiler, öz döngü ve bu sınırlı kontrolün bulmadığı üç düğümlü döngü bulunur. Son döngüyü çiz ve 50. günün döngü kontrolünü uygula. Kaynak etiketleri bağımsızlığı, NO_DIRECT_CONFLICT ise tüm grafiğin tutarlılığını kanıtlamaz. Veriler hayalîdir.

## Çalıştır
```bash
python3 labs/52-evidence-edge-provenance-and-conflict-reports/edge_review.py
```
