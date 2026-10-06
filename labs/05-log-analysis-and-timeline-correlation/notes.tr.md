# Gün 5 — Log Analizi, Timeline Correlation ve Event Reconstruction

[🇬🇧 English](notes.md) | [🇹🇷 Türkçe](notes.tr.md)

## Amaç

Birden fazla log kaynağını tek timeline içinde birleştirmeyi ve evidence'ın desteklediğinden daha fazlasını iddia etmeden event sequence çıkarmayı öğrenmek.

Bu gün; log structure, timestamp, timezone, normalization, clock skew, event correlation, request ID, missing log, hashing ve forensic reporting konularını birlikte işler.

## 1. Tek log tek bakış açısıdır

Authentication, web, system, firewall veya database logları aynı olayın farklı bölümlerini gösterebilir.

~~~text
auth log
web log
system log
   ↓
timestamp normalize
   ↓
timeline oluştur
   ↓
related event correlate et
   ↓
observation ile inference'ı ayır
~~~

Amaç sadece satırları sıralamak değil, her source'un neyi gerçekten kanıtlayabildiğini anlamaktır.

## 2. Observation vs inference

Log:

~~~text
LOGIN user=eren status=success
~~~

diyorsa güvenli ifade:

> Authentication log, eren account'u için successful login kaydı içeriyor.

Bu, fiziksel olarak klavyede kimin olduğunu tek başına kanıtlamaz.

## 3. Timestamp ve timezone

Lab ISO 8601 kullanır:

~~~text
2026-10-06T08:20:10+03:00
~~~

+03:00 UTC offset'tir.

Farklı timezone kullanan source'ları karşılaştırırken normalize et, ama original timestamp'i de koru.

Event table için:

- original time
- normalized time
- source
- event
- account
- request ID
- result
- notes

tutabilirsin.

## 4. Clock skew

İki sistemin saati farklı olabilir.

Bir host +2 dakika ilerideyse event order yanlış görünebilir.

İpuçları:

- NTP log
- known synchronization event
- request/response pair
- sürekli aynı offset

Timestamp'i sessizce düzeltme; düzeltmenin dayanağını document et.

## 5. Synthetic evidence oluştur

~~~bash
python3 create_log_evidence.py
~~~

Şunları üretir:

~~~text
evidence/auth.log
evidence/web.log
evidence/system.log
~~~

Analizden önce:

~~~bash
sha256sum evidence/*.log
sha256sum evidence/*.log > evidence_hashes.sha256
~~~

## 6. Önce source'ları ayrı incele

auth.log authentication event içerir.

web.log application request ve request ID içerir.

system.log service/file activity içerir.

Her source için sor:

- Ne logluyor?
- Neyi loglamıyor?
- Identity neyi temsil ediyor?
- Timestamp formatı nedir?

## 7. Timeline oluştur

~~~bash
python3 timeline.py
~~~

Script timestamp parse eder ve event'leri sıralar.

Örnek sequence:

~~~text
service start
login success
web request
download request
file creation
logout
service stop
~~~

Script sadece verilen timestamp'leri sıralar. Causation kanıtlamaz.

## 8. Correlation vs causation

Login sonrası request ve file creation görülmesi bu event'lerin yakın olduğunu gösterir.

Ama:

> Login file creation'a neden oldu.

sonucu otomatik çıkmaz.

Temporal proximity correlation'dır, causation proof değildir.

## 9. Request ID

Synthetic loglarda req-18 gibi ID var.

~~~text
web.log: request_id=req-18
        ↓
system.log: request_id=req-18
~~~

Bu, sadece timestamp proximity'den daha güçlü correlation sağlayabilir.

Yine scope ve semantics kontrol edilmelidir.

## 10. Missing log belirsizdir

Log entry yoksa:

- event olmadı
- source loglamıyor
- logging kapalıydı
- collection kaçırdı
- rotation oldu
- data silindi
- parser başarısız oldu

gibi birçok ihtimal vardır.

~~~text
no log entry != event hiç olmadı
~~~

## 11. Duplicate event

Tekrarlanan kayıt:

- retry
- reconnect
- duplicate collection
- aynı action'ın birden fazla layer'da loglanması

olabilir.

Line count = human action count değildir.

## 12. Identity caution

Username, sistemin kaydettiği account/context'tir.

> Account eren /download request gönderdi.

ifadesi:

> Eren fiziksel olarak kesin bu işlemi yaptı.

ifadesinden daha savunulabilirdir.

## 13. Hash ve preserve

Analiz sonrası:

~~~bash
sha256sum -c evidence_hashes.sha256
~~~

Hash aynıysa source loglar baseline ile aynı byte'lara sahiptir.

## 14. Mini challenge — event table

En az altı satır oluştur:

~~~text
Original Time
Normalized Time
Source
Event
Account
Request ID
Result
Observation
Inference
~~~

Evidence desteklemiyorsa alanı boş bırak. Tahminle doldurma.

## 15. Mini challenge — clock skew

Bir logun working copy'sindeki timestamp'lere +2 dakika ekle.

Sonra timeline'ı tekrar oluştur.

Cevapla:

- Hangi sequence yanıltıcı oldu?
- Offset nasıl tespit edilir?
- Correction nasıl document edilir?
- Original evidence neden değiştirilmemeli?

## 16. Mini challenge — case summary

Sadece synthetic evidence kullanarak kısa summary yaz:

1. direct observations,
2. supported inference,
3. limitations,
4. source hashes.

## 17. Reporting language

Doğrudan gözlem:

> web.log, 08:21:32+03:00'da /download?id=17 için GET request kaydediyor ve request_id=req-18.

Supported inference:

> Aynı request ID'ye sahip system.log kaydı kısa süre sonra report17.txt creation gösteriyor.

Unsupported:

> Account owner bilinçli şekilde report oluşturup indirdi.

Son cümle mevcut evidence'ın ötesine geçer.

## 18. Workflow

~~~text
preserve
  ↓
hash
  ↓
source'ları ayrı anla
  ↓
timestamp parse
  ↓
normalize
  ↓
timeline
  ↓
ID/event correlate
  ↓
observation vs inference
  ↓
limitations report et
~~~

## Alıştırmalar

1. Synthetic logları üret.
2. Hash al.
3. Source'ları ayrı incele.
4. Timeline script çalıştır.
5. Altı satırlık event table yap.
6. req-18'i source'lar arasında correlate et.
7. Üç direct observation yaz.
8. İki supported inference yaz.
9. Logların kanıtlayamadığı iki şeyi yaz.
10. Clock-skew challenge yap.
11. Analiz sonrası hash doğrula.
12. Kısa case summary yaz.

## Sorular

1. Neden birden fazla log source birleştirilir?
2. Original timestamp neden korunur?
3. Timezone normalization ne çözer?
4. Clock skew nedir?
5. Correlation neden causation değildir?
6. Request ID ne işe yarar?
7. Missing log neden belirsizdir?
8. Username neden fiziksel identity kanıtı değildir?
9. Hash log analysis'e ne katar?
10. Observation ve inference neden ayrılmalıdır?

## Ana çıkarım

~~~text
multiple partial sources
        ↓
time normalization
        ↓
correlation
        ↓
careful reasoning
        ↓
evidence-based reporting
~~~

Timeline analysis sadece timestamp sıralamak değildir; source scope ve limitation anlamaktır.
