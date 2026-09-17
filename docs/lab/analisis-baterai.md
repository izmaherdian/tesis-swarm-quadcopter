# Analisis Baterai untuk Wahana Bee35

> Dibuat 2026-09-17 dari inventaris yang dicatat penulis.

## Acuan pabrikan

| Sumber | Isi |
|---|---|
| [SpeedyBee Bee35 3.5" Frame](https://www.speedybee.com/speedybee-bee35-3-5-inch-frame/) | Baterai yang disarankan **900–1500 mAh 4S/6S**; KV motor yang disarankan **4S: 2500–3500KV, 6S: 1800–2300KV** |
| [SpeedyBee Bee35 3.5" Drone (motor 2006-1950KV)](https://www.speedybee.com/speedybee-bee35-3-5-inch-drone-hd-o3-air-unit-fpv/) | Motor **2006-1950KV (6S)**; baterai **6S LiPo, disarankan 1050–1300 mAh** |
| [SpeedyBee F405 Mini BLS 35A Stack](https://www.speedybee.com/speedybee-f405-mini-bls-35a-20x20-stack/) | ESC BLS 35A untuk 3–6S |

Motor terpasang adalah 2006-**1950KV**, yang masuk rentang KV untuk **6S**. Untuk 4S,
pabrikan menyarankan motor 2500–3500KV; dengan 1950KV pada 4S putaran maksimum turun
sekitar sepertiga (tegangan 14,8 V vs 22,2 V), sehingga gaya dorong tidak sesuai
rancangan, apalagi dengan beban tambahan (ESP32-S3, penanda bertiang, dua sensor jarak).

## Kecocokan baterai yang tersedia

| Baterai | Jumlah | Penilaian |
|---|---:|---|
| CNHL Pizza Series 6S 1200 mAh 100C | 2 | ✅ **Cocok.** 6S sesuai motor 1950KV, kapasitas dalam rentang 1050–1300 mAh, konektor XT60 (bobot sekitar 210 g menurut [CNHL](https://chinahobbyline.com/products/cnhl-pizza-series-1200mah-22-2v-6s-100c-lipo-battery-with-xt60-plug)) |
| CNHL Speedy Pizza 4S 1200 mAh 100C | 2 | ⚠️ Tidak untuk terbang uji: tegangan 4S di bawah rancangan motor 1950KV. Layak untuk uji meja **tanpa propeler** (arah putar motor, konfigurasi ESC/FC, komunikasi) |
| Gens Ace 5S 5000 mAh 40C | 2 | ❌ Kapasitas jauh di atas 900–1500 mAh sehingga terlalu berat untuk rangka 3,5 inci; 5S juga bukan konfigurasi yang disarankan |
| Onbo 4S 2200 mAh 50C | 1 | ❌ 4S dan kapasitas di atas rentang |
| Onbo Nano Power 3S 1500 mAh 25C | 2 | ❌ Tegangan terlalu rendah untuk motor 1950KV |
| LPB Power 2S/3S 1500 mAh 20–25C | 1 | ❌ 2S di bawah rentang kerja ESC (3–6S); 3S terlalu rendah |

## Kebutuhan

- **Satu baterai 6S per wahana** untuk uji kawanan serentak → 5 baterai. Tersedia 2,
  **kurang 3**.
- Agar pengulangan uji tidak menunggu pengisian, idealnya **satu cadangan per wahana**
  → 10 baterai, **kurang 8**.
- Uji terbang tunggal (Fase 4 awal) cukup dengan 2 baterai 6S yang ada.
- Papan pengisian paralel Power Genius hanya boleh mengisi baterai **bersel sama**
  (semua 6S) secara bersamaan, dan tetap memerlukan pengisi daya *balance*.

## Pengisian

Pengisi daya yang tersedia adalah **SkyRC T6X80** (1–6S, daya pengisian maksimum
80 W; [foto 19](foto/19-pengisi-daya-skyrc.png)), dipakai bersama papan paralel
Power Genius dan SkyRC *multi balance board*.

- Tegangan penuh 6S = 6 × 4,2 V = 25,2 V. Mengisi satu baterai 1200 mAh pada 1C
  (1,2 A) butuh sekitar 25,2 × 1,2 ≈ 30 W.
- Batas 80 W setara arus total sekitar 80 / 25,2 ≈ 3,2 A, sehingga pengisian paralel
  pada 1C **paling banyak 2 baterai sekaligus** (2 × 30 W ≈ 60 W). Tiga baterai sekaligus
  (≈ 91 W) harus diturunkan arusnya di bawah 1C.
- Dengan 6 baterai 6S, pengisian penuh berlangsung **sekitar tiga putaran** pengisian.
  Ini perlu diperhitungkan saat menjadwalkan sesi uji kawanan (Fase 4).
