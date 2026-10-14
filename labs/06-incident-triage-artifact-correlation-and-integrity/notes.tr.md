# Gün 6 — Incident Triage, Artifact Correlation ve Delil Bütünlüğü

[English](notes.md) · [Türkçe](notes.tr.md)

**Amaç:** Gün 5 log timeline bilgisini process, network ve file artifact'larını karşılaştıracak şekilde genişletmek.

**Kapsam:** Bu lab gerçek host taramaz. Synthetic JSONL artifact'lar ve SHA-256 manifest'i üretir.

## 1. Triage ve kapsam

Dijital adli triage ilk incelemedir: hangi artifact'lar var, delil nasıl korunur, hangi ek collection gerekli sorularını cevaplar. Triage sonucu kesin incident kararı değildir.

## 2. Birden fazla delil kaynağı

Process log PID/PPID ve process name, network log connection, file log dosya olayı gösterebilir. Her kaynak eksiktir. Process name görmen onu hangi insanın çalıştırdığını kanıtlamaz.

## 3. Hash ve bütünlük

SHA-256 dosyanın byte düzeyinde baseline'ını tutar. Analizden önce doğrula; uyuşmazlıkta dur. Manifest expected digest'leri içerir. Hash eşleşmesi baseline'a göre bütünlüğü destekler ama collector'ın dürüstlüğünü veya log'un gerçekliğini kanıtlamaz.

## 4. Chain of custody

Gerçek vakada acquisition yöntemi, collector, devir teslim, zaman, kullanılan tool ve hash kayıtları tutulur. Bu lab delili sentetik üretir; gerçek chain of custody kanıtı değildir. Her transformation ayrı belgelenmelidir.

## 5. Zaman normalizasyonu

Farklı timezone içeren kayıtları ham string sırasıyla karşılaştırmak yanıltabilir. Original timestamp'i sakla, timezone-aware UTC'ye normalize et. Clock skew, precision ve missing event ihtimalini hesaba kat.

## 6. PID correlation ve reuse

PID belli zaman ve host bağlamında process/network/file kayıtlarını bağlayabilir. PID başka zaman yeniden kullanılabilir. Start time, host ID, executable ve session gibi ek alanlar olmadan kesin correlation yapma.

## 7. Network delil sınırı

Connection log gözlemciye göre IP/port/protocol bildirir; tek başına exfiltration veya niyet kanıtlamaz. Sentetik hedef 192.0.2.55 documentation IP'sidir ve bağlantı kurulmaz. Payload delili yoktur.

## 8. File metadata ve nedensellik

Dosya oluşturma kaydı ile yakın zamandaki process connection anlamlı olabilir fakat nedensellik otomatik değildir. Yetkili ortamda file hash, EDR, handle veya filesystem journal gibi ek delillere bakılabilir.

## 9. Güven ve raporlama

Bulgu için source observation, time, destekleyen delil, inference, limitation ve confidence yaz. 'Log X kaydediyor' ile 'kişi kesin Y yaptı' farklı cümlelerdir. Confidence kaynak kalitesi ve kapsamına dayanmalı.

## 10. Güvenlik ve mahremiyet

Canlı process/network verisini yalnız izinli sistemlerden topla. Loglar özel isim veya ID içerebilir. Kopyalarda çalış ve gerçek delili public repoya yükleme. Bu lab host'u taramaz; sahte metadata üretir.

## Yerel uygulama

Lab klasöründe:

```bash
python3 generate_case.py
python3 analyze_case.py
```

`evidence/` altında şu JSONL dosyaları oluşur:
- `processes.jsonl`: PID 4102, child 4103, exit.
- `connections.jsonl`: PID 4103 için sentetik bağlantı/close.
- `files.jsonl`: dosya create ve read kayıtları.
- `manifest.sha256.json`: üç dosyanın SHA-256 değerleri.

Analyzer önce **bütün hash'leri doğrular**. Uyuşmazlık varsa devam etmez. Sonra olayları UTC'ye çevirip PID üzerinden context ekler. Ağ bağlantısı, kimlik doğrulama veya gerçek dosya toplama yapmaz.

### Delil bütünlüğü testi

Bir çalışma kopyasında `evidence/files.jsonl` içine bir boşluk ekle ve `python3 analyze_case.py` çalıştır. Hash mismatch beklenir. `python3 generate_case.py` ile sentetik baseline'ı yeniden üret. Gerçek olayda kanıt dosyasını böyle overwrite etmek doğru değildir; bu yalnız üretilebilir eğitim fixture'ı.

### Mini challenge

1. PID 4103'ün tüm olaylarını timeline olarak özetle.
2. Start/exit zamanlarını kullanıp PID reuse riskini açıkla.
3. Dosya oluşturmanın ağ bağlantısından kaynaklandığını mevcut verinin niye kanıtlayamadığını yaz.
4. Bir evidence worksheet oluştur: source, hash, timezone, observation, inference, limitation.

### Alıştırmalar

1. Fixture üret.
2. Hash manifest'ini incele.
3. Hash verify et.
4. Timeline çıktısı al.
5. UTC zamanlarını yorumla.
6. Parent/child ilişkisini çiz.
7. PID bağlamını açıkla.
8. Connection tuple bul.
9. File event sırasını incele.
10. Integrity failure simüle et.
11. Observation/inference ayır.
12. 8 cümlelik triage report yaz.

### Sorular

1. Forensic triage nedir?
2. Acquisition ile analysis farkı?
3. Hash neyi destekler?
4. Hash neyi kanıtlamaz?
5. Chain of custody nedir?
6. Timezone neden gerekli?
7. Clock skew ne yapar?
8. PID reuse nedir?
9. Process name identity kanıtı mı?
10. Connection exfiltration kanıtı mı?
11. Timestamp correlation causation mıdır?
12. Evidence scope ne demek?
13. Original evidence neden korunur?
14. Manifest mismatch olursa ne yapılır?
15. Triage raporuna hangi limitation yazılır?

**Ana çıkarım:** Delil korunur, hash doğrulanır, farklı kaynaklar dikkatli ilişkilendirilir ve gözlem ile çıkarım açıkça ayrılır.
