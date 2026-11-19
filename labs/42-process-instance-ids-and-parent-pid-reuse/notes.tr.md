# Gün 42 — PID Yeniden Kullanımı ve Süreç Örneğini Ayırt Etme

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](parent_pid_demo.py)

## 41. günden devam
Önceki gün süreç başlatıcısını belirlerken **UNKNOWN** veya **AMBIGUOUS** demenin önemini gördük. Bugün yeni sorun: **PID (Process ID) numarası zaman içinde yeniden kullanılabilir**.

Örnekte PID 400 önce bir sürece ait, sonra başka bir süreç aynı numarayı alıyor. Yalnızca sayıya bakmak yanlış parent/child ilişkisi kurabilir.

**Process instance:** bir sürecin belirli çalıştırılma örneği. **Parent process:** başka bir süreci başlattığı kaydedilen üst süreç. **Candidate:** makul aday, kesin kanıt değil.

Model `(PID, oluşturulma zamanı)` ikilisini kullanır. Eksik veya yinelenen kayıtlarla belirsiz sonuç verir. Hatalı bir kaynak kendi içinde tutarlı görünebilir; bu yüzden gerçek loglarda bağımsız doğrulama gerekir.

## Çalıştır
```bash
python3 labs/42-process-instance-ids-and-parent-pid-reuse/parent_pid_demo.py
```

## Sorular
Aynı PID farklı zamanlarda niçin başka süreci gösterebilir? Parent PID neden tek başına yeterli değil? Eşleşen süreç kayıtları kişiyi kanıtlar mı?

## Sınırlar
Gerçek Sysmon, Windows Event Log veya sistem verisi okunmaz.
