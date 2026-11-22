# Gün 45 — Süreç Soy Ağacı Kanıtının Kaynağı ve Bağımsızlığı

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](lineage_provenance_demo.py)

## 44. günden devam
Bir süreç soy ağacında eksik parent, döngü veya zaman çelişkisi bulunabilir. Bugün aynı iddiayı destekleyen iki logun gerçekten **iki bağımsız kanıt** olup olmadığını araştırıyoruz.

**Provenance:** delilin hangi kaynaktan geldiği. **Relay:** gelen logu başka sisteme ileten aracı. **Corroboration:** ayrı kaynaktan gelen kanıtların aynı hipotezi desteklemesi.

`agent-a` kaydının `relay-a` üzerinden gelmesi iki ayrı kanıt değildir. Uygulamanın güvenilir kolektör eşlemesi ikisini **aynı köken** olarak sayar. Bağımsız `agent-b` de aynı parent'ı gösterirse `CORROBORATED_CONTEXT`; iki kaynak çelişirse `CROSS_SOURCE_CONFLICT` döner.

## Çalıştır
```bash
python3 labs/45-process-lineage-provenance-and-independent-sources/lineage_provenance_demo.py
```

## Sorular
İki kez iletilen log neden iki bağımsız tanık değildir? Kaynağı logun kendi içindeki metinden almak riskli mi? İki sensörün uzlaşması gerçek aktörü kanıtlar mı?

## Sınır
Sentetik süreç kayıtlarıdır; gerçek Windows verisi veya kişi atfı yoktur.
