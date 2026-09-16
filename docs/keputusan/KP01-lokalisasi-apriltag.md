# KP01 — Lokalisasi memakai kamera atas + AprilTag, UWB opsional

**Tanggal:** 2026-09-16 · **Status:** diputuskan

## Konteks

Rencana awal ingin mencoba UWB lebih dulu, lalu kamera. Jadwal di proposal
memberi 2 bulan (Sep–Okt 2026) untuk Setup Lokalisasi, dan tahap itu berada di
jalur kritis menuju uji terbang single-agent bulan November.

## Keputusan

**Kamera atas + AprilTag sebagai jalur utama. UWB opsional dan bersyarat.**

## Alasan

1. **Jadwal.** Bring-up AprilTag berskala hari–minggu (kalibrasi intrinsik sekali,
   pustaka matang). UWB menuntut survei posisi *anchor* presisi sentimeter,
   kalibrasi *antenna delay* per modul, dan penjadwalan TWR untuk 5 tag — pekerjaan
   berminggu-minggu dengan varians tinggi, di atas jalur kritis.
2. **Semua agen sekaligus.** Satu bingkai kamera membaca kelima wahana bersamaan
   pada laju penuh; TWR harus menjadwalkan tiap tag bergantian sehingga laju per
   tag turun.
3. **Akurasi.** Sistem lokalisasi kamera eksternal terlapor mencapai galat pose
   < 3 cm dan < 1° tanpa *drift* (Bultmann dkk., ICRA 2023) — lihat
   `docs/pustaka/E01-landasan-lokalisasi.md`.

⚠️ **Kejujuran soal angka UWB.** Perbandingan awal sempat memakai angka galat UWB
10–30 cm. Angka itu **perkiraan, belum bersumber**, dan tidak dipakai sebagai
pembenaran resmi maupun sebagai batas sapuan E01.

## Syarat peninjauan ulang

UWB dipertimbangkan lagi hanya bila **keduanya** terpenuhi:
1. E01 menunjukkan ERC masih andal pada σ ≥ 20 cm dan laju ≤ 15 Hz, **dan**
2. Uji terbang kawanan dengan kamera sudah berjalan.

## Catatan susulan (2026-09-16, setelah data lab masuk)

Dua fakta baru yang perlu dicatat, dan keduanya **tidak membatalkan** keputusan
ini:

- **Plafon lab hanya 300 cm.** Jarak kamera–penanda tinggal 1,4–1,9 m, sehingga
  satu kamera hanya meliput 4,80 m lorong. Ini membuat jalur kamera lebih mahal
  dari perkiraan awal (2 kamera 4K, bukan 1 kamera 1080p). UWB tidak terpengaruh
  tinggi plafon — jadi kelebihan kamera menyusut, tapi tidak hilang.
- **FC tidak bisa menerima masukan beacon.** Build ArduPilot untuk
  `SpeedyBeeF405Mini` mematikan `AP_BEACON_ENABLED` **dan**
  `EK3_FEATURE_EXTERNAL_NAV`. Jadi jalur UWB pun tertutup pada papan ini tanpa
  firmware racikan — lihat [[KP02-firmware-fc]].
