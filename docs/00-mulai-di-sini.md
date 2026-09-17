# Mulai di Sini

> Diperbarui 2026-09-17. Peta seluruh dokumentasi repo. **Angka di depan nama berkas
> dan folder adalah urutan baca.** Folder `arsip/` tidak bernomor karena bukan acuan.

## Urutan baca

| # | Buka | Isinya | Kapan perlu |
|---|---|---|---|
| 0 | berkas ini | peta dokumen dan status proyek | selalu, paling awal |
| 1 | [`01-alur-kerja.md`](01-alur-kerja.md) | lima fase penelitian, alur satu eksperimen, siklus sesi dengan Claude, daftar periksa sebelum kirim draf | sebelum memulai fase atau eksperimen baru |
| 2 | [`02-keputusan/`](02-keputusan/) | catatan keputusan KP01–KP05 (apa yang diputuskan, alasannya, kapan ditinjau ulang) | saat bertanya "kenapa dirancang begini?" |
| 3 | [`03-lab/`](03-lab/README.md) | ruang uji dan arena, inventaris, baterai dan bobot, survei harga, tugas penulis, foto dan video | saat menyentuh perangkat keras, arena, atau RAB |
| 4 | [`04-pustaka/`](04-pustaka/) | kuartil jurnal rujukan, landasan pustaka lokalisasi | saat menambah atau mengganti rujukan |
| 5 | [`05-eksperimen/`](05-eksperimen/TEMPLATE-desain-eksperimen.md) | templat desain eksperimen | sebelum menjalankan eksperimen apa pun |
| — | [`arsip/`](arsip/) | dokumen lama yang sudah digantikan | hanya untuk menelusuri jejak keputusan |

### Catatan keputusan

| Kode | Keputusan |
|---|---|
| [KP01](02-keputusan/KP01-lokalisasi-kamera-apriltag.md) | Lokalisasi dengan kamera atas + AprilTag, bukan UWB |
| [KP02](02-keputusan/KP02-firmware-fc.md) | *Firmware* ArduPilot racikan untuk SpeedyBee F405 Mini |
| [KP03](02-keputusan/KP03-kamera-elp-lensa-2mm.md) | Kamera ELP-U3GS05B10C-IB21 lensa 2,1 mm, dua unit, penanda 12 cm |
| [KP04](02-keputusan/KP04-sensor-jarak-uji-banding.md) | Sensor jarak dipilih lewat uji banding HC-SR04, VL53L1X, MTF-01 |
| [KP05](02-keputusan/KP05-baterai-dan-pengadaan.md) | Baterai 6S 1200 mAh dan aturan pengadaan (batas atas, bertahap per gerbang) |

### Di luar `docs/`

| Berkas | Isinya |
|---|---|
| [`../README.md`](../README.md) | ringkasan repo dan perintah kompilasi |
| [`../CLAUDE.md`](../CLAUDE.md) | fakta penelitian dan aturan kerja, dibaca otomatis oleh Claude tiap sesi |
| [`../tulisan/proposal/main.tex`](../tulisan/proposal/main.tex) | naskah proposal |
| [`../tulisan/gambar/parameter.py`](../tulisan/gambar/parameter.py) | sumber tunggal angka ruang, kamera, dan arena untuk gambar dan tabel |
| [`../experiments/`](../experiments/README.md), [`../results/`](../results/README.md) | konfigurasi dan keluaran eksperimen (belum ada isinya) |
| [`../src/README.md`](../src/README.md) | cara menyiapkan simulator MultiAgentSim versi terkunci |

## Status proyek (2026-09-17)

| Bagian | Keadaan |
|---|---|
| Proposal | Bab I–V lengkap, 58 halaman, `make check` lolos; siap ditinjau pembimbing |
| Anggaran | Rp22.639.974 (Fase 2 Rp10.046.227, Fase 4 Rp12.593.747); setiap pos bertautan listing Tokopedia ([survei harga](03-lab/4-survei-harga.md)) |
| Kamera | ELP-U3GS05B10C-IB21 lensa 2,1 mm, Rp6.600.000 per unit, pra-pesan 3 minggu ([KP03](02-keputusan/KP03-kamera-elp-lensa-2mm.md)) |
| Inventaris lab | tercatat per rangka ([inventaris](03-lab/2-inventaris.md)) |
| Masih dicek penulis | merek router, *firmware* FC terpasang, pemetaan port USB laptop, bobot terbang ditimbang, versi ESC ([tugas penulis](03-lab/5-tugas-penulis.md)) |
| Simulator | versi terkunci `0d7ed5a`; faktor skala κ belum diterapkan (dijadwalkan Fase 1) |
| Eksperimen dan laporan akhir | belum dimulai; Fase 1 berjalan September 2026 |

## Aturan singkat menambah dokumen

- **Keputusan baru** → `02-keputusan/KP<NN>-<topik>.md`, nomor berikutnya. Isi minimal
  konteks, opsi, keputusan, alasan, syarat peninjauan ulang. Keputusan yang dibatalkan
  tidak dihapus, tetapi statusnya diubah dan diberi rujukan ke penggantinya.
- **Eksperimen baru** → salin templat jadi `05-eksperimen/E<NN>-<nama>.md`, isi
  **sebelum** menulis kode atau menerbangkan wahana.
- **Data lab baru** → perbarui berkas bernomor di `03-lab/` yang sesuai, tulis tanggalnya.
  Foto baru diberi nomor berikutnya dan dicatat di `03-lab/foto/README.md`.
- **Dokumen yang usang** → pindah ke `arsip/` dengan tanggal di nama berkas dan
  catatan "digantikan oleh …" di baris pertama.
- Setelah menambah atau memindah berkas, perbarui tabel di berkas ini.
