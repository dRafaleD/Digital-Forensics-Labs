# Gün 41 — Çalıştırma Başlatıcısı Hipotezleri ve Kararsız Kalabilme

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](initiator_demo.py)

## 40. günden devam
İki log aynı dosya ve zamanda eşleşse bile **işlemi kimin başlattığı** kesinleşmez. Bu gün kanıt eksikse sonuç uydurmak yerine **UNKNOWN** veya **AMBIGUOUS** raporlamayı öğreniyoruz.

**Initiator (başlatıcı):** sürecin çalışmasına neden olan etken. **Interactive session:** bir kullanıcı oturumuyla ilişkili bağlam; gerçek bir insanın tıkladığını kanıtlamaz. **Scheduled task:** zamanlayıcı bağlamı; görevi kimin kurduğunu göstermez. **Abstention:** yeterli kanıt yoksa sınıflandırmadan kaçınmak.

Kod sekiz hayalî olayı inceler. Tek bir gösterge varsa yalnızca bağlamı raporlar; çelişkili göstergeler varsa `AMBIGUOUS`, log eksikse `UNKNOWN` der. **Süreç bağlamı ile gerçek aktör kimliği farklıdır.**

## Çalıştırma
~~~bash
python3 labs/41-execution-initiator-hypotheses-and-abstention/initiator_demo.py
~~~

## Sorular
Interactive session neden insan eyleminin ispatı değildir? Zamanlanmış görevi kimin yarattığı nasıl araştırılır? Çelişkili loglarda neden kesin sınıf vermemeliyiz?

## Sınırlar
Gerçek Windows Event Log, Sysmon veya dosya sistemi analizi yapılmaz; yalnızca sentetik veri kullanılır.
