# docs/lab/ — Karakterisasi Lab

Data fisik ruangan dan perangkat keras di PTIO ITB. Diisi sekali di awal, lalu
diperbarui kalau ada perubahan.

## Kenapa ini dikerjakan lebih dulu

Tiga keputusan bergantung pada data di sini, dan ketiganya mahal kalau salah:

1. **Apakah satu kamera atas cukup?** Bergantung pada tinggi langit-langit dan
   luas area terbang. Kalau tidak cukup, butuh lensa lebih lebar atau kamera
   kedua — dan itu mengubah anggaran serta jadwal.
2. **Berapa ukuran AprilTag yang harus dicetak?** Bergantung pada tinggi
   pemasangan dan resolusi kamera. Tag terlalu kecil = deteksi putus-putus saat
   terbang.
3. **Apakah skenario koridor 1,0 m muat di ruangan itu?** Butuh koridor +
   jalur ancang-ancang + area keluar untuk 5 agen. Kalau tidak muat, skenario
   pengujian harus dirancang ulang.

Selain itu, isi folder ini jadi bahan langsung untuk **BAB III Metodologi**
subbab Perangkat Keras dan Lokasi Pelaksanaan.

## Cara mengisi

| Berkas | Isi |
|---|---|
| `kondisi-lab.md` | Ukuran ruangan, langit-langit, pencahayaan, lantai, dinding |
| `spesifikasi-hw.md` | Kamera, flight controller, companion computer, wahana, sensor |
| `foto/` | Foto dari ponsel — lihat `foto/README.md` untuk daftar yang diminta |

Isi seadanya. **Kolom yang belum diketahui tulis `?`** — jangan dikosongkan,
supaya jelas mana yang belum terdata dan mana yang memang tidak ada.

Ukuran kasar pakai langkah kaki atau meteran HP sudah cukup untuk tahap ini;
yang penting ordenya benar. Nanti diperhalus sebelum masuk naskah.

## Setelah terisi

Beri tahu saya, lalu saya susun `analisis-kelayakan.md` berisi perhitungan
cakupan kamera, ukuran tag minimum, kelayakan skenario, dan daftar risiko.
