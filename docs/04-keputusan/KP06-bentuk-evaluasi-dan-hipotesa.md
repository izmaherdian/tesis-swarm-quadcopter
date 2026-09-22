# KP06 — Bentuk evaluasi fisik, hipotesa, dan definisi metrik

**Tanggal:** 2026-09-22 · **Status:** diputuskan
**Terkait:** [KP03](KP03-kamera-elp-lensa-2-1mm.md) · [ruang uji dan arena](../02-lab/1-ruang-uji-dan-arena.md) ·
proposal Bab I Hipotesa, Subbab "Metrik Evaluasi dan Kriteria Kelayakan", Fase 4 dan Fase 5

## Konteks

Tiga persoalan muncul bersamaan saat memeriksa apakah proposal sudah layak diuji.

1. **Klaim utama tidak punya dasar.** Hipotesa lama berbunyi ERC "mereduksi pertukaran data
   komunikasi antaragen secara signifikan dibandingkan skema komunikasi periodik". Simulator
   versi terkunci `0d7ed5a` **tidak memodelkan komunikasi sama sekali**, dan makalah penulis
   juga tidak mengklaim penghematan komunikasi. Yang diklaim makalah adalah ERC menjaga
   performa nominal di medan rintangan biasa dan membuat misi layak di celah sempit tempat
   IAPF statis gagal.
2. **Pembanding fisik berbahaya.** Menerbangkan formasi V kaku menembus celah berarti
   memasukkan bentang 2,05 m ke celah 0,90 m, yaitu tabrakan yang pasti secara geometris.
3. **Metrik dan gerbang tanpa angka.** Naskah menyebut RMSE tanpa rumus dan gerbang berupa
   "batas aman" tanpa nilai, sehingga kriteria bisa bergeser setelah hasil terlihat.

## Dasar keputusan

| Dasar | Sumber | Isi yang dipakai |
|---|---|---|
| Kode | `MultiAgentSim` @ `0d7ed5a`, `Visualization/generate_plots.py` | definisi RMSE formasi antarpasangan, RMSE mengekor terhadap `DREF`, dan RMSE operasional yang berpindah mengikuti mode |
| Kode | `Visualization/analysis_for_report.py`, `compute_order` | parameter keteraturan Φ sebagai norma rata-rata vektor satuan kecepatan |
| Kode | pencarian istilah komunikasi di `Agent/*.py` | **nol** kemunculan istilah komunikasi, paket, atau *bandwidth*, sehingga klaim penghematan tidak berdasar |
| Pustaka | `herdianDecentralizedFormationControl2026` | ERC menyelesaikan misi celah sempit dengan RMSE 0,692 m dan Φ 0,878, sedangkan IAPF statis gagal |
| Data lab | [ruang uji dan arena](../02-lab/1-ruang-uji-dan-arena.md) | bentang formasi 2,05 m, celah 0,90 m, jarak mengekor rancangan 0,36 m |
| Lembar data | halaman resmi SpeedyBee Bee35 | waktu terbang maksimum 13 menit pada 6S 1300 mAh untuk wahana sekelas, dipakai menaksir jumlah lintasan per baterai |
| Keputusan penulis | 2026-09-22 | klaim diganti, pembanding tidak diterbangkan menembus celah, metrik disamakan dengan kode |
| **Asumsi rancangan** | — | seluruh **angka ambang gerbang** (70% CPU, 50 ms, 0,10 m, 95% bingkai, 8 dari 10 lintasan, 0,30 m, 10 detik) belum berdasar pengukuran; ditinjau setelah simulasi arena Fase 1 |

## Keputusan

1. **Hipotesa diganti** ke klaim yang memang diuji, yaitu ERC memungkinkan kelima wahana
   melintasi celah 0,90 m yang lebih sempit daripada bentang formasi 2,05 m, formasi pulih
   setelah celah, dan tidak ada pelanggaran jarak aman antaragen. Beban komputasi dan trafik
   komunikasi tetap diukur, tetapi sebagai karakterisasi sumber daya, bukan klaim penghematan.
2. **Rumusan masalah dan sasaran ikut diubah** supaya tidak lagi menjanjikan perbandingan
   terhadap skema komunikasi periodik yang tidak diterbangkan.
3. **Bentuk evaluasi** yaitu kondisi kontrol berupa formasi V tanpa rekonfigurasi di koridor
   terbuka, kondisi uji berupa ERC melintasi arena, dan pembanding kuantitatif diambil dari
   simulasi arena berskala Fase 1. Formasi kaku **tidak** diterbangkan menembus celah.
4. **Metrik memakai definisi kode** sehingga hasil fisik dan simulasi sebanding tanpa
   penyesuaian, yaitu RMSE formasi, RMSE mengekor, Φ, waktu tempuh, waktu pemulihan formasi,
   keberhasilan melintas, jarak minimum antaragen, beban CPU, dan trafik UDP.
5. **Sepuluh lintasan per kondisi**, dengan taksiran lima sampai delapan lintasan per baterai
   sehingga dibutuhkan dua putaran pengisian.

## Konsekuensi

- Tesis kehilangan klaim penghematan *bandwidth*, yang selama ini menjadi daya tarik judul.
  Gantinya adalah klaim kelayakan fisik yang benar-benar diukur, dan itu sejalan dengan judul
  "Implementasi Fisik dan Evaluasi".
- Perbandingan terhadap simulasi menjadi tulang punggung evaluasi, sehingga simulasi arena
  berskala pada Fase 1 berubah dari pelengkap menjadi **keluaran wajib**.
- Bila kelak ingin mengklaim penghematan komunikasi, jalurnya ada dua, yaitu menghitungnya
  secara analitis dari log penerbangan yang sama atau benar-benar menerapkan komunikasi
  terpicu kejadian di ESP32-S3. Keduanya menambah ruang lingkup dan tidak diambil sekarang.

## Syarat peninjauan ulang

- Simulasi arena Fase 1 memberi nilai acuan yang jauh berbeda dari ambang di Tabel Kriteria
  Kelayakan, sehingga ambangnya perlu disetel ulang sebelum uji terbang.
- Uji terbang tunggal menunjukkan satu baterai hanya cukup untuk kurang dari lima lintasan,
  sehingga jumlah ulangan atau jumlah baterai perlu ditinjau ([KP05](KP05-baterai-dan-pengadaan.md)).
- Muncul kebutuhan menguji klaim komunikasi secara langsung, yang berarti keputusan ini
  dibuka lagi bersama ruang lingkup di Bab I.
