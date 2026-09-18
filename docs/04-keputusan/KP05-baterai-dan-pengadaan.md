# KP05 — Baterai 6S 1200 mAh dan aturan pengadaan

**Tanggal:** 2026-09-17 · **Status:** diputuskan
**Terkait:** [baterai dan bobot](../02-lab/3-baterai-dan-bobot.md) · [inventaris](../02-lab/2-inventaris.md) ·
[survei harga](../02-lab/4-survei-harga.md) · proposal Tabel Anggaran Fase 2, Fase 4, Rekapitulasi

## Bagian A — Baterai

### Konteks

Motor terpasang adalah SpeedyBee 2006-**1950KV**. SpeedyBee menyarankan baterai **6S
1050–1300 mAh** untuk motor ini. Dari sepuluh baterai di lab, hanya **2 × CNHL Pizza Series
6S 1200 mAh 100C** yang cocok; 4S terlalu rendah untuk 1950KV, 5000 mAh dan 2200 mAh terlalu
berat, 2S/3S di bawah rancangan.

### Opsi

| Opsi | Jumlah 6S | Beli |
|---|---:|---:|
| minimum, satu per wahana | 5 | 3 |
| **satu per wahana + satu cadangan** | **6** | **4** |
| ideal, dua per wahana | 10 | 8 |

### Dasar keputusan

| Dasar | Sumber | Isi yang dipakai |
|---|---|---|
| Data lab | [inventaris 1c](../02-lab/2-inventaris.md) | 10 baterai di lab, hanya 2 yang 6S 1200 mAh |
| Data lab | [inventaris 2](../02-lab/2-inventaris.md) | pengisi daya SkyRC T6X80 80 W, papan pengisian paralel |
| Halaman resmi | `speedybeeBee35`, `SpeedyBeeBee3535a` | motor 2006-1950KV untuk 6S, baterai 1050–1300 mAh |
| Hitungan | [baterai dan bobot](../02-lab/3-baterai-dan-bobot.md) | 1C ≈ 30 W per baterai sehingga 80 W cukup untuk dua baterai paralel |
| Listing | [survei harga](../02-lab/4-survei-harga.md) | Rp637.000 sebagai batas atas |
| Keputusan penulis | 2026-09-17 | total enam baterai, bukan lima atau sepuluh |
| **Belum ada data** | uji terbang tunggal | waktu terbang sebenarnya per baterai |

### Keputusan

**Total enam baterai 6S** (keputusan penulis): beli **4 × CNHL Pizza Series 6S 1200 mAh
100C** pada Fase 4 setelah uji terbang tunggal lolos, harga batas atas Rp637.000.
Uji terbang tunggal cukup memakai dua baterai yang ada. Baterai 4S dipakai untuk uji meja
tanpa propeler.

### Konsekuensi

- Pengisi daya SkyRC T6X80 (80 W) hanya dapat mengisi **dua baterai 6S paralel pada 1C**.
  Enam baterai butuh sekitar tiga putaran pengisian, sehingga sesi uji kawanan dijadwalkan
  dengan jeda pengisian.
- Bobot terbang perkiraan **≈ 520 g** termasuk baterai (batas bawah, belum ditimbang).
- Baterai disimpan dalam kontainer lab, tas LiPo tidak dianggarkan.

## Bagian B — Aturan pengadaan

1. **Sumber harga** hanya RAB awal penulis atau listing Tokopedia yang tautannya dicatat di
   survei harga. Pos tanpa sumber ditulis *survei*, tidak diperkirakan.
2. **Batas atas.** Bila ada beberapa listing untuk produk yang sama persis, dipakai harga
   tertinggi. Listing yang dikecualikan (paket berisi barang lain, versi berbeda, produk lain
   berjudul mirip, salah input) dicatat alasannya.
3. **Bertahap mengikuti gerbang.** Anggaran hanya ada di Fase 2 dan Fase 4. Komponen untuk
   lima wahana dibeli **setelah uji terbang tunggal lolos**, karena tiga ketidakpastian
   (firmware muat 1 MB, deteksi penanda saat bergerak, sensor jarak andal) hanya terjawab
   lewat percobaan.
4. **Mengikuti inventaris.** Yang sudah ada tidak dibeli lagi: *flight controller* (6),
   motor (20), penerima ExpressLRS (5). Yang dibeli hanya kekurangan nyata:
   - 1 ESC BLS 35A Mini V2 (ESC lepas diduga rusak),
   - 1 XIAO ESP32-S3 sebagai cadangan (keputusan penulis),
   - 2 paket propeler Gemfan D90S (20 dibutuhkan, 14 ada),
   - 4 baterai 6S (bagian A).
5. **Keselamatan.** Pemancar RadioMaster Pocket dibeli di **Fase 2** karena satu-satunya
   jalur penghentian darurat yang tidak bergantung pada Wi-Fi. Kacamata pengaman cukup
   satu; jaring pengaman tidak diperlukan (keputusan penulis).
6. **Tidak dianggarkan karena tersedia di lab:** tiang penanda (pencetak 3D), kontainer
   baterai, pengisi daya, laptop stasiun darat, router Wi-Fi.
7. **Kontinjensi** yang bergantung hasil uji (MTF-01) ditulis sebagai harga satuan saja dan
   tidak masuk subtotal.

### Hasil (proposal 2026-09-17)

| Fase | Subtotal |
|---|---:|
| Fase 2 | Rp10.046.227 |
| Fase 4 | Rp12.593.747 |
| **Total** | **Rp22.639.974** |

## Syarat peninjauan ulang

- Bobot hasil timbang jauh di atas 520 g sehingga rasio gaya dorong tidak memadai →
  tinjau kapasitas baterai.
- Waktu terbang per baterai terlalu singkat untuk satu lintasan arena ditambah pengulangan →
  pertimbangkan menambah baterai ke arah opsi ideal.
- Stok ESC V2 atau kamera habis atau harga berubah → survei ulang dengan aturan yang sama.
