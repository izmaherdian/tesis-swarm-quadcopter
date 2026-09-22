# Ruang Uji dan Arena

> Diperbarui 2026-09-18. Ringkasan yang **berlaku** dari analisis kelayakan
> 2026-09-16 ([arsip](../arsip/analisis-kelayakan-2026-09-16.md)), setelah koreksi
> bentuk koridor dan pergantian kamera. Angka geometri yang dipakai gambar dan tabel
> naskah ada di [`tulisan/gambar/parameter.py`](../../tulisan/gambar/parameter.py);
> bila berbeda dengan berkas ini, `parameter.py` yang benar.
>
> Dipakai proposal Bab III pada subbab "Kondisi Ruang Pengujian", "Penentuan Jumlah
> Kamera dan Ukuran Penanda", dan "Rancangan Arena Uji".

## 1. Ruangan

Koridor PTIO ITB (Gedung Pusat Antar Universitas lantai 8) berbentuk **huruf T** dan juga
dipakai sebagai area lalu lintas dan pelatihan. Pengujian **hanya memakai bagian lurus**
koridor, tanpa persimpangan T (konfirmasi penulis 2026-09-17). Ukuran diukur langsung
dengan galat sekitar ±5 cm ([denah, foto 06](foto/06-sketsa-denah-ruangan.png)).

| Besaran | Nilai | Konsekuensi |
|---|---|---|
| Tinggi plafon | **300 cm** | membatasi liputan kamera atas |
| Lebar bersih bagian lurus | **270 cm** | membatasi bentang formasi |
| Panjang bagian lurus | 720 cm (sisi dalam) – 960 cm (sisi luar) | segmen uji dipakai 7,20 m |
| Kolom di dalam area | 4 buah, 45–60 cm | satu kolom (60 × 79 cm) dipakai sebagai sisi celah |
| Plafon | gipsum pada rangka-T, ubin 60 × 60 cm | dudukan kamera mencantol ke rel rangka; hindari ubin berisi AC kaset, lampu, *sprinkler*, detektor asap |
| Pencahayaan | TL *troffer*, *downlight* hangat, jendela besar, kaca *clerestory* | *auto-exposure* dan *auto-white-balance* kamera **dikunci manual** saat merekam |
| Lantai | ubin besar abu gelap, memantul | kontras baik untuk penanda terang; nat ubin menandai posisi dus antarsesi; waspadai pantulan lampu |
| Status | dapat dipakai eksklusif dengan penjadwalan | perabot dapat disingkirkan saat uji |

**Perabot sehari-hari** (dari [video](video/00-video-ruangan.mp4)): deretan sofa di satu
dinding, *roll-up banner*, bangku kerja, kipas industri beroda, kipas berdiri, pintu kayu
yang membuka ke dalam area, dan orang yang lalu lalang. Dengan sofa di tempatnya lebar
bersih tinggal sekitar 180 cm, sehingga formasi V terskala tidak muat dan pemicu ERC
tidak sah. **Sofa dan banner wajib disingkirkan** saat sesi uji, dan pengelola mengizinkannya
(konfirmasi penulis 2026-09-22); pintu dan lalu lintas orang diatur lewat penjadwalan.

**Angin:** kipas tidak dipakai. Uji gangguan angin dibatasi pada simulasi.

## 2. Arena uji

Denah: [`tulisan/proposal/figures/arena.pdf`](../../tulisan/proposal/figures/arena.pdf),
dibuat oleh `tulisan/gambar/gbr_arena.py` (`make gambar`).

| Besaran | Nilai | Catatan |
|---|---|---|
| Segmen uji | 7,20 m × 2,70 m | diliput dua kamera |
| Faktor skala formasi V | **k = 0,9** | maksimum yang muat k ≤ 0,925 (2k + 0,25 + 0,60 ≤ 2,70) |
| Bentang lateral formasi | 2,05 m | ruang bebas 32,5 cm tiap sisi |
| Celah | **0,90 m** | ruang bebas 32,5 cm tiap sisi saat mengekor |
| Sisi celah | kolom bangunan 0,60 × 0,79 m di satu sisi, dus kardus sedalam 1,01 m di sisi seberang | kolom permanen, jadi geometri dapat diulang tanpa ukur ulang |
| Panjang kanal | 1,80 m | kolom 60 cm + perpanjangan dus 60 cm tiap sisi |
| Dus | **32** × kardus polos 60 × 40 × 40 cm, dua baris (kedalaman 0,60 + 0,40 = 1,00 m) × empat lapis (tinggi 1,60 m) | 8 dus per lapis; kedalaman 1,00 m memberi celah 0,91 m, masih dalam galat ukur ±5 cm terhadap rancangan 0,90 m ([survei harga](4-survei-harga.md)) |
| Ambang mengekor | αR = 8 × 0,125 m = **1,0 m** | celah 0,90 m memicu mengekor, koridor 2,70 m mempertahankan formasi |

### Perbandingan dengan simulasi

| Besaran | Simulasi | Arena |
|---|---|---|
| Diameter agen | 0,40 m | 0,25 m |
| Bentang lateral formasi | 2,40 m | 2,05 m |
| Lebar celah | 1,00 m | 0,90 m |
| Panjang bagian sempit | 5,00 m | 1,80 m |
| Rasio bentang / celah | 2,40 | 2,28 |
| Rasio celah / diameter agen | 2,50 | 3,60 |

Dua perbedaan ini **wajib dinyatakan** saat membandingkan hasil fisik dengan simulasi.
Rasio celah terhadap agen di arena lebih longgar, dan fase mengekor lebih singkat. Untuk
yang kedua, simulator diberi skema baru yang meniru arena (Fase 1), bukan arena yang
dipaksa meniru simulasi.

## 3. Kamera di plafon

Kamera dan alasannya: [KP03](../04-keputusan/KP03-kamera-elp-lensa-2-1mm.md).

| Besaran | Nilai |
|---|---|
| Ketinggian terbang | **1,3 m**; tinggi wahana 0,08 m; tiang penanda 0,07 m |
| Jarak kamera ke bidang penanda | 1,55 m |
| Posisi kamera | K1 di 2,12 m dan K2 di 5,08 m dari awal segmen, di tengah lebar koridor |
| Liputan satu kamera (lubang jarum) | 4,23 × 3,18 m, 1,62 mm/piksel |
| Tumpang tindih dua kamera | 1,27 m |
| Penanda AprilTag 12 cm | 73 piksel di sumbu optik (acuan > 70 piksel, DeGol dkk. 2017) |
| Batas pesimistis (proyeksi ekuidistan) | ±42 piksel radial di tepi koridor sejajar kamera, ±26 piksel di ujung segmen |

Nilai lubang jarum hanya berlaku dekat sumbu optik karena lensa berdistorsi tong (ELP
menyebut HFOV 150°, lubang jarum 107,6°). Kepadatan piksel sebenarnya **diukur saat
kalibrasi Fase 2** ([tugas penulis A](5-tugas-penulis.md)).

## 4. Yang masih terbuka

- [ ] Titik cantol kamera pada rel plafon di sekitar 2,12 m dan 5,08 m yang bebas dari
  AC kaset, lampu, dan *sprinkler*. Diperiksa saat pemasangan kamera pertama.
- [x] Jumlah dus dihitung ulang 2026-09-18 menjadi **32** (8 per lapis × 4 lapis). Yang perlu
  dipastikan saat menyusun arena adalah kestabilan tumpukan terhadap hembusan propeler;
  bila goyah, dus diberi pemberat atau direkatkan.
- [x] Sofa dan banner boleh dipindah tiap sesi (konfirmasi penulis 2026-09-22).
