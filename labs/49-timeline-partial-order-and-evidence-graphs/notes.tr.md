# Gün 49 — Zaman Çizelgesi Kısmi Sıralama ve Kanıt Grafiği

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](partial_order.py)

48. günde belirsiz zaman damgalarını ikili olarak karşılaştırdık. Bugün yalnızca kesin zaman ilişkilerinden yönlü grafik oluşturuyoruz. A'nın en geç olası zamanı B'nin en erken olası zamanından küçükse A → B kenarı eklenir. Aralıklar kesişiyor veya sınırda temas ediyorsa sıralama uydurulmaz.

Örnek: A=[0,2], B=[1,4], C=[5,7], D=[7,9]. Dört kenar: A→C, A→D, B→C, B→D. A/B ve C/D belirsizdir. Girdi sırası grafiği değiştirmez.

**Alıştırma:** grafiği çiz, D'nin başlangıcı 8 olursa değişimi tahmin et, tüm aralıkları kapsayan bir olay ekle. Zaman sırası neden nedensellik kanıtı değildir? Beklenen: 9 partial-order checks passed. Tüm olaylar hayalîdir; aktör atfı yapılmaz.

## Çalıştır
```bash
python3 labs/49-timeline-partial-order-and-evidence-graphs/partial_order.py
```
