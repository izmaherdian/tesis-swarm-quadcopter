# E<NN> — <Nama Eksperimen>

> Salin berkas ini jadi `docs/05-eksperimen/E<NN>-<nama>.md` dan isi **sebelum** menulis
> kode atau menerbangkan wahana. Bagian yang masih `<...>` berarti eksperimen belum siap
> jalan. Alur lengkapnya di [`01-alur-kerja.md`](../01-alur-kerja.md) bagian 3.

| | |
|---|---|
| **ID** | E<NN> |
| **Fase** | <1 simulasi / 2 implementasi / 3 HITL / 4 uji terbang / 5 analisis> |
| **Jenis** | <simulasi / uji meja / uji terbang> |
| **Tanggal desain** | <YYYY-MM-DD> |
| **Status** | rancangan / berjalan / selesai / dibatalkan |
| **Konfigurasi** | `experiments/E<NN>-<nama>/config.yaml` |
| **Folder hasil** | `results/<YYYY-MM-DD>-E<NN>-<nama>/` |

## 1. Pertanyaan

Satu kalimat. Pertanyaan yang bisa dijawab dengan data, bukan dengan pendapat.

> Contoh: Apakah ERC membuat kelima wahana melintasi celah 0,90 m di arena tanpa
> tabrakan dan dengan jarak minimum antaragen di atas batas aman, dibanding formasi V
> kaku tanpa rekonfigurasi?

## 2. Hipotesis

Pernyataan yang **bisa terbukti salah**. Kalau tidak ada hasil yang bisa
menyangkalnya, itu bukan hipotesis.

- **H₀ (nol):** <tidak ada perbedaan yang berarti antara ... dan ...>
- **H₁ (kerja):** <ERC menaikkan/menurunkan ... sebesar sekurang-kurangnya ...>

## 3. Variabel

| Jenis | Variabel | Nilai / rentang |
|---|---|---|
| Bebas (diubah) | <mis. lebar celah, sudut sensor β> | <...> |
| Terikat (diukur) | <mis. RMSE galat formasi> | — |
| Kontrol (ditahan tetap) | <jumlah agen, parameter ERC, ketinggian terbang, jenis baterai> | <5 agen, 1,3 m, 6S 1200 mAh> |

## 4. Kondisi pembanding

Minimal satu. Tanpa pembanding, hasilmu tidak punya makna.

- **Baseline A:** <formasi kaku tanpa rekonfigurasi>
- **Baseline B:** <IAPF saja, tanpa pemicu berbasis kejadian>
- **Uji:** <IAPF + ERC>
- **Simulasi arena berskala** (untuk uji fisik): <skema simulator yang meniru arena>

## 5. Metrik

| Metrik | Satuan | Cara hitung | Arah baik |
|---|---|---|---|
| RMSE galat formasi | m | <rumus / fungsi di kode> | turun |
| Waktu konvergensi | s | <ambang & definisi> | turun |
| Keberhasilan melintasi celah | % | <n berhasil / n percobaan> | naik |
| Jarak minimum antaragen | m | <min sepanjang lintasan> | naik |
| Beban komputasi, *bandwidth* | %, kbit/s | <alat ukur> | turun |

## 6. Rancangan percobaan

- **Jumlah ulangan:** <n seed (simulasi) atau n lintasan (uji terbang) — satu run bukan bukti>
- **Urutan kondisi:** <diacak atau bergantian, supaya kondisi baterai/ruang tidak berat sebelah>
- **Durasi tiap run:** <detik>
- **Total run:** <kondisi × ulangan>

## 7. Perangkat dan keadaan (uji fisik)

| Butir | Nilai |
|---|---|
| Wahana yang dipakai | <nomor rangka> |
| *Firmware* FC | <berkas .apj + daftar fitur, [KP02](../04-keputusan/KP02-firmware-fc.md)> |
| Kamera dan kalibrasi | <jumlah kamera, berkas kalibrasi, tanggal> |
| Sensor jarak | <jenis, sudut β> |
| Baterai | <nomor baterai, tegangan awal> |
| Arena | <susunan dus, [ruang uji](../02-lab/1-ruang-uji-dan-arena.md)> |
| Keselamatan | <pemancar terikat, uji pengambilalihan manual, kacamata, area dikosongkan> |

## 8. Kriteria keberhasilan — **ditetapkan sekarang, bukan setelah melihat hasil**

> <Mis.: H₁ diterima bila keberhasilan melintasi celah ≥ <n>% dari <m> lintasan dan jarak
> minimum antaragen tidak pernah di bawah <d> m.>

## 9. Yang bisa membuat eksperimen ini gagal

Tulis jujur sebelum jalan — memaksa kamu memikirkan pembatalnya.

- <mis. penanda di ujung liputan kamera jatuh jauh di bawah acuan 70 px karena distorsi lensa, pose hilang>
- <mis. sensor jarak kehilangan pantulan pada kolom beton di sudut 45°>
- <mis. Wi-Fi padat sehingga latensi MAVLink/UDP melonjak>

## 10. Konfigurasi

`experiments/E<NN>-<nama>/config.yaml` — semua parameter ada di sana, bukan di dalam kode.

## 11. Hasil (diisi setelah dijalankan)

| Kondisi | <metrik 1> | <metrik 2> | <metrik 3> |
|---|---|---|---|
| Baseline A | | | |
| Baseline B | | | |
| Uji | | | |

**Kesimpulan:** <H₁ diterima / ditolak — sesuai kriteria di bagian 8, tanpa
menggeser tiang gawang.>

**Yang tidak terduga:** <catat hal aneh, walau tidak mendukung hipotesis.
Ini sering jadi bahan bab Keterbatasan yang paling bernilai.>
