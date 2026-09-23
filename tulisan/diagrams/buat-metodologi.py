"""Bangun ulang halaman Metodologi di proposal-tesis.drawio dengan tata letak ringkas.

Tinggi baris dihitung di sini supaya tata letaknya rapat dan hurufnya tetap besar
saat gambar diperkecil ke lebar teks naskah.
"""
SUMBER = "tulisan/diagrams/proposal-tesis.drawio"
FONT = "fontFamily=Times New Roman;fontSize=14;"

GAYA_KOTAK = f"rounded=0;whiteSpace=wrap;html=1;{FONT}"
GAYA_PUTUSAN = f"rhombus;whiteSpace=wrap;html=1;{FONT}"
GAYA_ELIPS = f"ellipse;whiteSpace=wrap;html=1;{FONT}"
GAYA_FASE = f"swimlane;horizontal=0;whiteSpace=wrap;html=1;startSize=60;dashed=1;fillColor=none;{FONT}"
GAYA_TEPI = f"edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;{FONT}"
GAYA_LABEL = f"edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];{FONT}"

KIRI, KANAN, LEBAR = 118, 358, 202      # dua kolom isi
WADAH_X, WADAH_W = 40, 524              # bingkai fase
H_KOTAK, H_PUTUSAN = 58, 78
JARAK_BARIS, PAD, JARAK_FASE = 16, 12, 12
KORIDOR = 596                           # jalur "tidak" di kanan bingkai

sel, y_baris, wadah = [], {}, []
y = 60                                   # setelah elips Mulai


def susun(nama_fase, judul, baris):
    """Tempatkan satu bingkai fase beserta barisnya, lalu kembalikan tinggi yang terpakai."""
    global y
    atas = y
    y += PAD
    for kunci, tinggi in baris:
        y_baris[kunci] = y
        y += tinggi + JARAK_BARIS
    y = y - JARAK_BARIS + PAD
    wadah.append((nama_fase, judul, atas, y - atas))
    y += JARAK_FASE


susun("f1", "Fase 1&lt;div&gt;Studi dan Desain&lt;/div&gt;", [("b1", H_KOTAK)])
susun("f2", "Fase 2&lt;div&gt;Implementasi Teknologi&lt;/div&gt;", [("b2", H_KOTAK), ("b3", H_KOTAK)])
susun("f3", "Fase 3&lt;div&gt;Pengujian HITL&lt;/div&gt;", [("b4", H_PUTUSAN)])
susun("f4", "Fase 4&lt;div&gt;Uji Terbang Eksperimen&lt;/div&gt;",
      [("b5", H_PUTUSAN), ("b6", H_PUTUSAN), ("b7", H_PUTUSAN)])
susun("f5", "Fase 5&lt;div&gt;Analisis dan Pelaporan&lt;/div&gt;", [("b8", H_KOTAK), ("b9", H_KOTAK)])
TINGGI_TOTAL = y + 52


def kotak(i, x, y_, teks, w=LEBAR, h=H_KOTAK, gaya=GAYA_KOTAK):
    sel.append(f'        <mxCell id="{i}" value="{teks}" style="{gaya}" vertex="1" parent="1">\n'
               f'          <mxGeometry x="{x}" y="{y_}" width="{w}" height="{h}" as="geometry" />\n'
               f'        </mxCell>')


def tepi(i, asal, tujuan, gaya_tambahan="", titik=(), label=None, label_x=-0.4, geser_y=-10):
    arr = ""
    if titik:
        arr = ("\n            <Array as=\"points\">\n"
               + "\n".join(f'              <mxPoint x="{a}" y="{b}" />' for a, b in titik)
               + "\n            </Array>\n          ")
    sel.append(f'        <mxCell id="{i}" style="{GAYA_TEPI}{gaya_tambahan}" edge="1" parent="1" '
               f'source="{asal}" target="{tujuan}">\n'
               f'          <mxGeometry relative="1" as="geometry">{arr}</mxGeometry>\n'
               f'        </mxCell>')
    if label:
        sel.append(f'        <mxCell id="{i}-l" value="{label}" style="{GAYA_LABEL}" vertex="1" '
                   f'connectable="0" parent="{i}">\n'
                   f'          <mxGeometry x="{label_x}" y="0" relative="1" as="geometry">\n'
                   f'            <mxPoint y="{geser_y}" as="offset" />\n'
                   f'          </mxGeometry>\n        </mxCell>')


for nama, judul, atas, tinggi in wadah:
    kotak(nama, WADAH_X, atas, judul, w=WADAH_W, h=tinggi, gaya=GAYA_FASE)

kotak("mulai", 247, 4, "Mulai", w=110, h=44, gaya=GAYA_ELIPS)


def pasang(kunci, teks_kiri, teks_kanan=None, putusan=False):
    y_ = y_baris[kunci]
    if putusan:
        kotak(f"{kunci}k", KIRI, y_ + (H_PUTUSAN - H_KOTAK) // 2, teks_kiri)
        kotak(f"{kunci}n", KANAN, y_, teks_kanan, h=H_PUTUSAN, gaya=GAYA_PUTUSAN)
    else:
        kotak(f"{kunci}k", KIRI, y_, teks_kiri)
        if teks_kanan:
            kotak(f"{kunci}n", KANAN, y_, teks_kanan)


pasang("b1", "Studi Literatur dan Simulasi Arena Berskala", "Desain Arsitektur Lima Quadcopter")
pasang("b2", "Komunikasi Eksternal (UDP Wi-Fi Lokal)", "Komunikasi Internal (&lt;i&gt;Firmware&lt;/i&gt; Racikan, MAVLink)")
pasang("b3", "Lokalisasi Kamera Atas dan Uji Banding Sensor", "Penanaman Logika ERC dan IAPF")
pasang("b4", "Uji HITL pada &lt;i&gt;Companion Computer&lt;/i&gt;", "CPU dan Latensi Aman?", putusan=True)
pasang("b5", "Uji Terbang Tunggal (EKF, Tautan, PID)", "Wahana Tunggal Stabil?", putusan=True)
pasang("b6", "Uji Terbang Tiga Wahana, Mengekor Celah 90 cm", "Tiga Wahana Berhasil?", putusan=True)
pasang("b7", "Uji Terbang Lima Wahana, Prosedur Sama", "Lima Wahana Berhasil?", putusan=True)
pasang("b8", "Ekstraksi &lt;i&gt;Log&lt;/i&gt; Pose, Pemicu ERC, dan Trafik UDP",
       "Analisis RMSE, Φ, Keberhasilan Melintas, dan Beban Komunikasi")
kotak("b9k", 238, y_baris["b9"], "Perbandingan dengan Simulasi dan Penyusunan Tesis")
kotak("selesai", 247, TINGGI_TOTAL - 46, "Selesai", w=110, h=44, gaya=GAYA_ELIPS)

TENGAH_KIRI, TENGAH_KANAN = KIRI + LEBAR // 2, KANAN + LEBAR // 2
ATAS = "entryX=0.5;entryY=0;entryDx=0;entryDy=0;"

tepi("e1", "mulai", "b1k", "exitX=0.5;exitY=1;exitDx=0;exitDy=0;" + ATAS,
     titik=((302, 54), (TENGAH_KIRI, 54)))
tepi("e2", "b1k", "b1n")
tepi("e3", "b1n", "b2n")
tepi("e4", "b2n", "b2k")
tepi("e5", "b2k", "b3k")
tepi("e6", "b3k", "b3n")


def antar(i, dari, ke, label=None):
    """Sambungkan kotak atau putusan di kolom kanan ke kotak kiri baris berikutnya."""
    tepi(i, dari, ke, ATAS, titik=((TENGAH_KANAN, y_antara[i]), (TENGAH_KIRI, y_antara[i])),
         label=label, label_x=-0.55)


y_antara = {
    "e7": y_baris["b4"] - JARAK_FASE // 2 - PAD,
    "e8": y_baris["b5"] - JARAK_FASE // 2 - PAD,
    "e9": y_baris["b6"] - JARAK_BARIS // 2,
    "e10": y_baris["b7"] - JARAK_BARIS // 2,
    "e11": y_baris["b8"] - JARAK_FASE // 2 - PAD,
}
antar("e7", "b3n", "b4k")
tepi("e12", "b4k", "b4n")
antar("e8", "b4n", "b5k", label="Ya")
tepi("e13", "b5k", "b5n")
antar("e9", "b5n", "b6k", label="Ya")
tepi("e14", "b6k", "b6n")
antar("e10", "b6n", "b7k", label="Ya")
tepi("e15", "b7k", "b7n")
antar("e11", "b7n", "b8k", label="Ya")
tepi("e16", "b8k", "b8n")
tepi("e17", "b8n", "b9k", "entryX=1;entryY=0.5;entryDx=0;entryDy=0;",
     titik=((552, y_baris["b9"] + H_KOTAK // 2),))
tepi("e18", "b9k", "selesai", "exitX=0.5;exitY=1;exitDx=0;exitDy=0;" + ATAS,
     titik=((339, TINGGI_TOTAL - 58), (302, TINGGI_TOTAL - 58)))

for n, kunci in enumerate(["b4", "b5", "b6", "b7"], 1):
    tepi(f"t{n}", f"{kunci}n", "b3n",
         "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;",
         titik=((KORIDOR, y_baris[kunci] + H_PUTUSAN // 2),
                (KORIDOR, y_baris["b3"] + H_KOTAK // 2)),
         label="Tidak", label_x=-0.88)

halaman = ('    <diagram name="Metodologi" id="oeeEZdFLL3CIaSeiuWsl">\n'
           '      <mxGraphModel dx="1178" dy="613" grid="1" gridSize="10" guides="1" tooltips="1" '
           'connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" '
           'math="1" shadow="0">\n        <root>\n'
           '        <mxCell id="0" />\n        <mxCell id="1" parent="0" />\n'
           + "\n".join(sel) + "\n        </root>\n      </mxGraphModel>\n    </diagram>")

berkas = open(SUMBER).read()
i = berkas.index('  <diagram name="Metodologi"')
j = berkas.index("  <diagram", i + 10)
open(SUMBER, "w").write(berkas[:i] + halaman + "\n" + berkas[j:])
print(f"halaman Metodologi ditulis ulang, {len(sel)} sel, tinggi {TINGGI_TOTAL} px")
