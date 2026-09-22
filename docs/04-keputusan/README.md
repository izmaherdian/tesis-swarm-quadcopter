# 04-keputusan — Catatan Keputusan Perancangan (KP)

> Diperbarui 2026-09-22. Keputusan ditulis **setelah** data lab ada
> ([`02-lab/`](../02-lab/README.md)) dan sumbernya jelas
> ([`03-pustaka/`](../03-pustaka/README.md)). Rantai lengkapnya di
> [`01-alur-kerja.md`](../01-alur-kerja.md) bagian 2.

| Kode | Keputusan | Status | Bersandar terutama pada |
|---|---|---|---|
| [KP01](KP01-lokalisasi-kamera-apriltag.md) | Lokalisasi kamera atas + AprilTag, UWB opsional | berlaku | plafon 300 cm, Bultmann dkk. 2023, fitur firmware |
| [KP02](KP02-firmware-fc.md) | *Firmware* ArduPilot racikan untuk F405 Mini | berlaku, dieksekusi Fase 2 | 6 papan flash 1 MB, dokumentasi ArduPilot |
| [KP03](KP03-kamera-elp-lensa-2-1mm.md) | Kamera ELP-U3GS05B10C-IB21 lensa 2,1 mm, dua unit, penanda 12 cm | berlaku, diuji saat kalibrasi | ukuran ruang, lembar data ELP, hitungan `parameter.py` |
| [KP04](KP04-sensor-jarak-uji-banding.md) | Sensor jarak dipilih lewat uji banding tiga kandidat | metode diputuskan, sensor belum terpilih | permukaan arena, Borenstein 1988, lembar data MTF-01 |
| [KP05](KP05-baterai-dan-pengadaan.md) | Baterai 6S 1200 mAh (total 6) dan aturan pengadaan | berlaku | inventaris baterai, halaman resmi SpeedyBee, survei harga |
| [KP06](KP06-bentuk-evaluasi-dan-hipotesa.md) | Hipotesa diganti ke klaim yang diuji, evaluasi tanpa pembanding terbang di celah, metrik mengikuti kode | berlaku | kode simulator terkunci, makalah penulis, geometri arena |

## Isi wajib sebuah KP

1. **Judul dan status** beserta tanggal dibuat dan tanggal diperbarui.
2. **Konteks** — masalah yang memaksa keputusan diambil.
3. **Opsi yang dipertimbangkan** beserta biaya dan risikonya.
4. **Dasar keputusan** — tabel berisi data lab, pustaka, lembar data, hasil uji, dan
   keputusan penulis, masing-masing dengan tautan. Hal yang belum berdasar ditulis apa
   adanya sebagai asumsi atau "belum ada data", jangan disamarkan.
5. **Keputusan** dan **konsekuensi** yang harus ditulis di naskah.
6. **Syarat peninjauan ulang** — kondisi terukur yang membuat keputusan ini dibuka lagi.

## Kalau hasil uji bertentangan

Perbarui KP-nya beserta tanggal dan alasannya, sebutkan eksperimen mana
(`results/<id>/`) yang menyebabkannya, lalu periksa apakah naskah dan RAB ikut berubah.
Keputusan lama tidak dihapus supaya jejaknya tetap terbaca.
