"""Script pengujian diagram kendali tingkat rendah berukuran proporsional dan sangat jelas (Iterasi 7)."""
import os, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif", "serif"],
    "mathtext.fontset": "stix",
    "figure.autolayout": False,
})

fig, ax = plt.subplots(figsize=(15.6, 9.0), dpi=300)
ax.set_xlim(-2.4, 29.8)
ax.set_ylim(-5.2, 9.4)
ax.axis("off")

# Helper kotak dengan ukuran proporsional dan teks tidak meluber
def box(x, y, w, h, title="", subtitle="", text="", fc="white", ec="#1e293b", lw=1.3,
        fs_title=11.0, fs_sub=9.8, fs_text=9.5, zorder=3):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=ec, lw=lw, zorder=zorder, joinstyle="round"))
    cx = x + w/2
    
    if title and subtitle and text:
        ax.text(cx, y + h - 0.28, title, ha="center", va="top", fontsize=fs_title,
                fontweight="bold", color="#0f172a", zorder=zorder+1, linespacing=1.15)
        ax.text(cx, y + h - 0.74, subtitle, ha="center", va="top", fontsize=fs_sub,
                color="#334155", zorder=zorder+1)
        ax.text(cx, y + 0.40, text, ha="center", va="center", fontsize=fs_text,
                color="#0f172a", zorder=zorder+1, linespacing=1.2)
    elif title and subtitle:
        ax.text(cx, y + h/2 + 0.26, title, ha="center", va="center", fontsize=fs_title,
                fontweight="bold", color="#0f172a", zorder=zorder+1, linespacing=1.15)
        ax.text(cx, y + h/2 - 0.28, subtitle, ha="center", va="center", fontsize=fs_sub,
                color="#334155", zorder=zorder+1)
    elif title and text:
        ax.text(cx, y + h - 0.30, title, ha="center", va="top", fontsize=fs_title,
                fontweight="bold", color="#0f172a", zorder=zorder+1, linespacing=1.15)
        ax.text(cx, y + (h - 0.45)/2, text, ha="center", va="center", fontsize=fs_text,
                color="#0f172a", zorder=zorder+1, linespacing=1.2)
    elif title:
        ax.text(cx, y + h/2, title, ha="center", va="center", fontsize=fs_title,
                fontweight="bold", color="#0f172a", zorder=zorder+1, linespacing=1.15)
    return dict(x=x, y=y, w=w, h=h, cx=cx, cy=y+h/2,
                top=(cx, y+h), bottom=(cx, y),
                left=(x, y+h/2), right=(x+w, y+h/2))

def circle_sum(cx, cy, r=0.40, plus_top=False, zorder=4):
    ax.add_patch(Circle((cx, cy), r, fc="white", ec="#0f172a", lw=1.4, zorder=zorder))
    ax.text(cx, cy, "+", ha="center", va="center", fontsize=14, fontweight="bold", zorder=zorder+1)
    ax.text(cx, cy - r - 0.22, "$-$", ha="center", va="center", fontsize=13, fontweight="bold", color="#b91c1c", zorder=zorder+1)
    if plus_top:
        ax.text(cx, cy + r + 0.22, "$+$", ha="center", va="center", fontsize=13, fontweight="bold", color="#15803d", zorder=zorder+1)
    return dict(cx=cx, cy=cy, r=r,
                top=(cx, cy+r), bottom=(cx, cy-r),
                left=(cx-r, cy), right=(cx+r, cy))

def arrow(p1, p2, label="", label_pos=0.5, fs=11.0, color="#0f172a", lw=1.3, ls="-",
          ha="center", va="bottom", dx=0.0, dy=0.12, zorder=3):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=12.0,
                                 color=color, lw=lw, linestyle=ls, shrinkA=0, shrinkB=0, zorder=zorder))
    if label:
        lx = p1[0] + (p2[0] - p1[0]) * label_pos + dx
        ly = p1[1] + (p2[1] - p1[1]) * label_pos + dy
        ax.text(lx, ly, label, ha=ha, va=va, fontsize=fs, color=color, zorder=zorder+2,
                bbox=dict(fc="white", ec="none", pad=1.5))

# -------------------------------------------------------------
# 1. KONTAINER UTAMA
# -------------------------------------------------------------
# FC SpeedyBee F405 Mini
ax.add_patch(Rectangle((2.4, -4.9), 18.2, 14.0, fc="#f8faff", ec="#2563eb", lw=1.5, ls="--", zorder=1, joinstyle="round"))
ax.text(2.8, 8.75, "Hardware Flight Controller SpeedyBee F405 Mini (Firmware ArduPilot Copter)",
        fontsize=12.5, fontweight="bold", color="#1d4ed8", va="top", zorder=2)

# Companion Computer ESP32-S3
ax.add_patch(Rectangle((-2.2, -2.2), 4.2, 11.3, fc="#fff7ed", ec="#ea580c", lw=1.5, zorder=1, joinstyle="round"))
ax.text(-0.1, 8.75, "Companion Computer\n(XIAO ESP32-S3)", ha="center", va="top",
        fontsize=11.5, fontweight="bold", color="#c2410c", zorder=2, linespacing=1.2)
ax.text(-0.1, 7.85, "Serial MAVLink\n(115200 bps)", ha="center", va="top",
        fontsize=9.2, color="#64748b", zorder=2, linespacing=1.15)

# Aktuator Quadcopter
ax.add_patch(Rectangle((21.3, 0.2), 8.2, 4.0, fc="#f0fdf4", ec="#16a34a", lw=1.4, zorder=1, joinstyle="round"))
ax.text(25.4, 3.85, "Aktuator Quadcopter", ha="center", va="top",
        fontsize=12.0, fontweight="bold", color="#15803d", zorder=2)

# -------------------------------------------------------------
# 2. TIER 1: KALANG TRANSLASI (y = 4.8)
# -------------------------------------------------------------
y_t1 = 4.8

pref_pt = (2.0, y_t1)
vref_pt = (2.0, 6.1)
psiref_pt = (2.0, 7.0)

ax.text(-0.1, y_t1, r"$\mathbf{p}_{\mathrm{ref}}$", ha="center", va="center", fontsize=12.5, fontweight="bold", color="#0f172a")
ax.text(-0.1, 6.1, r"$\mathbf{v}_{\mathrm{ref}}$", ha="center", va="center", fontsize=12.5, fontweight="bold", color="#0f172a")
ax.text(-0.1, 7.0, r"$\psi_{\mathrm{ref}}$", ha="center", va="center", fontsize=12.5, fontweight="bold", color="#0f172a")

sum_p = circle_sum(3.7, y_t1)
p_pos = box(5.1, y_t1 - 0.70, 2.7, 1.4, title="Pengendali\nPosisi", subtitle=r"P ($K_p^{\mathrm{pos}}$)",
            fs_title=11.0, fs_sub=10.2)

sum_v = circle_sum(9.4, y_t1, plus_top=True)
p_vel = box(10.6, y_t1 - 0.70, 2.9, 1.4, title="Pengendali\nKecepatan", subtitle=r"PID ($K_{p,i,d}^{\mathrm{vel}}$)",
            fs_title=11.0, fs_sub=10.2)

p_conv = box(14.9, y_t1 - 0.95, 5.0, 1.9,
             title="Konversi Akselerasi",
             subtitle="ke Sikap & Gaya Dorong",
             text=r"$T = m(g + a_z)$" + "\n" + r"$\mathbf{q}_{\mathrm{des}} = \mathcal{F}(\mathbf{a}_{\mathrm{cmd}}, \psi_{\mathrm{ref}})$",
             fc="#eff6ff", ec="#3b82f6", fs_title=11.0, fs_sub=9.8, fs_text=10.2)

# Arrows Tier 1
arrow(pref_pt, sum_p["left"])
arrow(sum_p["right"], p_pos["left"], r"$\mathbf{e}_p$", fs=11.5)
arrow(p_pos["right"], sum_v["left"], r"$\mathbf{v}_{\mathrm{cmd}}$", fs=11.5)
arrow(sum_v["right"], p_vel["left"], r"$\mathbf{e}_v$", fs=11.5)
arrow(p_vel["right"], p_conv["left"], r"$\mathbf{a}_{\mathrm{cmd}}$", fs=11.5)

# Feedforward v_ref (lewat atas pada y = 6.1)
ax.plot([vref_pt[0], 2.1, 2.1, sum_v["top"][0], sum_v["top"][0]],
        [vref_pt[1], vref_pt[1], 6.1, 6.1, sum_v["top"][1]],
        color="#0f172a", lw=1.3, zorder=3)
ax.add_patch(FancyArrowPatch((sum_v["top"][0], sum_v["top"][1]+0.2), sum_v["top"],
                             arrowstyle="-|>", mutation_scale=12.0, color="#0f172a", lw=1.3, zorder=3))
ax.text(5.8, 6.25, r"$\mathbf{v}_{\mathrm{ref}}$ (umpan-maju kecepatan)", ha="center", va="bottom", fontsize=10.0,
        bbox=dict(fc="white", ec="none", pad=1.5))

# psi_ref to conv (lewat atas pada y = 7.0)
ax.plot([psiref_pt[0], 1.9, 1.9, p_conv["cx"], p_conv["cx"]],
        [psiref_pt[1], psiref_pt[1], 7.0, 7.0, p_conv["top"][1]],
        color="#0f172a", lw=1.3, zorder=3)
ax.add_patch(FancyArrowPatch((p_conv["cx"], p_conv["top"][1]+0.2), p_conv["top"],
                             arrowstyle="-|>", mutation_scale=12.0, color="#0f172a", lw=1.3, zorder=3))
ax.text(10.5, 7.15, r"$\psi_{\mathrm{ref}}$ (sudut yaw target)", ha="center", va="bottom", fontsize=10.0,
        bbox=dict(fc="white", ec="none", pad=1.5))

# -------------------------------------------------------------
# 3. TIER 2: KALANG ROTASI & AKTUASI (y = 1.6)
# -------------------------------------------------------------
y_t2 = 1.6

psidot_pt = (2.0, 2.3)
ax.text(-0.1, 2.3, r"$\dot{\psi}_{\mathrm{ref}}$", ha="center", va="center", fontsize=12.5, fontweight="bold", color="#0f172a")

sum_q = circle_sum(3.7, y_t2)
p_att = box(5.1, y_t2 - 0.70, 2.7, 1.4, title="Pengendali\nSikap", subtitle=r"P ($K_p^{\mathrm{att}}$)",
            fs_title=11.0, fs_sub=10.2)

sum_w = circle_sum(9.4, y_t2, plus_top=True)
p_rate = box(10.6, y_t2 - 0.70, 2.9, 1.4, title="Pengendali\nLaju Sudut", subtitle=r"PID ($K_{p,i,d}^{\mathrm{rate}}$)",
             fs_title=11.0, fs_sub=10.2)

p_mix = box(14.6, y_t2 - 0.70, 2.1, 1.4, title="Mixer\nMotor", subtitle="(Quad-X)",
            fc="#eff6ff", ec="#3b82f6", fs_title=10.8, fs_sub=9.8)
p_dshot = box(17.9, y_t2 - 0.70, 2.4, 1.4, title="DShot300", subtitle="(DMA Timer)",
              fc="#f8fafc", ec="#64748b", fs_title=10.5, fs_sub=9.5)

p_esc = box(21.7, y_t2 - 0.70, 2.8, 1.4, title="ESC 4-in-1", subtitle="BLS 35A",
            fs_title=10.8, fs_sub=9.5)
p_mot = box(25.9, y_t2 - 0.70, 2.8, 1.4, title="Motor BLDC", subtitle="4× 2006 1950KV",
            fs_title=10.8, fs_sub=9.2)

# Signals from Conv to Tier 2:
# 1. q_des to sum_q (turun dari conv, belok di y = 3.35, turun di x = 3.1 langsung ke sum_q)
ax.plot([p_conv["left"][0] + 0.6, p_conv["left"][0] + 0.6, 3.1, 3.1, sum_q["left"][0]-0.15, sum_q["left"][0]],
        [p_conv["bottom"][1], 3.35, 3.35, y_t2, y_t2, y_t2],
        color="#0f172a", lw=1.3, zorder=3)
ax.add_patch(FancyArrowPatch((sum_q["left"][0]-0.2, y_t2), sum_q["left"],
                             arrowstyle="-|>", mutation_scale=12.0, color="#0f172a", lw=1.3, zorder=3))
ax.text(8.0, 3.50, r"$\mathbf{q}_{\mathrm{des}}$ (orientasi target)", ha="center", va="bottom", fontsize=10.2,
        bbox=dict(fc="white", ec="none", pad=1.5))

# 2. Thrust T to mixer
ax.plot([p_conv["cx"] + 0.4, p_conv["cx"] + 0.4, p_mix["cx"], p_mix["cx"]],
        [p_conv["bottom"][1], 2.80, 2.80, p_mix["top"][1]],
        color="#0f172a", lw=1.3, zorder=3)
ax.add_patch(FancyArrowPatch((p_mix["cx"], p_mix["top"][1]+0.2), p_mix["top"],
                             arrowstyle="-|>", mutation_scale=12.0, color="#0f172a", lw=1.3, zorder=3))
ax.text(p_mix["cx"] + 0.25, 2.90, r"Gaya Dorong $T$", ha="left", va="bottom", fontsize=10.0,
        bbox=dict(fc="white", ec="none", pad=1.5))

# Arrows Tier 2
arrow(sum_q["right"], p_att["left"], r"$\mathbf{e}_q$", fs=11.5)
arrow(p_att["right"], sum_w["left"], r"$\boldsymbol{\omega}_{\mathrm{des}}$", label_pos=0.42, fs=11.5)
arrow(sum_w["right"], p_rate["left"], r"$\mathbf{e}_\omega$", fs=11.5)
arrow(p_rate["right"], p_mix["left"], r"$\boldsymbol{\tau}$", fs=11.5)
arrow(p_mix["right"], p_dshot["left"], "PWM", fs=9.5)
arrow(p_dshot["right"], p_esc["left"], "DShot", label_pos=0.45, fs=10.2, color="#1d4ed8", lw=1.4)
arrow(p_esc["right"], p_mot["left"], "3-Fase", fs=9.5)

# Feedforward psidot_ref (lewat y = 2.3)
ax.plot([psidot_pt[0], 2.2, 2.2, sum_w["cx"], sum_w["cx"]],
        [psidot_pt[1], psidot_pt[1], 2.3, 2.3, sum_w["top"][1]],
        color="#0f172a", lw=1.3, zorder=3)
ax.add_patch(FancyArrowPatch((sum_w["cx"], sum_w["top"][1]+0.2), sum_w["top"],
                             arrowstyle="-|>", mutation_scale=12.0, color="#0f172a", lw=1.3, zorder=3))
ax.text(5.8, 2.40, r"$\dot{\psi}_{\mathrm{ref}}$ (umpan-maju laju yaw)", ha="center", va="bottom", fontsize=10.0,
        bbox=dict(fc="white", ec="none", pad=1.5))

# -------------------------------------------------------------
# 4. TIER 3: STATE ESTIMATOR (EKF3) & SENSOR
# -------------------------------------------------------------
# p_extnav width 3.6 (dari x=4.8 ke 8.4) agar bebas dari garis v_hat di x=8.85!
p_extnav = box(4.8, -2.0, 3.6, 1.4, title="Navigasi Eksternal",
               subtitle="AprilTag Kamera (60 Hz)", fc="#f0fdfa", ec="#0d9488", fs_title=10.8, fs_sub=9.5)
p_imu = box(12.5, -2.0, 6.4, 1.4, title="Sensor IMU Onboard",
            subtitle="ICM-42688P (1--8 kHz)", fc="#f0fdfa", ec="#0d9488", fs_title=11.0, fs_sub=10.0)

p_ekf = box(3.2, -4.6, 16.2, 1.8, title="ArduPilot EKF3 State Estimator (STM32F405, 400 Hz)",
            text=r"Fusi Multi-Tingkat Menghasilkan Estimasi:" + "\n" +
                 r"Pose 3D ($\hat{\mathbf{p}}, \hat{\mathbf{q}}$), Kecepatan Linear ($\hat{\mathbf{v}}$), dan Laju Sudut ($\hat{\boldsymbol{\omega}}$)",
            fc="#ccfbf1", ec="#0f766e", fs_title=12.0, fs_text=10.8, lw=1.5)

# Sensors to EKF3
arrow(p_extnav["bottom"], (p_extnav["cx"], p_ekf["top"][1]), color="#0f766e", lw=1.4)
arrow(p_imu["bottom"], (p_imu["cx"], p_ekf["top"][1]), color="#0f766e", lw=1.4)

# MAVLink vision pose from ESP32
ax.text(-0.1, -1.30, "Paket Vision\nPose", ha="center", va="center", fontsize=11.0, color="#c2410c", fontweight="bold")
arrow((2.0, -1.30), p_extnav["left"], "MAVLink", fs=10.0, color="#ea580c", ls="--", lw=1.3)

# -------------------------------------------------------------
# 5. JALUR UMPAN BALIK EKF3 KE KOMPARATOR
# -------------------------------------------------------------
# 1. p_hat ke sum_p (naik di x = 2.7, belok ke sum_p)
ax.plot([2.7, 2.7, sum_p["cx"], sum_p["cx"]],
        [p_ekf["top"][1], 3.9, 3.9, sum_p["bottom"][1]],
        color="#0f766e", lw=1.3, zorder=3)
ax.add_patch(FancyArrowPatch((sum_p["cx"], sum_p["bottom"][1]-0.2), sum_p["bottom"],
                             arrowstyle="-|>", mutation_scale=12.0, color="#0f766e", lw=1.3, zorder=3))
ax.text(2.55, 2.5, r"$\hat{\mathbf{p}}$", ha="right", va="center", fontsize=12.5, color="#0f766e",
        bbox=dict(fc="white", ec="none", pad=1.5))

# 2. q_hat ke sum_q (naik vertikal di x = sum_q["cx"])
ax.plot([sum_q["cx"], sum_q["cx"]],
        [p_ekf["top"][1], sum_q["bottom"][1]],
        color="#0f766e", lw=1.3, zorder=3)
ax.add_patch(FancyArrowPatch((sum_q["cx"], sum_q["bottom"][1]-0.2), sum_q["bottom"],
                             arrowstyle="-|>", mutation_scale=12.0, color="#0f766e", lw=1.3, zorder=3))
ax.text(sum_q["cx"] + 0.18, 0.45, r"$\hat{\mathbf{q}}$", ha="left", va="center", fontsize=12.5, color="#0f766e",
        bbox=dict(fc="white", ec="none", pad=1.5))

# 3. v_hat ke sum_v (naik di x = 8.85, belok ke sum_v)
ax.plot([8.85, 8.85, sum_v["cx"], sum_v["cx"]],
        [p_ekf["top"][1], 3.9, 3.9, sum_v["bottom"][1]],
        color="#0f766e", lw=1.3, zorder=3)
ax.add_patch(FancyArrowPatch((sum_v["cx"], sum_v["bottom"][1]-0.2), sum_v["bottom"],
                             arrowstyle="-|>", mutation_scale=12.0, color="#0f766e", lw=1.3, zorder=3))
ax.text(8.70, 2.5, r"$\hat{\mathbf{v}}$", ha="right", va="center", fontsize=12.5, color="#0f766e",
        bbox=dict(fc="white", ec="none", pad=1.5))

# 4. omega_hat ke sum_w (naik vertikal di x = sum_w["cx"])
ax.plot([sum_w["cx"], sum_w["cx"]],
        [p_ekf["top"][1], sum_w["bottom"][1]],
        color="#0f766e", lw=1.3, zorder=3)
ax.add_patch(FancyArrowPatch((sum_w["cx"], sum_w["bottom"][1]-0.2), sum_w["bottom"],
                             arrowstyle="-|>", mutation_scale=12.0, color="#0f766e", lw=1.3, zorder=3))
ax.text(sum_w["cx"] + 0.18, 0.45, r"$\hat{\boldsymbol{\omega}}$", ha="left", va="center", fontsize=12.5, color="#0f766e",
        bbox=dict(fc="white", ec="none", pad=1.5))

out_png = "scratch/test_pengendali.png"
fig.savefig(out_png, dpi=300, bbox_inches="tight", facecolor="white")
print("Saved to", out_png)
