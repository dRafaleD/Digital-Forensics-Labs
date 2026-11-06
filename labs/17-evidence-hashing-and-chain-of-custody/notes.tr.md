# Gün 17 — Delil Hash'leme, Muhafaza Zinciri ve Bütünlük Denetimi

[English](notes.md) · [Türkçe](notes.tr.md)

## Amaç
Zararsız yerel dosyalar için **SHA-256 delil manifestosu** oluşturmak ve dosya değişince hash değerinin nasıl farklılaştığını görmek. Bütünlük, özgünlük ve **delil muhafaza zinciri (chain of custody)** kavramlarını ayırt etmek.

## Temel bilgiler
- **Hash**, dosyanın baytlarının değişip değişmediğini test etmeye yardım eder; dosyayı kimin oluşturduğunu kanıtlamaz.
- **Muhafaza zinciri**, delilin ne zaman, kim tarafından, nasıl toplandığını ve kime aktarıldığını kaydeder.
- Orijinal konum, zaman dilimi, araç sürümü, işlem sahibi ve saklama koşulları ayrıca belgelenmelidir.
- Manifestonun da bütünlüğü korunmalıdır. Hem delil hem manifesto değiştirilirse doğrulama aldatılabilir.
- Dosya zaman damgaları değiştirilebilir; tek başlarına aktör atfına yetmez.

## Uygulama
```bash
python3 evidence_manifest_demo.py
```
Program geçici klasörde iki sentetik metin oluşturur, hash'lerini kaydeder ve birini değiştirerek uyuşmazlığı gösterir.

## Görevler
1. Hash eşleşmesi neden dosyanın özgün olduğunu kesin kanıtlamaz?
2. Gerçek delil kayıt defterinde bulunması gereken alanları listele.
3. Değişiklikten önce/sonra SHA-256 çıktılarını karşılaştır.
4. Manifesto da değiştirilebiliyorsa risk nedir?
5. Bağımsız bir doğrulama yöntemi öner.

## Güvenlik
Gerçek delile müdahale edilmez; hukuki geçerlilik iddiası yoktur.
