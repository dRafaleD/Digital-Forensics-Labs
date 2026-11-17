# Gün 40 — Zaman Çizelgesinde Kanıt Kökeni ve Bağımsız Doğrulama

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](corroboration_demo.py)

## 39. günden devam
Bir olayın zamanı tek bir nokta yerine **belirsizlik aralığı** olabilir. Ancak iki kayıt zaman ve dosya kimliği açısından eşleşse bile aynı kaynaktan kopyalanmış olabilir.

**Provenance (kanıt kökeni):** kaydın asıl üretildiği kaynak. **Collector/relay:** kaydı alan veya ileten sistem. **Corroboration:** başka bir gözlemin mevcut bulguyu desteklemesi. Bir logun iki toplayıcıya gitmesi iki bağımsız delil sayılmaz.

Kod, `volume + file_id` çiftini ve belirsizlikli zaman aralığını kontrol eder. Ardından eşleşen kayıtların benzersiz **producer** değerlerini sayar. Farklı üretici adları gerçek bağımsızlığı veya başlatıcı kimliğini kesin kanıtlamaz.

## Çalıştırma
~~~bash
python3 labs/40-timeline-provenance-and-independent-corroboration/corroboration_demo.py
~~~

## Sorular
Collector ve producer farkı ne? Dosya kimliği neden disk birimiyle birlikte tutulmalı? Aynı olay farklı yerlerde tutulursa kanıt sayısı nasıl şişer? Kayıt eşleşmesi aktör atfı yapar mı?

## Sınır
Gerçek sistem veya NTFS kaydı okunmaz; tamamen sentetik delil karşılaştırmasıdır.
