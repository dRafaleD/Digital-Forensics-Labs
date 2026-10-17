# Gün 10 — Çok Kaynaklı İz Korelasyonu ve Güven Düzeyi Raporlama

[English](notes.md) · [Türkçe](notes.tr.md)

## Hedef
Çok Kaynaklı İz Korelasyonu ve Güven Düzeyi Raporlama konusunu tamamen yerel ve zararsız örneklerle öğrenmek. Gözlemlenen bulguyu yorumdan ayırmak ve kesin olmayan sonuçları abartmamak.

## Temel kavramlar
1. **event timestamps and UTC normalization:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.
2. **joining across request IDs:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.
3. **source integrity hashes:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.
4. **positive versus missing evidence:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.
5. **corroboration versus causation:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.
6. **confidence and uncertainty statements:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.

## Uygulama
Lab klasöründe `correlate.py` dosyasını inceleyin ve şu komutları sırasıyla uygulayın:

```bash
python3 correlate.py
```

**Beklenen sonuç:** Events are normalized into UTC and sorted; only the first two share a correlation ID.

## Analiz defteri
Kullandığınız araç sürümünü, komutu, girdiyi, gördüğünüz çıktıyı, beklenmeyen olayları ve olası açıklamaları kaydedin. Ölçülen veri ile çıkarımı ayrı başlıklar altında yazın.

## Uygulama görevleri
1. Orijinal örneği çalıştırıp çıktıyı kaydedin.
2. Zararsız bir girdiyi değiştirerek sonucu önceden tahmin edin.
3. Bir negatif test ekleyin ve gerçekten hangi kontrolün başarısız olduğunu belirleyin.
4. Başlangıç dosyasına dönüp regresyon testi yapın.
5. İki olası yanlış pozitif açıklaması üretin.
6. Sonucu doğrulayacak bağımsız bir kanıt kaynağı önerin.
7. Belirsizlikleri açıkça yazan kısa bir rapor hazırlayın.

## Tekrar soruları
1. event timestamps and UTC normalization nedir, ne işe yarar, neyi garanti etmez?
2. joining across request IDs nedir, ne işe yarar, neyi garanti etmez?
3. source integrity hashes nedir, ne işe yarar, neyi garanti etmez?
4. positive versus missing evidence nedir, ne işe yarar, neyi garanti etmez?
5. corroboration versus causation nedir, ne işe yarar, neyi garanti etmez?
6. confidence and uncertainty statements nedir, ne işe yarar, neyi garanti etmez?
7. Sonucun güvenilirliğini nasıl artırırsınız?
8. Hangi kontrolü otomatik regresyon testine dönüştürürsünüz?

## Kapsam
Bu lab yalnızca izinli, sentetik veriler içindir. Tek bir bulguyu kesin saldırı kanıtı saymayın.
