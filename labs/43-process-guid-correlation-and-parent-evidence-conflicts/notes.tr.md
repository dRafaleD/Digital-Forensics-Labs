# Gün 43 — Process GUID ve Parent Süreç Kanıt Çelişkileri

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](process_guid_demo.py)

## 42. günden devam
Önceki gün **PID** numarasının tekrar kullanılabileceğini gördük. Bu gün süreçleri ayırt etmek için loglarda yer alabilen **Process GUID** bilgisini de değerlendiriyoruz.

**GUID:** bir süreç örneğini ayırmaya yardımcı olan kayıt kimliği. **Parent PID:** üst sürecin sayısal kimliği. **Conflicting evidence:** iki delilin aynı şey hakkında uyuşmaması.

Model, iddia edilen parent GUID'ini buluyor; PID ve başlama zamanını kontrol ediyor. Birbiriyle çelişen bilgiler için `CONFLICTING_EVIDENCE`, birden fazla aynı GUID kaydı varsa `AMBIGUOUS`, veri eksikse `UNKNOWN` veriyor. Eşleşme varsa bile yalnızca `PARENT_CANDIDATE`.

## Çalıştırma
```bash
python3 labs/43-process-guid-correlation-and-parent-evidence-conflicts/process_guid_demo.py
```

## Sorular
GUID neden tek başına kesin delil değil? Parent sürecin child'dan önce başlaması neden beklenir? Parent ilişkisi gerçek insanı belirler mi?

## Sınırlar
Gerçek Windows olayları okunmaz. Veriler tamamen sentetiktir ve aktör atfı yapılmaz.
