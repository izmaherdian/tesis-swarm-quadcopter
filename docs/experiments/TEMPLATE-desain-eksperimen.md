# E<NN> — <Nama Eksperimen>

> Salin berkas ini jadi `docs/experiments/E01-<nama>.md` dan isi **sebelum**
> menulis kode. Bagian yang masih `<...>` berarti eksperimen belum siap jalan.

| | |
|---|---|
| **ID** | E<NN> |
| **Tanggal desain** | <YYYY-MM-DD> |
| **Status** | rancangan / berjalan / selesai / dibatalkan |
| **Folder hasil** | `results/<YYYY-MM-DD>-E<NN>-<nama>/` |

## 1. Pertanyaan

Satu kalimat. Pertanyaan yang bisa dijawab dengan data, bukan dengan pendapat.

> Contoh: Apakah ERC menurunkan RMSE galat formasi saat melewati lorong selebar
> 1,2 m dibanding formasi kaku tanpa rekonfigurasi?

## 2. Hipotesis

Pernyataan yang **bisa terbukti salah**. Kalau tidak ada hasil yang bisa
menyangkalnya, itu bukan hipotesis.

- **H₀ (nol):** <tidak ada perbedaan yang berarti antara ... dan ...>
- **H₁ (kerja):** <ERC menurunkan ... sebesar sekurang-kurangnya ...>

## 3. Variabel

| Jenis | Variabel | Nilai / rentang |
|---|---|---|
| Bebas (diubah) | <mis. lebar lorong> | <1,0 / 1,2 / 1,5 m> |
| Terikat (diukur) | <mis. RMSE galat formasi> | — |
| Kontrol (ditahan tetap) | <jumlah agen, penguatan PID, seed> | <5 agen, ...> |

## 4. Kondisi pembanding

Minimal satu. Tanpa pembanding, hasilmu tidak punya makna.

- **Baseline A:** <formasi kaku tanpa rekonfigurasi>
- **Baseline B:** <IAPF saja, tanpa pemicu berbasis kejadian>
- **Uji:** <IAPF + ERC>

## 5. Metrik

| Metrik | Satuan | Cara hitung | Arah baik |
|---|---|---|---|
| RMSE galat formasi | m | <rumus / fungsi di kode> | turun |
| Waktu konvergensi | s | <ambang & definisi> | turun |
| Keberhasilan lolos lorong | % | <n berhasil / n percobaan> | naik |
| Jarak minimum antaragen | m | <min sepanjang lintasan> | naik |

## 6. Rancangan percobaan

- **Jumlah ulangan:** <n seed acak — satu run bukan bukti>
- **Daftar seed:** <mis. 0–9>
- **Durasi tiap run:** <detik simulasi>
- **Total run:** <kondisi × seed>

## 7. Kriteria keberhasilan — **ditetapkan sekarang, bukan setelah melihat hasil**

> <Mis.: H₁ diterima bila RMSE turun ≥ 20% pada ketiga lebar lorong, dengan
> keberhasilan lolos tetap ≥ 90%.>

## 8. Yang bisa membuat eksperimen ini gagal

Tulis jujur sebelum jalan — memaksa kamu memikirkan pembatalnya.

- <mis. lorong 1,0 m lebih sempit dari batas fisik formasi tailgating>
- <mis. laju kamera 60 FPS tidak cukup untuk kecepatan manuver yang diuji>

## 9. Konfigurasi

`experiments/E<NN>/config.yaml` — semua parameter ada di sana, bukan di dalam kode.

## 10. Hasil (diisi setelah dijalankan)

| Kondisi | <metrik 1> | <metrik 2> | <metrik 3> |
|---|---|---|---|
| Baseline A | | | |
| Baseline B | | | |
| Uji | | | |

**Kesimpulan:** <H₁ diterima / ditolak — sesuai kriteria di bagian 7, tanpa
menggeser tiang gawang.>

**Yang tidak terduga:** <catat hal aneh, walau tidak mendukung hipotesis.
Ini sering jadi bahan bab Keterbatasan yang paling bernilai.>
