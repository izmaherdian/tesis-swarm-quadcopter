# Mulai di Sini

> Diperbarui 2026-09-18. Peta seluruh dokumentasi repo. **Angka di depan nama berkas dan
> folder mengikuti urutan kerja**, yaitu data lab dulu, lalu sumber, baru keputusan.
> Folder `arsip/` tidak bernomor karena bukan acuan.

```
02-lab (data lapangan) → 03-pustaka (sumber) → 04-keputusan (KP) → naskah, pengadaan
                                    ▲                                     │
                                    └────── 05-eksperimen (hasil uji) ◄───┘
```

## Urutan baca

| # | Buka | Isinya | Kapan perlu |
|---|---|---|---|
| 0 | berkas ini | peta dokumen dan status proyek | selalu, paling awal |
| 1 | [`01-alur-kerja.md`](01-alur-kerja.md) | rantai bukti (lab → pustaka → keputusan), lima fase pelaksanaan, alur satu eksperimen, siklus sesi, daftar periksa | sebelum memulai fase, keputusan, atau eksperimen baru |
| 2 | [`02-lab/`](02-lab/README.md) | ruang uji dan arena, inventaris, baterai dan bobot, survei harga, tugas penulis, foto dan video | **langkah pertama** tiap kali menyentuh perangkat keras, arena, atau RAB |
| 3 | [`03-pustaka/`](03-pustaka/README.md) | indeks sumber per topik, kuartil jurnal, landasan lokalisasi | saat mencari dasar sebuah pilihan atau menambah rujukan |
| 4 | [`04-keputusan/`](04-keputusan/README.md) | KP01–KP05, masing-masing dengan tabel dasar keputusan | saat bertanya "kenapa dirancang begini?" atau saat memutuskan hal baru |
| 5 | [`05-eksperimen/`](05-eksperimen/TEMPLATE-desain-eksperimen.md) | templat desain eksperimen | sebelum menjalankan eksperimen apa pun |
| — | [`arsip/`](arsip/) | dokumen lama yang sudah digantikan | hanya untuk menelusuri jejak keputusan |

### Catatan keputusan

| Kode | Keputusan |
|---|---|
| [KP01](04-keputusan/KP01-lokalisasi-kamera-apriltag.md) | Lokalisasi dengan kamera atas + AprilTag, bukan UWB |
| [KP02](04-keputusan/KP02-firmware-fc.md) | *Firmware* ArduPilot racikan untuk SpeedyBee F405 Mini |
| [KP03](04-keputusan/KP03-kamera-elp-lensa-2mm.md) | Kamera ELP-U3GS05B10C-IB21 lensa 2,1 mm, dua unit, penanda 12 cm |
| [KP04](04-keputusan/KP04-sensor-jarak-uji-banding.md) | Sensor jarak dipilih lewat uji banding HC-SR04, VL53L1X, MTF-01 |
| [KP05](04-keputusan/KP05-baterai-dan-pengadaan.md) | Baterai 6S 1200 mAh dan aturan pengadaan (batas atas, bertahap per gerbang) |

### Di luar `docs/`

| Berkas | Isinya |
|---|---|
| [`../README.md`](../README.md) | ringkasan repo dan perintah kompilasi |
| [`../CLAUDE.md`](../CLAUDE.md) | fakta penelitian dan aturan kerja, dibaca otomatis oleh Claude tiap sesi |
| [`../tulisan/proposal/main.tex`](../tulisan/proposal/main.tex) | naskah proposal |
| [`../tulisan/gambar/parameter.py`](../tulisan/gambar/parameter.py) | sumber tunggal angka ruang, kamera, dan arena untuk gambar dan tabel |
| [`../experiments/`](../experiments/README.md), [`../results/`](../results/README.md) | konfigurasi dan keluaran eksperimen (belum ada isinya) |
| [`../src/README.md`](../src/README.md) | cara menyiapkan simulator MultiAgentSim versi terkunci |

## Status proyek (2026-09-18)

| Bagian | Keadaan |
|---|---|
| Proposal | Bab I–V lengkap, 58 halaman, `make check` lolos; siap ditinjau pembimbing |
| Anggaran | Rp22.639.974 (Fase 2 Rp10.046.227, Fase 4 Rp12.593.747); setiap pos bertautan listing Tokopedia ([survei harga](02-lab/4-survei-harga.md)) |
| Kamera | ELP-U3GS05B10C-IB21 lensa 2,1 mm, Rp6.600.000 per unit, pra-pesan 3 minggu ([KP03](04-keputusan/KP03-kamera-elp-lensa-2mm.md)) |
| Inventaris lab | tercatat per rangka ([inventaris](02-lab/2-inventaris.md)) |
| Masih dicek penulis | merek router, *firmware* FC terpasang, pemetaan port USB laptop, bobot terbang ditimbang, versi ESC ([tugas penulis](02-lab/5-tugas-penulis.md)) |
| Simulator | versi terkunci `0d7ed5a`; faktor skala κ belum diterapkan (dijadwalkan Fase 1) |
| Eksperimen dan laporan akhir | belum dimulai; Fase 1 berjalan September 2026 |

## Aturan singkat menambah dokumen

- **Keputusan baru** → data lab dan sumbernya dicatat dulu, baru buat
  `04-keputusan/KP<NN>-<topik>.md` dengan konteks, opsi, **tabel dasar keputusan**,
  keputusan, konsekuensi, dan syarat peninjauan ulang. Keputusan yang dibatalkan tidak
  dihapus, tetapi statusnya diubah dan diberi rujukan ke penggantinya.
- **Rujukan baru** → masuk `tulisan/common/references.bib`, kuartilnya dicatat di
  `03-pustaka/kuartil-jurnal.md`, perannya di indeks `03-pustaka/README.md`.
- **Eksperimen baru** → salin templat jadi `05-eksperimen/E<NN>-<nama>.md`, isi
  **sebelum** menulis kode atau menerbangkan wahana.
- **Data lab baru** → perbarui berkas bernomor di `02-lab/` yang sesuai, tulis tanggalnya.
  Foto baru diberi nomor berikutnya dan dicatat di `02-lab/foto/README.md`.
- **Dokumen yang usang** → pindah ke `arsip/` dengan tanggal di nama berkas dan
  catatan "digantikan oleh …" di baris pertama.
- Setelah menambah atau memindah berkas, perbarui tabel di berkas ini.
