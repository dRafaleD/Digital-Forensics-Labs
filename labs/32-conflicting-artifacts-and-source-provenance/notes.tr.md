# Gün 32 — Çelişkili Adli İzler ve Kaynak Kökeni

[English](notes.md) · [Türkçe](notes.tr.md) · [Çevrimdışı uygulama](conflicts_demo.py)

## Amaç
Dijital incelemede NTFS metadata, sistem logları ve uygulama kayıtları aynı olaya ilişkin **farklı bilgiler** içerebilir. Bu çelişkileri görmezden gelmek veya tek bir kayda göre kesin atıf yapmak hatalı sonuca yol açabilir.

## Gözlem, rapor ve çıkarım farklı şeylerdir
Her kaydın **kaynak kimliği**, özgün zaman damgası, toplama zamanı ve kaydedilmiş alanları korunmalıdır. İki kaynak farklı başlatıcı bildiriyorsa bu bir **uyuşmazlık bulgusudur**. Kayıtlardan birinin kesin sahte olduğu veya belirli aktörün zararlı olduğu sonucuna doğrudan gidilemez.

## Sentetik senaryo
`artifact-01` için üç zararsız kayıt vardır:
- Dosya olayı kaydı başlatıcıyı `automation` olarak bildiriyor.
- Uygulama denetim kaydı `user` diyor.
- Depolama kaydı başlatıcı belirtmiyor.

Aynı dosya kimliği kayıtları bir araya getirmeye yarar, ancak **kimin başlattığını tek başına çözmez**. Kod bütün kayıtları koruyarak sonuç alanını `inconclusive` bırakır.

## Uygulama
```bash
python3 conflicts_demo.py
```

`report` sözlüğünde kanıt kimlikleri, bildirilen başlatıcılar ve belirsizlik açıklaması bulunur. Gerçek disk veya loglar okunmaz.

## Görevler
1. Başlatıcılardan birini `unknown` yap; belirsizlik gerçekten çözüldü mü?
2. Korelasyondan önce kaynak kökeni ve zaman kayması neden araştırılır?
3. Dördüncü bir kaydı özgün kayıtları değiştirmeden ekle.
4. Aktör atfını güçlendirecek **bağımsız** delil kaynağı öner.
5. Raporunda **gözlenen**, **kaynağın bildirdiği**, **yorumlanan** ve **çözülemeyen** alanları ayır.

## Sınırlamalar
Sentetik kayıtlar gerçek NTFS/Sysmon/Windows Event Log ayrıştırması değildir; atıf doğruluğu veya F1 ölçümü içermez. Gerçek incelemede delil koruma ve edinim zinciri ayrıca gereklidir.
