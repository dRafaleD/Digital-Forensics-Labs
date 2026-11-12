# Gün 36 — İndirme ve Çalıştırma Olaylarının İlişkilendirilmesi

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](attribution_demo.py)

## 35. günden devam
Önceki laboratuvarda tarayıcı indirmesi ile `Zone.Identifier` izini karşılaştırdık. Şimdi **süreç başlatma (process execution)** kayıtlarını da ekliyoruz. Yol ve zamanın eşleşmesi, olayların ilişkili olabileceğini gösterir; **bir kişinin veya işlemin gerçekten başlatıcı olduğunu kanıtlamaz**.

## Üç veri kaynağı
- **Browser download history:** tarayıcının kaydettiği indirme bilgisi.
- **Zone.Identifier:** dosya kaynağına ilişkin olası ek NTFS veri akışı; her dosyada bulunmayabilir.
- **Process telemetry:** süreç başlatma zamanı ve raporlanan dosya yolu.

**Correlation (korelasyon):** kayıtların ortak özelliklerle eşleşmesi. **Causation (nedensellik):** bir olayın diğerini gerçekten tetiklemesi. İkisi aynı şey değildir.

Kodda UTC zaman damgaları ve örnek olarak 5 saniyelik eşleşme penceresi vardır. İndirme kaydı, bu basitleştirilmiş akışta çalıştırma kaydından sonra olamaz.

## Çıktılar
- **CORRELATED:** bir indirme ve bir Zone kaydı eşleşiyor.
- **AMBIGUOUS:** aynı dosya için iki indirme adayı var; hangisinin ilgili olduğu belirsiz.
- **INSUFFICIENT:** yeterli eşleşen kayıt yok.

Bu etiketler **aktör atfı değildir**. Yol değişiklikleri, saat kayması, eksik loglar ve dosya kopyaları gerçek olaylarda ayrıca incelenmelidir.

## Uygulama
~~~bash
python3 labs/36-download-execution-correlation-and-attribution-limits/attribution_demo.py
~~~

## Sorular
1. Aynı yolun görünmesi neden kullanıcı kimliğini kanıtlamaz?
2. Saat kayması korelasyonu nasıl etkiler?
3. Aynı dosyaya iki indirme kaydı varsa ne raporlanmalı?
4. Parent PID, komut satırı ve hash hangi ek sorulara yanıt verebilir?
5. Kanıt eksikliğini raporda nasıl belirtirsin?

## Güvenlik sınırı
Yalnızca sentetik Python listeleri kullanılıyor; gerçek sistemler incelenmiyor ve sebep-sonuç ilişkisi iddia edilmiyor.
