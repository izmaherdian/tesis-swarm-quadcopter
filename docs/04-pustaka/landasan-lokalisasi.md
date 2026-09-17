> **Catatan 2026-09-17.** Dulu bernama `docs/pustaka/E01-landasan-lokalisasi.md`. Awalan
> "E01" merujuk eksperimen sapuan sensitivitas lokalisasi yang **tidak masuk proposal yang
> berlaku**, sehingga dilepas dari nama berkas. Status verifikasi di bawah adalah keadaan
> 2026-09-16. Rujukan yang akhirnya dipakai naskah (mis. Bultmann dkk. 2023, tiga makalah
> AprilTag) sudah ada di `tulisan/common/references.bib`, dan kuartil yang berlaku ada di
> [`kuartil-jurnal.md`](kuartil-jurnal.md).

# Landasan Pustaka — Lokalisasi Indoor & Sensitivitas Formasi

> Dibuat: 2026-09-16 · Untuk: menambal sitasi Subbab 2.4 proposal + mengunci
> rentang sapuan eksperimen E01.
>
> **Aturan mutu:** klaim angka wajib 2021–2026, jurnal Q1/Q2 atau konferensi
> robotika papan atas (ICRA/IROS/RA-L/T-RO). Makalah asal metode dikutip apa
> adanya berapa pun umurnya, **tapi hanya untuk metodenya, bukan angkanya.**

## Status verifikasi — baca ini dulu

Verifikasi dilakukan dengan mengambil langsung halaman arXiv/penerbit dan
membaca metadata apa adanya. **Belum ada satu pun entri yang dimasukkan ke
`references.bib`** sampai statusnya hijau.

| Status | Arti |
|---|---|
| ✅ TERVERIFIKASI | Judul, penulis, tahun, venue dibaca langsung dari halaman resmi |
| ⚠️ SEBAGIAN | Sebagian metadata terbaca, ada yang masih bentrok atau kosong |
| ❌ BELUM | Hanya muncul di hasil pencarian; metadata belum dibuka sama sekali |

**Kendala yang perlu diketahui:** DBLP tidak dapat dijangkau dari sesi ini
(timeout dan `ECONNRESET` berulang), sehingga pemeriksaan silang DBLP yang
biasanya dilakukan `/phd-skills:factcheck` **belum dijalankan**. Kuartil Scimago
juga belum dicek mesin — kolom kuartil di bawah adalah perkiraan berdasarkan
reputasi venue dan **wajib dikonfirmasi manual di scimagojr.com** sebelum
dipakai sebagai pembenaran mutu ke pembimbing.

---

## A. Akurasi lokalisasi berbasis kamera eksternal

| Referensi | Tahun | Venue | Kuartil | Angka yang bisa dikutip | Status |
|---|---|---|---|---|---|
| Bultmann, Memmesheimer, Behnke — *External Camera-based Mobile Robot Pose Estimation for Collaborative Perception with Smart Edge Sensors* | 2023 | **ICRA** | konferensi papan atas | **galat pose < 3 cm dan < 1°**, **tidak mengalami *drift*** seiring waktu, pada lingkungan indoor **± 240 m²** | ✅ |

**Catatan pemakaian.** Ini sumber terkuat yang ditemukan untuk membenarkan klaim
"presisi sentimeter dan bebas *drift*" di Subbab 2.4. Perlu kejujuran saat
mengutip: sistem mereka memakai **beberapa kamera tepi (*smart edge sensors*)
dengan deteksi *keypoint* berbasis jaringan saraf**, bukan satu kamera atas
dengan AprilTag. Jadi angkanya sah sebagai **pembanding kelas sistem lokalisasi
kamera eksternal**, bukan sebagai angka persis yang akan dicapai sistem ini.
Klaim di naskah harus dirumuskan sebagai "sekelas", bukan "sama dengan".

⚠️ **Celah yang masih terbuka:** belum ditemukan sumber 2021–2026 Q1/Q2 yang
melaporkan RMSE posisi untuk **kamera atas + AprilTag pada MAV** secara spesifik.
Kandidat yang muncul tapi belum layak: `YoloTag` (arXiv 2409.02334, 2024 — venue
belum terverifikasi) dan sebuah makalah SSRN 2024 (pracetak, bukan telaah
sejawat — **jangan dipakai**). Pencarian lanjutan diperlukan; lihat bagian
"Pekerjaan tersisa".

---

## B. UWB untuk MAV indoor multi-agen

| Referensi | Tahun | Venue | Kuartil | Kegunaan | Status |
|---|---|---|---|---|---|
| Shalaby, Ahmed, Dahdah, Cossette, Le Ny, Forbes — *MILUV: A Multi-UAV Indoor Localization dataset with UWB and Vision* | 2026 | **Int. J. of Robotics Research** (IJRR), DOI `10.1177/02783649251405898`; pracetak arXiv 2504.14376 | Q1 | Dataset 3 quadcopter, 217 menit terbang, 36 eksperimen, **6 *anchor* UWB statis**, **48 AprilTag**, hingga **12 *transceiver***, kondisi LOS **dan NLOS**, kebenaran dasar Vicon. Kecepatan maksimum **4,418 m/s** | ⚠️ |
| Torrico Morón, Peña Queralta, Westerlund — *Towards Large-Scale Relative Localization in Multi-Robot Systems with Dynamic UWB Role Allocation* | 2022 | arXiv 2203.03893 — **venue terbit belum diketahui** | — | Membahas penjadwalan peran UWB saat jumlah agen bertambah — inti masalah penskalaan TWR multi-tag | ⚠️ |

⚠️ **Konflik metadata pada MILUV:** urutan penulis berbeda antara halaman DOI
IJRR (`Shalaby, Dahdah, Ahmed, …`) dan halaman arXiv (`Shalaby, Ahmed, Dahdah, …`).
**Harus dipastikan dari versi terbit sebelum masuk `references.bib`.**

⚠️ **Angka belum didapat.** Baik akurasi jarak UWB (bias/simpangan baku, LOS vs
NLOS), laju *ranging* per tag, maupun akurasi sumbu vertikal **belum diambil dari
tabel mana pun** — yang terbaca baru abstrak. Angka "10–30 cm" yang saya sebut
dalam diskusi sebelumnya adalah **perkiraan saya, belum bersumber**, dan tidak
boleh masuk naskah maupun jadi batas sapuan E01 sampai ditemukan tabelnya.

---

## C. Sensitivitas kontrol formasi terhadap derau lokalisasi

**Temuan terpenting dari Fase 1 ini.**

| Referensi | Tahun | Venue | Kuartil | Status |
|---|---|---|---|---|
| Walter, Vrba, Bonilla Licea, Hilmer, Saska — *Distributed UAV Formation Control Robust to Relative Pose Measurement Noise* | 2026 | **Robotics and Autonomous Systems**, Vol. 201, art. 105458, DOI `10.1016/j.robot.2026.105458` | Q1/Q2 | ✅ |

Dari abstrak (dikutip apa adanya): metode mereka memungkinkan *Formation-Enforcing
Control* (FEC) berbasis teori kekakuan graf "to interface with a realistic relative
localization system onboard lightweight Unmanned Aerial Vehicles (UAVs)", karena
derau sensor "otherwise causes undesirable oscillations and drifts in sensor-based
formations, and this effect is **not sufficiently addressed in existing FEC
algorithms**".

### Artinya untuk E01

**Jawaban pertanyaan (c): ya, sudah ada.** E01 bukan lahan kosong dan **wajib
memposisikan diri terhadap makalah ini** — kalau tidak, penguji yang mengenal
kelompok Saska (CTU MRS) akan menanyakannya.

Tiga pembeda yang membuat E01 tetap punya alasan berdiri, dan sebaiknya
dinyatakan terang-terangan di BAB IV:

1. **Jenis lokalisasi berbeda.** Mereka menangani derau pengukuran pose
   **relatif** dari sensor *onboard*; penelitian ini memakai posisi **absolut**
   dari kamera atas. Watak galatnya berbeda — galat relatif menumpuk antaragen,
   galat absolut tidak.
2. **Jenis kontrol berbeda.** Mereka memakai FEC berbasis kekakuan graf yang
   mempertahankan **satu bentuk formasi**; ERC justru **berpindah bentuk formasi
   secara diskret** saat terpicu kejadian. Perpindahan diskret inilah yang
   berpotensi rapuh terhadap derau — sebuah *event* bisa terpicu palsu atau
   terlewat, dan itu tidak dibahas mereka.
3. **Jenis pertanyaan berbeda.** Mereka menawarkan **perbaikan hukum kontrol**;
   E01 menghasilkan **anggaran galat** — berapa σ, laju, dan latensi terburuk
   yang masih ditoleransi — untuk memilih perangkat keras. Itu keluaran
   rekayasa, bukan keluaran teori kontrol.

Poin 2 adalah yang paling kuat: **pemicuan kejadian palsu akibat derau
lokalisasi** adalah celah yang belum tersentuh, dan itu tepat berada di jantung
ERC. Layak diangkat jadi rumusan E01.

### Kandidat lain yang belum diperiksa

| Referensi | Tahun | Venue | Status |
|---|---|---|---|
| *Distributed adaptive formation control of multi-agent systems with measurement noises*, DOI `10.1016/j.automatica.2023.110857` | 2023 | **Automatica** (Q1) | ❌ penulis belum diketahui |
| *Distributed formation tracking for multi-UAVs with unknown disturbances under **event-triggered communication*** | 2024 | J. Franklin Institute | ❌ — **relevan khusus**: berbasis kejadian, bersinggungan langsung dengan ERC |
| *Robust control strategy for multi-UAVs system using MPC combined with Kalman-consensus filter and disturbance observer* | 2022/23 | ISA Transactions | ❌ |

---

## D. Makalah asal metode (umur dikecualikan)

Wajib ada supaya AprilTag/ArUco tidak dipakai tanpa menyebut sumbernya. **Semua
masih perlu diverifikasi metadatanya.**

| Metode | Rujukan yang lazim | Status |
|---|---|---|
| AprilTag | Olson, ICRA 2011 | ❌ |
| AprilTag 2 | Wang & Olson, IROS 2016 | ❌ |
| AprilTag 3 | Krogius, Haggenmiller, Olson, IROS 2019 | ❌ |
| ArUco | Garrido-Jurado dkk., Pattern Recognition 2014 | ❌ |
| Perbandingan akurasi AprilTag3 vs ArUco | Kallwies, Forkel, Wuensche, ICRA 2020 | ❌ — **2020, di luar jendela**; hanya boleh untuk perbandingan metode, bukan klaim angka terkini |

---

## Pekerjaan tersisa sebelum bagian ini bisa dipakai

1. **Cari sumber akurasi AprilTag yang layak** (2021–2026, Q1/Q2) — celah
   terbesar. Tanpa ini, klaim "±1–3 cm" di Subbab 2.4 tetap tak bersumber.
2. **Ambil angka UWB dari tabel MILUV** (bukan abstrak): bias dan simpangan baku
   LOS/NLOS, laju *ranging*, akurasi sumbu vertikal.
3. **Selesaikan konflik urutan penulis MILUV** dari versi terbit IJRR.
4. **Verifikasi metadata** semua entri berstatus ❌ dan ⚠️.
5. **Konfirmasi kuartil** tiap jurnal di scimagojr.com, catat di tabel.
6. **Jalankan `/phd-skills:factcheck`** saat jaringan memungkinkan, sekalian
   membereskan 3 entri salah tipe yang sudah diketahui (Kane & Welch ditandai
   `@article`, Gelb ditandai `@inproceedings`).
7. Baru setelah itu: tambal sitasi Subbab 2.4 dan kunci rentang sapuan E01.

## Dampak langsung ke rencana E01

Rentang sapuan **belum bisa dikunci** karena angka UWB belum bersumber. Yang
sudah bisa ditetapkan sekarang:

- Batas bawah σ ≈ **3 cm** punya dasar (Bultmann dkk. 2023, ICRA).
- Batas atas σ **masih perkiraan** — tunggu angka MILUV.
- **Rumusan E01 sebaiknya digeser** agar menonjolkan celah yang belum tersentuh
  Walter dkk.: *pemicuan kejadian palsu pada ERC akibat derau lokalisasi*, bukan
  sekadar "ERC terhadap derau".

---

## E. Publikasi sendiri — landasan langsung tesis ini

Ditemukan di dalam repo simulator (`10.1007_s44444-026-00111-4-citation.ris`,
berkas ekspor sitasi resmi dari penerbit — sumber otoritatif).

> **Herdian, I. A.; Ekawati, E.; Mukhlish, F.; Prabaswara, P.** (2026).
> *Decentralized formation control system design for swarm quadcopters using an
> improved artificial potential field and event-based reconfiguration control.*
> **Journal of King Saud University – Engineering Sciences**, 38(5), 41.
> DOI `10.1007/s44444-026-00111-4` · ISSN 2213-1558 · terbit 4 Juni 2026 ✅

### Angka baseline yang kini BERSUMBER

Diambil langsung dari abstrak resmi — sebelumnya angka-angka ini hanya ada di
README repo, kini punya rujukan yang bisa dikutip di naskah:

| Skenario | Waktu misi | $\overline{RMSE}_{\text{total}}$ | $\overline{\Phi}$ |
|---|---|---|---|
| Celah sempit (ERC) | 59,735 s | 0,692 m | 0,878 |
| Celah sempit + hembusan angin periodik | hampir tak berubah | 0,694 m | 0,925 |

Juga tercatat: IAPF statis **gagal** pada celah sempit, dan perangkap berbentuk U
mengungkap keterbatasan perencana yang murni reaktif.

**Dampak ke E01:** uji regresi mode `PERFECT` sekarang punya acuan terbit, bukan
sekadar angka dari README. Kalau hasil regresi menyimpang dari 59,735 s /
0,692 m, yang meleset adalah kodenya — karena angka itu sudah melewati telaah
sejawat.

### Masalah yang ditemukan di proposal

Sebelum perbaikan ini, proposal **hanya mengutip katalog digilib ITB** untuk
karya ini:

```
@misc{PerancanganSistemKendali}  ← rekaman digilib, tesis Juli 2025, hanya URL
```

dan hanya di **satu tempat** (baris 794, arsitektur perencana tingkat tinggi).
Artikel jurnalnya sama sekali tidak ada di `references.bib`.

**Sudah diperbaiki:** entri jurnal ditambahkan dan disitasi berdampingan dengan
rujukan lama di baris 794. Terbit sebagai rujukan `[35]` di PDF.

### Yang masih perlu keputusan penulis

Penempatan satu sitasi di BAB II saja terasa kurang untuk karya yang menjadi
**fondasi seluruh tesis**. Pertimbangkan menyebutnya juga di:

- **Latar Belakang** — menegaskan bahwa ERC sudah tervalidasi dalam simulasi oleh
  penulis sendiri, sehingga tesis ini berlanjut ke implementasi fisik.
- **Studi Terkait** — memposisikan karya sendiri terhadap Bui dkk. dan Wang dkk.
- **Rumusan Masalah / Kontribusi** — batas kontribusi jadi tegas:
  *makalah = simulasi, tesis = implementasi fisik.* Pembatasan ini justru
  melindungi dari pertanyaan penguji "apa bedanya dengan paper Anda sendiri?"

Penempatan sitasi diri memengaruhi cara kontribusi terbaca, jadi ini keputusan
penulis — bukan sesuatu yang pantas saya putuskan sendiri.

⚠️ **Kuartil JKSUES belum dicek** di Scimago. Perlu dikonfirmasi karena batas
mutu yang ditetapkan adalah Q1/Q2.

---

## F. Entri tambahan untuk revisi besar proposal (2026-09-16)

Verifikasi lewat **CrossRef API** dan laman resmi penulis — DBLP tetap memblokir
akses otomatis (anti-bot "Anubis").

| Referensi | Tahun | Venue | Kuartil | Dipakai untuk | Status |
|---|---|---|---|---|---|
| Olson — *AprilTag: A robust and flexible visual fiducial system* | 2011 | ICRA, hlm. 3400–3407 | konferensi papan atas | asal metode AprilTag | ✅ BibTeX resmi APRIL Robotics Lab |
| Wang & Olson — *AprilTag 2* | 2016 | IROS | konferensi papan atas | asal metode | ✅ idem |
| Krogius, Haggenmiller, Olson — *Flexible Layouts for Fiducial Tags* | 2019 | IROS | konferensi papan atas | asal metode (AprilTag 3) | ✅ idem |
| Garrido-Jurado dkk. — *Automatic generation and detection of highly reliable fiducial markers under occlusion* | 2014 | Pattern Recognition 47(6):2280–2292 | Q1 | asal metode ArUco | ✅ CrossRef |
| Bultmann, Memmesheimer, Behnke — *External Camera-based Mobile Robot Pose Estimation…* | 2023 | ICRA | konferensi papan atas | galat pose < 3 cm dan < 1°, tanpa *drift*, area ±240 m² | ✅ arXiv |
| Zhang dkk. — *An integrated framework for enhancing small AprilTag pose accuracy under long-distance conditions* | 2026 | Pattern Recognition 179:113683 | Q1 | akurasi AprilTag menurun seiring jarak & mengecilnya penanda | ✅ CrossRef |
| **Pedro & Marta — *On the Development of a Sense and Avoid System for Small Fixed-Wing UAV*** | **2025** | **Sensors 25(8):2460** | **Q1/Q2** | resolusi sudut ultrasonik yang buruk; laser beresolusi spasial lebih tinggi | ✅ CrossRef |
| **Kabiri dkk. — *Graph-Based vs. Error State Kalman Filter-Based Fusion…*** | **2024** | **J. Intelligent & Robotic Systems 110(2):87** | **Q2** | penapis Kalman masih jadi acuan untuk pose MAV indoor | ✅ CrossRef |

### Entri lama yang tipenya diperbaiki

| Entri | Sebelum | Sesudah | Sumber verifikasi |
|---|---|---|---|
| Kane & Levinson, *Dynamics: Theory and Applications* (1985) | `@article` | `@book`, McGraw-Hill, ISBN 0-07-037846-0 | Open Library |
| Welch & Bishop, *An Introduction to the Kalman Filter* | `@article` | `@techreport`, TR 95-041, Dept. of CS, UNC Chapel Hill | laman UNC & salinan resmi |
| Gelb (ed.), *Applied Optimal Estimation* (1974) | `@inproceedings` | `@book`, The MIT Press, Cambridge MA | laman MIT Press |

**Hasilnya: peringatan bibtex turun dari 3 menjadi 0.**

⚠️ Masih terbuka: `hoDesignIndoorPositioning2023` tetap yatim (sisa era UWB).
Keputusan dipakai-ulang atau dibuang ada pada penulis. Kuartil semua venue di
atas masih perlu dikonfirmasi manual di scimagojr.com.
