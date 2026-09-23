# KP07 — Sebutan IAPF dipertahankan, tetapi batas klaimnya ditulis

**Tanggal:** 2026-09-23 · **Status:** diputuskan
**Terkait:** [KP06](KP06-bentuk-evaluasi-dan-hipotesa.md) · proposal Bab II studi terkait,
Bab III subbab perencana tingkat tinggi

## Konteks

Naskah menyebut metode penghindaran rintangan sebagai **IAPF** (*Improved Artificial
Potential Field*), tetapi tidak pernah menerangkan apa yang membuatnya *improved* pada
penelitian ini. Pemeriksaan ke kode versi terkunci menemukan dua hal.

1. **Medan tolak yang dipakai adalah bentuk klasik.** `behavior_obstacle()` menghitung
   `0,5 (1/d − 1/Rₐ) n̂ / d²`, yaitu gradien potensial tolak Khatib, tanpa modifikasi.
2. **Gaya acak tidak aktif.** `behavior_random()` ada di `MultiAgentIAPF.py` dan
   `MultiAgentERC.py`, tetapi **tidak pernah dipanggil** di kedua berkas itu. Padahal
   justru gaya acak inilah yang disebut Bab II sebagai pembeda IAPF terhadap APF klasik.

Tanpa penjelasan, penguji wajar bertanya mengapa metodenya masih disebut IAPF.

## Dasar keputusan

| Dasar | Sumber | Isi yang dipakai |
|---|---|---|
| Kode | `Agent/MultiAgentIAPF.py`, `behavior_obstacle()` | medan tolak berbentuk klasik |
| Kode | pencarian `behavior_random` di `Agent/*.py` | fungsinya ada, pemanggilannya tidak ada |
| Pustaka | `wangUAVFormationObstacle2021` | IAPF didefinisikan sebagai APF + gaya acak + kontrol formasi |
| Pustaka | `herdianDecentralizedFormationControl2026` | makalah penulis menyebut perbaikan berupa logika lepas landas, navigasi tujuan 3D dinamis, pelacakan lintasan, dan orientasi formasi |
| Keputusan penulis | 2026-09-23 | sebutan IAPF dipertahankan agar sejalan dengan makalah yang sudah terbit |

## Keputusan

1. **Nama IAPF tetap dipakai**, karena makalah penulis yang dikutip di naskah memakai nama
   itu dan mengganti nama akan membuat naskah dan rujukannya tidak sejalan.
2. **Batas klaimnya ditulis terang-terangan.** Bab II menyebutkan bahwa perbaikan yang
   dipakai pada penelitian ini adalah paduan perilakunya, yaitu migrasi, formasi dengan
   topologi yang dirotasi dan diskalakan κ, penghindaran antaragen, dan mengekor. Bab III
   menambahkan satu paragraf bahwa medan tolaknya sama dengan bentuk klasik dan suku gaya
   acak tersedia tetapi tidak diaktifkan.
3. **Klaim lama dibuang.** Kalimat Bab II yang menyatakan simulasi terdahulu berhasil
   "dengan efisiensi komunikasi tinggi" diganti, karena simulator tidak memodelkan
   komunikasi sama sekali (lihat [KP06](KP06-bentuk-evaluasi-dan-hipotesa.md)).

## Konsekuensi

- Naskah tidak lagi menjanjikan mekanisme yang tidak dijalankan kodenya.
- Bila suatu saat gaya acak diaktifkan, paragraf di Bab II dan Bab III harus diperbarui dan
  pengaruhnya dibandingkan lewat simulasi, bukan diklaim begitu saja.

## Syarat peninjauan ulang

- Uji terbang atau simulasi menunjukkan kawanan terjebak minimum lokal, sehingga gaya acak
  atau mekanisme lepas jebakan lain perlu diaktifkan.
- Pembimbing meminta sebutan metode diseragamkan menjadi APF saja.
