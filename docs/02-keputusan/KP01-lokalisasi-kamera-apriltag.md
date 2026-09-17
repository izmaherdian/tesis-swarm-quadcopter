# KP01 — Lokalisasi memakai kamera atas + AprilTag, UWB opsional

**Tanggal:** 2026-09-16 · **Diperbarui:** 2026-09-17 · **Status:** diputuskan, berlaku
**Terkait:** [KP02](KP02-firmware-fc.md) (firmware ExtNav) · [KP03](KP03-kamera-elp-lensa-2mm.md) (model kamera)

## Konteks

Rencana awal ingin mencoba UWB lebih dulu, lalu kamera. Tahap lokalisasi berada di jalur
kritis menuju uji terbang tunggal. Pada jadwal yang berlaku (Bab IV, September 2026 –
Mei 2027), lokalisasi dikerjakan di Fase 2 (Oktober–November 2026) dan uji terbang
tunggal di Fase 4 mulai Desember 2026.

## Keputusan

**Kamera atas + AprilTag sebagai jalur utama. UWB opsional dan bersyarat.**

## Alasan

1. **Jadwal.** *Bring-up* AprilTag berskala hari–minggu (kalibrasi intrinsik sekali,
   pustaka matang). UWB menuntut survei posisi *anchor* presisi sentimeter, kalibrasi
   *antenna delay* per modul, dan penjadwalan TWR untuk 5 tag, pekerjaan berminggu-minggu
   dengan varians tinggi, tepat di jalur kritis.
2. **Semua agen sekaligus.** Satu bingkai kamera membaca kelima wahana bersamaan pada
   laju penuh; TWR menjadwalkan tiap tag bergantian sehingga laju per tag turun.
3. **Akurasi.** Sistem lokalisasi kamera eksternal terlapor mencapai galat pose < 3 cm
   dan < 1° tanpa *drift* (Bultmann dkk., ICRA 2023), lihat
   [`04-pustaka/landasan-lokalisasi.md`](../04-pustaka/landasan-lokalisasi.md).

⚠️ **Angka UWB belum bersumber.** Perbandingan awal sempat memakai galat UWB 10–30 cm.
Angka itu perkiraan dan tidak dipakai sebagai pembenaran di naskah.

## Syarat peninjauan ulang

UWB dipertimbangkan lagi hanya bila kalibrasi Fase 2 atau uji terbang tunggal
menunjukkan penanda **tidak terdeteksi andal** di sebagian segmen uji dan ketiga jalan
keluar di [KP03](KP03-kamera-elp-lensa-2mm.md) (penanda lebih besar, terbang lebih
tinggi, kamera ketiga) tidak memadai.

> Syarat lama (2026-09-16) merujuk sapuan sensitivitas "E01" (σ ≥ 20 cm, laju ≤ 15 Hz).
> Eksperimen itu tidak masuk proposal yang berlaku, sehingga syaratnya diganti di atas.

## Fakta susulan yang tidak membatalkan keputusan

- **Plafon hanya 300 cm.** Jarak kamera–penanda 1,72 m, satu kamera tidak cukup untuk
  segmen 7,20 m sehingga dibutuhkan **dua kamera** ([ruang uji](../03-lab/1-ruang-uji-dan-arena.md)).
  Jalur kamera jadi lebih mahal dari perkiraan awal, tetapi kelebihannya tetap ada.
  Catatan 2026-09-16 menyebut "2 kamera 4K"; kamera yang berlaku adalah ELP 5 MP
  *global shutter* ([KP03](KP03-kamera-elp-lensa-2mm.md)).
- **FC tidak menerima masukan eksternal pada firmware bawaan.** Build ArduPilot untuk
  `SpeedyBeeF405Mini` mematikan `AP_BEACON_ENABLED` **dan** `EK3_FEATURE_EXTERNAL_NAV`.
  Jalur UWB pun tertutup tanpa firmware racikan, lihat [KP02](KP02-firmware-fc.md).
