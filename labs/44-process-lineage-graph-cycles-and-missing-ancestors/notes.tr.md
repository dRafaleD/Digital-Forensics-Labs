# Gün 44 — Süreç Soy Ağacı, Döngüler ve Eksik Üst Süreçler

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lineage_graph.py)

## 43. günden devam
Önceki gün parent süreç GUID ve PID uyuşmazlıklarını kontrol ettik. Bugün birden fazla süreç ilişkisini **graf (graph)** olarak takip ediyoruz.

**Process lineage:** bir sürecin üst süreçlerden oluşan zinciri. **Ancestor:** zincirde daha yukarıdaki süreç. **Cycle:** bir bağlantının dönüp aynı noktaya gelmesi. **Collection gap:** bir olay kaydının elimizde olmaması.

Kod, çocuk süreçten başlayarak parent bağlantılarını izler. Eksik parent için `MISSING_ANCESTOR`, birden çok aynı GUID için `AMBIGUOUS_GUID`, zaman çelişkisi için `TIME_ORDER_CONFLICT`, kendi üzerine dönen zincir için `CYCLE` sonucu verir.

Zincir düzgün görünürse **CHAIN_CANDIDATE** olur. Yani *makul adaydır*, gerçek kişiyi veya kesin olay nedenini ispatlamaz.

## Çalıştırma
```bash
python3 labs/44-process-lineage-graph-cycles-and-missing-ancestors/lineage_graph.py
```

## Sorular
Eksik parent kaydı neden kesinlikle parent yok demek değildir? Aynı GUID tekrar kullanılırsa hangi belirsizlik oluşur? Süreç zinciri insan aktörünü kanıtlar mı?

## Sınırlar
Gerçek Windows, Sysmon veya süreç listesi incelenmez; tamamen sentetik veridir.
