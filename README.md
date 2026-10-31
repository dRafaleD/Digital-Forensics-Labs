# Digital-Forensics-Labs

[🇬🇧 English](#english) | [🇹🇷 Türkçe](#türkçe)

# English

A beginner-friendly, hands-on digital forensics learning journal.

The goal is to learn how digital evidence should be preserved, verified, examined, and documented before moving into deeper disk, filesystem, memory, network, and artifact analysis.

## Labs

- [Day 1 — Digital Evidence, Integrity and Hashing](labs/01-evidence-integrity-and-hashing/notes.md)
- [Day 2 — Metadata, Timestamps and Timeline Basics](labs/02-metadata-timestamps-and-timeline/notes.md)
- [Day 3 — Filesystem and Disk Image Fundamentals](labs/03-filesystem-and-disk-image-fundamentals/notes.md)
- [Day 4 — Deleted Files, Filesystem Metadata and File Carving Foundations](labs/04-deleted-files-and-file-carving/notes.md)
- [Day 5 — Log Analysis, Timeline Correlation and Event Reconstruction](labs/05-log-analysis-and-timeline-correlation/notes.md)
- [Day 6 — Incident Triage, Artifact Correlation and Evidence Integrity](labs/06-incident-triage-artifact-correlation-and-integrity/notes.md)
- [Day 7 — Browser Artifacts, SQLite History and Timeline Reconstruction](labs/07-browser-artifacts-sqlite-and-timeline/notes.md)
- [Day 8 — Chain of Custody, Evidence Manifests and Hash Verification](labs/08-chain-of-custody-and-evidence-manifests/notes.md)

- [Day 9 — Linux Authentication Logs and Timeline Reconstruction](labs/09-linux-auth-logs-and-login-timeline/notes.md)

- [Day 10 — Multi-Source Artifact Correlation and Confidence Reporting](labs/10-10-artifact-correlation-and-confidence-reporting/notes.md)

- [Day 11 — File Metadata, MAC Times and Timeline Uncertainty](labs/11-file-metadata-mactime-and-timeline-uncertainty/notes.md)

- [Day 12 — Evidence Manifests, Integrity Checking and Audit Limits](labs/12-evidence-manifest-and-verification/notes.md)

- [Day 13 — Removable Device Artifacts and Timeline Correlation](labs/13-synthetic-usb-artifacts-and-device-timeline/notes.md)

- [Day 14 — Evidence Working Copies, Hash Checks and Change Detection](labs/14-evidence-copy-and-hash-verification/notes.md)

- [Day 15 — Evidence Timelines, Time Zones and Correlation Confidence](labs/15-evidence-timeline-and-timezone-normalization/notes.md)

## Learning path

Future labs will gradually cover:

- evidence handling and acquisition concepts
- cryptographic hashing and verification
- metadata and timestamps
- filesystems and disk images
- deleted files and file carving
- timeline analysis
- Linux and Windows artifacts
- memory forensics
- network evidence and PCAP analysis
- log correlation
- forensic reporting

## Lab philosophy

The repository uses small, harmless, reproducible exercises. The emphasis is on preserving evidence, documenting actions, and understanding what each tool proves instead of only memorizing commands.

## Safety and ethics

Work only with files, images, systems, and captures that you own or are explicitly authorized to examine. Preserve originals whenever possible and perform experiments on copies.

# Türkçe

Temelden başlayan, uygulamalı bir dijital adli bilişim öğrenme günlüğü.

Amaç; disk, dosya sistemi, bellek, ağ ve artifact analizine geçmeden önce dijital delilin nasıl korunacağını, bütünlüğünün nasıl doğrulanacağını, nasıl inceleneceğini ve işlemlerin nasıl kayıt altına alınacağını öğrenmektir.

## Lab'ler

- [Gün 1 — Dijital Delil, Bütünlük ve Hashing](labs/01-evidence-integrity-and-hashing/notes.tr.md)
- [Gün 2 — Metadata, Timestamp ve Timeline Temelleri](labs/02-metadata-timestamps-and-timeline/notes.tr.md)
- [Gün 3 — Filesystem ve Disk Image Temelleri](labs/03-filesystem-and-disk-image-fundamentals/notes.tr.md)
- [Gün 4 — Silinen Dosyalar, Filesystem Metadata ve File Carving Temelleri](labs/04-deleted-files-and-file-carving/notes.tr.md)
- [Gün 5 — Log Analizi, Timeline Correlation ve Event Reconstruction](labs/05-log-analysis-and-timeline-correlation/notes.tr.md)
- [Gün 6 — Incident Triage, Artifact Correlation ve Delil Bütünlüğü](labs/06-incident-triage-artifact-correlation-and-integrity/notes.tr.md)
- [Gün 7 — Tarayıcı İzleri, SQLite Geçmişi ve Zaman Çizelgesi](labs/07-browser-artifacts-sqlite-and-timeline/notes.tr.md)
- [Gün 8 — Muhafaza Zinciri, Delil Manifestleri ve Hash Doğrulama](labs/08-chain-of-custody-and-evidence-manifests/notes.tr.md)

- [Gün 9 — Linux Kimlik Doğrulama Kayıtları ve Zaman Çizelgesi](labs/09-linux-auth-logs-and-login-timeline/notes.tr.md)

- [Gün 10 — Çok Kaynaklı İz Korelasyonu ve Güven Düzeyi Raporlama](labs/10-10-artifact-correlation-and-confidence-reporting/notes.tr.md)

- [Gün 11 — Dosya Metadata, MAC Zamanları ve Zaman Çizelgesi Belirsizliği](labs/11-file-metadata-mactime-and-timeline-uncertainty/notes.tr.md)

- [Gün 12 — Delil Manifesti, Bütünlük Kontrolü ve Denetim Sınırları](labs/12-evidence-manifest-and-verification/notes.tr.md)

- [Gün 13 — Çıkarılabilir Aygıt İzleri ve Zaman Çizelgesi Korelasyonu](labs/13-synthetic-usb-artifacts-and-device-timeline/notes.tr.md)

- [Gün 14 — Delil Çalışma Kopyaları, Hash Kontrolü ve Değişiklik Tespiti](labs/14-evidence-copy-and-hash-verification/notes.tr.md)

- [Gün 15 — Delil Zaman Çizelgeleri, Saat Dilimleri ve Korelasyon Güveni](labs/15-evidence-timeline-and-timezone-normalization/notes.tr.md)

## Öğrenme yolu

İlerleyen lab'lerde adım adım şu konular işlenecektir:

- evidence handling ve acquisition kavramları
- cryptographic hashing ve doğrulama
- metadata ve timestamp'ler
- filesystem ve disk image'ları
- deleted file ve file carving
- timeline analysis
- Linux ve Windows artifact'ları
- memory forensics
- network evidence ve PCAP analizi
- log correlation
- forensic reporting

## Lab yaklaşımı

Repo küçük, zararsız ve tekrar üretilebilir alıştırmalar kullanır. Amaç yalnızca komut ezberlemek değil; delili korumak, yapılan işlemleri belgelemek ve kullanılan aracın neyi kanıtladığını anlamaktır.

## Güvenlik ve etik

Yalnızca size ait olan veya incelemek için açık izin aldığınız dosya, image, sistem ve capture'lar üzerinde çalışın. Mümkün olduğunda orijinali koruyun ve deneyleri kopyalar üzerinde gerçekleştirin.


## Latest lab

- **Day 27 — Download History and File Creation Correlation**
- [English notes](labs/27-download-history-and-file-creation-correlation/notes.md) · [Türkçe notlar](labs/27-download-history-and-file-creation-correlation/notes.tr.md) · [Practical exercise](labs/27-download-history-and-file-creation-correlation/download_demo.py)
