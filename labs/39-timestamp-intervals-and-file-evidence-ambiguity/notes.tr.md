# Gün 39 — Zaman Aralıkları ve Dosya Kanıtı Belirsizliği

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](uncertain_timeline.py)

## 38. günden devam
Kopyalama ve yeniden adlandırma için dosya yolu, file ID ve hash değerlerini inceledik. Bu gün **zaman damgası belirsizliği** ekliyoruz: günlükte yazan saniye, olayın tam anı olmayabilir.

**Timestamp uncertainty:** saat kayması, toplama gecikmesi veya ölçüm hassasiyeti nedeniyle zamanın kesin bilinmemesi. `100 ± 2` ifadesi, gerçek zamanın 98 ile 102 arasında olabileceği anlamına gelir.

Kod iki ayrı soruyu yanıtlar:
- **İlişki:** aynı volume/file ID mi, aynı dosya yolu mu, yalnızca aynı içerik hash'i mi?
- **Sıra:** kaynak kesin olarak önce mi, gözlem kesin olarak önce mi, yoksa zaman aralıkları çakışıyor mu?

**SAME_RECORDED_ID**, kesin dosya kimliği demek değildir; gerçek sistemlerde sayısal file ID yeniden kullanılabilir. Aynı hash de dosyanın gerçekten kopyalandığını ispatlamaz.

## Çalıştırma
~~~bash
python3 labs/39-timestamp-intervals-and-file-evidence-ambiguity/uncertain_timeline.py
~~~

## Sorular
İki zaman aralığı çakışırsa hangi olayın önce olduğunu söyleyebilir miyiz? Toplama zamanı ile olay zamanı niçin farklıdır? Eşleşen hash niçin aktör atfı değildir?

## Sınırlar
Sadece hayalî olay kayıtları kullanılır; gerçek bir Windows adli incelemesi veya nedensellik kanıtı değildir.
