# KP02 — Firmware FC: ArduPilot racikan lewat Custom Firmware Builder

**Tanggal:** 2026-09-16 · **Status:** diputuskan, belum dieksekusi

## Masalah

Kamera atas hanya berguna bila *flight controller* mau menerima posisi dari luar.
Papan yang tersedia adalah **SpeedyBee F405 Mini** (STM32F405, flash 1 MB).

Daftar fitur resmi build stabil ArduPilot untuk papan ini
(`firmware.ardupilot.org/Copter/stable/SpeedyBeeF405Mini/features.txt`):

```
!EK3_FEATURE_EXTERNAL_NAV     DISABLED   ← navigasi eksternal EKF3
!HAL_VISUALODOM_ENABLED       DISABLED   ← odometri visual
!AP_BEACON_ENABLED            DISABLED   ← masukan beacon (jalur UWB)
!HAL_NAVEKF2_AVAILABLE        DISABLED
!AP_OPTICALFLOW_ENABLED       DISABLED
```

Dokumentasi ArduPilot menyatakan navigasi non-GPS "requires a board with more
than 1MB of flash" dan "only supported by EKF3 (not EKF2)".

**Akibatnya:** dengan firmware bawaan, papan ini tidak dapat menerima
`VISION_POSITION_ESTIMATE` dari kamera atas — maupun masukan UWB lewat driver
beacon. Ini keterbatasan flash papan, bukan soal pilihan sensor.

## Opsi yang dipertimbangkan

| Jalan | Biaya | Risiko |
|---|---|---|
| **A. ArduPilot racikan** | Rp0 | belum pasti muat 1 MB |
| B. Ganti FC ke kelas H7 (≥2 MB) | 5 × papan baru, melebihi RAB Rp2,75 jt | rendah |
| C. Kalang posisi dipindah ke ESP32-S3 | Rp0 | EKF & kontrol posisi ditulis sendiri; beban XIAO ESP32-S3 berat |

## Keputusan

**Jalan A — ArduPilot racikan**, dibangun lewat **ArduPilot Custom Firmware
Builder** (<https://custom.ardupilot.org>).

Layanan ini dibuat persis untuk masalah ini. Dari dokumentasi ArduPilot: *"Since
all 1MB flash sized boards now have feature restrictions to allow the code to
fit, this will give a path to enable a user to select which features will or will
not be included, giving some flexibility to users of 1MB autopilots."*

Artinya **tidak perlu menyiapkan toolchain ARM atau waf** — cukup lewat web.

## Cara eksekusi

1. Buka <https://custom.ardupilot.org> → **Add a build**
2. Pilih berurutan: **Copter** → versi → board **SpeedyBeeF405Mini**
3. **Aktifkan:** `EK3_FEATURE_EXTERNAL_NAV` (dan `HAL_VISUALODOM_ENABLED` bila
   dibutuhkan). Dependensi ikut tercentang otomatis.
4. **Matikan** fitur tak terpakai agar muat 1 MB. Kandidat pertama: seluruh jenis
   rangefinder yang tidak dipakai, mount/gimbal, kamera, OSD, protokol telemetri
   yang tidak dipakai. Halaman dokumentasi menyediakan tabel dampak ukuran tiap
   fitur dalam byte — pakai itu untuk memilih.
5. **Generate** → tunggu log build → unduh `.apj`
6. Flash lewat Mission Planner → **Load custom firmware**

⚠️ Dokumentasi memperingatkan: *"It is possible to select a set of features that
will not fit on a board which will cause the build will fail."* Kalau gagal,
matikan lebih banyak fitur dan ulangi — ini iterasi murah, bukan kegagalan jalan A.

## Kalau jalan A ternyata buntu

Jatuh ke **jalan C** (kalang posisi di ESP32-S3), bukan jalan B — karena B
menuntut belanja 5 papan yang melebihi seluruh RAB.

## Konsekuensi yang harus dicatat di naskah

- Firmware yang dipakai **bukan rilis resmi**, melainkan build dengan fitur
  terpilih. Ini wajib disebut di BAB Metodologi beserta daftar fitur yang
  diaktifkan/dimatikan, supaya orang lain dapat mereproduksi.
- Simpan berkas `.apj` dan tangkapan layar pilihan fiturnya sebagai lampiran.

## Terkait

[[KP01-lokalisasi-apriltag]] · `docs/lab/analisis-kelayakan.md` bagian 6
