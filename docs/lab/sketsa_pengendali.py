"""Penyempurnaan posisi bebas tabrakan dan jarak nyaman untuk sketsa_pengendali."""
import os
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

fig, ax = plt.subplots(figsize=(15.8, 9.2), dpi=300)
ax.set_xlim(-2.5, 30.2)
ax.set_ylim(-5.3, 9.5)
ax.axis("off")

def box(x, y, w, h, title="", subtitle="", text="", fc="white", ec="#1e293b", lw=1.6,
        fs_title=13.0, fs_sub=11.5, fs_text=11.5, zorder=3):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=ec, lw=lw, zorder=zorder, joinstyle="round"))
    cx = x + w/2
    cy = y + h/2
    
    if title and subtitle and text:
        ax.text(cx, y + h - 0.26, title, ha="center", va="top", fontsize=fs_title,
                fontweight="bold", color="#0f172a", zorder=zorder+1, linespacing=1.15)
        ax.text(cx, y + h - 0.72, subtitle, ha="center", va="top", fontsize=fs_sub,
                color="#334155", zorder=zorder+1)
        ax.text(cx, y + 0.40, text, ha="center", va="center", fontsize=fs_text,
                color="#0f172a", zorder=zorder+1, linespacing=1.2)
    elif title and subtitle:
        ax.text(cx, cy + 0.28, title, ha="center", va="center", fontsize=fs_title,
                fontweight="bold", color="#0f172a", zorder=zorder+1, linespacing=1.15)
        ax.text(cx, cy - 0.36, subtitle, ha="center", va="center", fontsize=fs_sub,
                color="#334155", zorder=zorder+1)
    elif title and text:
        ax.text(cx, y + h - 0.28, title, ha="center", va="top", fontsize=fs_title,
                fontweight="bold", color="#0f172a", zorder=zorder+1, linespacing=1.15)
        ax.text(cx, y + (h - 0.45)/2, text, ha="center", va="center", fontsize=fs_text,
                color="#0f172a", zorder=zorder+1, linespacing=1.2)
    elif title:
        ax.text(cx, cy, title, ha="center", va="center", fontsize=fs_title,
                fontweight="bold", color="#0f172a", zorder=zorder+1, linespacing=1.15)
    return dict(x=x, y=y, w=w, h=h, cx=cx, cy=cy,
                top=(cx, y+h), bottom=(cx, y),
                left=(x, cy), right=(x+w, cy))

def circle_sum(cx, cy, r=0.45, plus_top=False, zorder=4):
    ax.add_patch(Circle((cx, cy), r, fc="white", ec="#0f172a", lw=1.6, zorder=zorder))
    ax.text(cx, cy, "+", ha="center", va="center", fontsize=16, fontweight="bold", zorder=zorder+1)
    ax.text(cx, cy - r - 0.25, "$-$", ha="center", va="center", fontsize=15, fontweight="bold", color="#b91c1c", zorder=zorder+1)
    if plus_top:
        ax.text(cx, cy + r + 0.25, "$+$", ha="center", va="center", fontsize=15, fontweight="bold", color="#15803d", zorder=zorder+1)
    return dict(cx=cx, cy=cy, r=r,
                top=(cx, cy+r), bottom=(cx, cy-r),
                left=(cx-r, cy), right=(cx+r, cy))

def arrow(p1, p2, label="", label_pos=0.5, fs=13.0, color="#0f172a", lw=1.6, ls="-",
          ha="center", va="bottom", dx=0.0, dy=0.14, zorder=3):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=14.0,
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
ax.add_patch(Rectangle((2.3, -4.9), 18.2, 14.0, fc="#f8faff", ec="#2563eb", lw=1.8, ls="--", zorder=1, joinstyle="round"))
ax.text(3.0, 8.75, "Hardware Flight Controller SpeedyBee F405 Mini (Firmware ArduPilot Copter)",
        fontsize=13.5, fontweight="bold", color="#1d4ed8", va="top", zorder=2)

# Companion Computer ESP32-S3 (width 3.9, from -2.1 to 1.8)
ax.add_patch(Rectangle((-2.1, -2.2), 3.9, 11.3, fc="#fff7ed", ec="#ea580c", lw=1.8, zorder=1, joinstyle="round"))
ax.text(-0.15, 8.85, "Companion Computer\n(XIAO ESP32-S3)", ha="center", va="top",
        fontsize=11.0, fontweight="bold", color="#c2410c", zorder=2, linespacing=1.2)
ax.text(-0.15, 8.00, "UART MAVLink\n(115200 bps)", ha="center", va="top",
        fontsize=9.8, color="#64748b", zorder=2, linespacing=1.15)

# Aktuator Quadcopter
ax.add_patch(Rectangle((21.0, 0.1), 8.8, 4.3, fc="#f0fdf4", ec="#16a34a", lw=1.6, zorder=1, joinstyle="round"))
ax.text(25.4, 4.05, "Aktuator Quadcopter", ha="center", va="top",
        fontsize=13.5, fontweight="bold", color="#15803d", zorder=2)

# -------------------------------------------------------------
# 2. TIER 1: KALANG TRANSLASI (y = 4.8)
# -------------------------------------------------------------
y_t1 = 4.8

pref_pt = (1.8, y_t1)
vref_pt = (1.8, 6.1)
psiref_pt = (1.8, 7.0)

ax.text(-0.15, y_t1, r"$\mathbf{p}_{\mathrm{ref}}$", ha="center", va="center", fontsize=15.0, fontweight="bold", color="#0f172a")
ax.text(-0.15, 6.1, r"$\mathbf{v}_{\mathrm{ref}}$", ha="center", va="center", fontsize=15.0, fontweight="bold", color="#0f172a")
ax.text(-0.15, 7.0, r"$\psi_{\mathrm{ref}}$", ha="center", va="center", fontsize=15.0, fontweight="bold", color="#0f172a")

sum_p = circle_sum(3.7, y_t1)
p_pos = box(5.0, y_t1 - 0.80, 2.9, 1.6, title="Kendali\nPosisi", subtitle=r"P ($K_p^{\mathrm{pos}}$)",
            fs_title=13.0, fs_sub=11.5)

sum_v = circle_sum(9.5, y_t1, plus_top=True)
p_vel = box(10.7, y_t1 - 0.80, 3.1, 1.6, title="Kendali\nKecepatan", subtitle=r"PID ($K_{p,i,d}^{\mathrm{vel}}$)",
            fs_title=13.0, fs_sub=11.5)

p_conv = box(14.8, y_t1 - 1.10, 5.2, 2.2,
             title="Konversi Akselerasi",
             subtitle="ke Sikap & Gaya Dorong",
             text=r"$T = m(g + a_z)$" + "\n" + r"$\mathbf{q}_{\mathrm{des}} = \mathcal{F}(\mathbf{a}_{\mathrm{cmd}}, \psi_{\mathrm{ref}})$",
             fc="#eff6ff", ec="#3b82f6", fs_title=13.0, fs_sub=11.0, fs_text=11.8)

# Arrows Tier 1
arrow(pref_pt, sum_p["left"])
arrow(sum_p["right"], p_pos["left"], r"$\mathbf{e}_p$", fs=13.0)
arrow(p_pos["right"], sum_v["left"], r"$\mathbf{v}_{\mathrm{cmd}}$", fs=13.0)
arrow(sum_v["right"], p_vel["left"], r"$\mathbf{e}_v$", fs=13.0)
arrow(p_vel["right"], p_conv["left"], r"$\mathbf{a}_{\mathrm{cmd}}$", fs=13.0)

# Feedforward v_ref (lewat atas pada y = 6.1)
ax.plot([vref_pt[0], 2.0, 2.0, sum_v["top"][0], sum_v["top"][0]],
        [vref_pt[1], vref_pt[1], 6.1, 6.1, sum_v["top"][1]],
        color="#0f172a", lw=1.6, zorder=3)
ax.add_patch(FancyArrowPatch((sum_v["top"][0], sum_v["top"][1]+0.2), sum_v["top"],
                             arrowstyle="-|>", mutation_scale=14.0, color="#0f172a", lw=1.6, zorder=3))
ax.text(5.8, 6.25, r"$\mathbf{v}_{\mathrm{ref}}$ (umpan-maju kecepatan)", ha="center", va="bottom", fontsize=11.5,
        bbox=dict(fc="white", ec="none", pad=1.5))

# psi_ref to conv (lewat atas pada y = 7.0)
ax.plot([psiref_pt[0], 1.9, 1.9, p_conv["cx"], p_conv["cx"]],
        [psiref_pt[1], psiref_pt[1], 7.0, 7.0, p_conv["top"][1]],
        color="#0f172a", lw=1.6, zorder=3)
ax.add_patch(FancyArrowPatch((p_conv["cx"], p_conv["top"][1]+0.2), p_conv["top"],
                             arrowstyle="-|>", mutation_scale=14.0, color="#0f172a", lw=1.6, zorder=3))
ax.text(10.5, 7.15, r"$\psi_{\mathrm{ref}}$ (sudut yaw target)", ha="center", va="bottom", fontsize=11.5,
        bbox=dict(fc="white", ec="none", pad=1.5))

# -------------------------------------------------------------
# 3. TIER 2: KALANG ROTASI & AKTUASI (y = 1.6)
# -------------------------------------------------------------
y_t2 = 1.6

psidot_pt = (1.8, 2.3)
ax.text(-0.15, 2.3, r"$\dot{\psi}_{\mathrm{ref}}$", ha="center", va="center", fontsize=15.0, fontweight="bold", color="#0f172a")

sum_q = circle_sum(3.7, y_t2)
p_att = box(5.0, y_t2 - 0.80, 2.9, 1.6, title="Kendali\nSikap", subtitle=r"P ($K_p^{\mathrm{att}}$)",
            fs_title=13.0, fs_sub=11.5)

sum_w = circle_sum(9.5, y_t2, plus_top=True)
p_rate = box(10.7, y_t2 - 0.80, 3.1, 1.6, title="Kendali\nLaju Sudut", subtitle=r"PID ($K_{p,i,d}^{\mathrm{rate}}$)",
             fs_title=13.0, fs_sub=11.5)

p_mix = box(14.6, y_t2 - 0.80, 2.1, 1.6, title="Mixer\nMotor", subtitle="(Quad-X)",
            fc="#eff6ff", ec="#3b82f6", fs_title=12.5, fs_sub=11.0)
p_dshot = box(17.4, y_t2 - 0.80, 2.2, 1.6, title="DShot\n300", subtitle="(DMA)",
              fc="#f8fafc", ec="#64748b", fs_title=12.2, fs_sub=10.5)

p_esc = box(21.4, y_t2 - 0.80, 2.9, 1.6, title="ESC 4-in-1", subtitle="BLS 35A",
            fs_title=12.5, fs_sub=11.0)
p_mot = box(25.8, y_t2 - 0.80, 3.1, 1.6, title="4× Motor", subtitle="BLDC 1950KV",
            fs_title=12.5, fs_sub=11.0)

# Signals from Conv to Tier 2:
# 1. q_des to sum_q (turun dari conv, belok di y = 3.35, turun di x = 3.1 langsung ke sum_q)
ax.plot([p_conv["left"][0] + 0.6, p_conv["left"][0] + 0.6, 3.1, 3.1, sum_q["left"][0]-0.15, sum_q["left"][0]],
        [p_conv["bottom"][1], 3.35, 3.35, y_t2, y_t2, y_t2],
        color="#0f172a", lw=1.6, zorder=3)
ax.add_patch(FancyArrowPatch((sum_q["left"][0]-0.2, y_t2), sum_q["left"],
                             arrowstyle="-|>", mutation_scale=14.0, color="#0f172a", lw=1.6, zorder=3))
ax.text(8.0, 3.50, r"$\mathbf{q}_{\mathrm{des}}$ (orientasi target)", ha="center", va="bottom", fontsize=11.5,
        bbox=dict(fc="white", ec="none", pad=1.5))

# 2. Thrust T to mixer
ax.plot([p_conv["cx"] + 0.4, p_conv["cx"] + 0.4, p_mix["cx"], p_mix["cx"]],
        [p_conv["bottom"][1], 2.80, 2.80, p_mix["top"][1]],
        color="#0f172a", lw=1.6, zorder=3)
ax.add_patch(FancyArrowPatch((p_mix["cx"], p_mix["top"][1]+0.2), p_mix["top"],
                             arrowstyle="-|>", mutation_scale=14.0, color="#0f172a", lw=1.6, zorder=3))
ax.text(p_mix["cx"] + 0.25, 2.90, r"Gaya Dorong $T$", ha="left", va="bottom", fontsize=11.5,
        bbox=dict(fc="white", ec="none", pad=1.5))

# Arrows Tier 2
arrow(sum_q["right"], p_att["left"], r"$\mathbf{e}_q$", fs=13.0)
arrow(p_att["right"], sum_w["left"], r"$\boldsymbol{\omega}_{\mathrm{des}}$", label_pos=0.42, fs=13.0)
arrow(sum_w["right"], p_rate["left"], r"$\mathbf{e}_\omega$", fs=13.0)
arrow(p_rate["right"], p_mix["left"], r"$\boldsymbol{\tau}$", fs=13.0)
arrow(p_mix["right"], p_dshot["left"], "PWM", fs=11.0)
arrow(p_dshot["right"], p_esc["left"], "DShot", label_pos=0.50, fs=11.8, color="#1d4ed8", lw=1.6, dy=0.18)
arrow(p_esc["right"], p_mot["left"], "3-Fase", fs=11.0)

# Feedforward psidot_ref (lewat y = 2.3)
ax.plot([psidot_pt[0], 2.2, 2.2, sum_w["cx"], sum_w["cx"]],
        [psidot_pt[1], psidot_pt[1], 2.3, 2.3, sum_w["top"][1]],
        color="#0f172a", lw=1.6, zorder=3)
ax.add_patch(FancyArrowPatch((sum_w["cx"], sum_w["top"][1]+0.2), sum_w["top"],
                             arrowstyle="-|>", mutation_scale=14.0, color="#0f172a", lw=1.6, zorder=3))
ax.text(5.5, 2.42, r"$\dot{\psi}_{\mathrm{ref}}$ (umpan-maju yaw)", ha="center", va="bottom", fontsize=11.5,
        bbox=dict(fc="white", ec="none", pad=1.5))

# -------------------------------------------------------------
# 4. TIER 3: STATE ESTIMATOR (EKF3) & SENSOR
# -------------------------------------------------------------
# p_extnav width 3.6 (dari x=4.9 ke 8.5)
p_extnav = box(4.9, -2.1, 3.6, 1.6, title="Navigasi\nEksternal",
               subtitle="AprilTag Kamera (60 Hz)", fc="#f0fdfa", ec="#0d9488", fs_title=12.2, fs_sub=10.5)
p_imu = box(12.3, -2.1, 6.8, 1.6, title="Sensor IMU Onboard ICM-42688P",
            subtitle="Akselerometer & Giroskop (1--8 kHz)", fc="#f0fdfa", ec="#0d9488", fs_title=12.5, fs_sub=11.0)

p_ekf = box(3.2, -4.6, 16.2, 1.9, title="ArduPilot EKF3 State Estimator (STM32F405, 400 Hz)",
            text=r"Fusi Multi-Tingkat Menghasilkan Estimasi:" + "\n" +
                 r"Pose 3D ($\hat{\mathbf{p}}, \hat{\mathbf{q}}$), Kecepatan Linear ($\hat{\mathbf{v}}$), dan Laju Sudut ($\hat{\boldsymbol{\omega}}$)",
            fc="#ccfbf1", ec="#0f766e", fs_title=13.5, fs_text=12.2, lw=1.8)

# Sensors to EKF3
arrow(p_extnav["bottom"], (p_extnav["cx"], p_ekf["top"][1]), color="#0f766e", lw=1.6)
arrow(p_imu["bottom"], (p_imu["cx"], p_ekf["top"][1]), color="#0f766e", lw=1.6)

# MAVLink vision pose from ESP32
ax.text(-0.15, -1.30, "Paket Vision\nPose", ha="center", va="center", fontsize=12.5, color="#c2410c", fontweight="bold")
arrow((1.8, -1.30), p_extnav["left"], "MAVLink", label_pos=0.50, fs=11.5, color="#ea580c", ls="--", lw=1.6, dy=0.16)

# -------------------------------------------------------------
# 5. JALUR UMPAN BALIK EKF3 KE KOMPARATOR
# -------------------------------------------------------------
# 1. p_hat ke sum_p (naik di x = 2.7, belok ke sum_p)
ax.plot([2.7, 2.7, sum_p["cx"], sum_p["cx"]],
        [p_ekf["top"][1], 3.9, 3.9, sum_p["bottom"][1]],
        color="#0f766e", lw=1.6, zorder=3)
ax.add_patch(FancyArrowPatch((sum_p["cx"], sum_p["bottom"][1]-0.2), sum_p["bottom"],
                             arrowstyle="-|>", mutation_scale=14.0, color="#0f766e", lw=1.6, zorder=3))
ax.text(2.50, 2.5, r"$\hat{\mathbf{p}}$", ha="right", va="center", fontsize=14.0, color="#0f766e",
        bbox=dict(fc="white", ec="none", pad=1.5))

# 2. q_hat ke sum_q (naik vertikal di x = sum_q["cx"])
ax.plot([sum_q["cx"], sum_q["cx"]],
        [p_ekf["top"][1], sum_q["bottom"][1]],
        color="#0f766e", lw=1.6, zorder=3)
ax.add_patch(FancyArrowPatch((sum_q["cx"], sum_q["bottom"][1]-0.2), sum_q["bottom"],
                             arrowstyle="-|>", mutation_scale=14.0, color="#0f766e", lw=1.6, zorder=3))
ax.text(sum_q["cx"] + 0.20, 0.45, r"$\hat{\mathbf{q}}$", ha="left", va="center", fontsize=14.0, color="#0f766e",
        bbox=dict(fc="white", ec="none", pad=1.5))

# 3. v_hat ke sum_v (naik di x = 8.85, belok ke sum_v)
ax.plot([8.85, 8.85, sum_v["cx"], sum_v["cx"]],
        [p_ekf["top"][1], 3.9, 3.9, sum_v["bottom"][1]],
        color="#0f766e", lw=1.6, zorder=3)
ax.add_patch(FancyArrowPatch((sum_v["cx"], sum_v["bottom"][1]-0.2), sum_v["bottom"],
                             arrowstyle="-|>", mutation_scale=14.0, color="#0f766e", lw=1.6, zorder=3))
ax.text(8.65, 2.5, r"$\hat{\mathbf{v}}$", ha="right", va="center", fontsize=14.0, color="#0f766e",
        bbox=dict(fc="white", ec="none", pad=1.5))

# 4. omega_hat ke sum_w (naik vertikal di x = sum_w["cx"])
ax.plot([sum_w["cx"], sum_w["cx"]],
        [p_ekf["top"][1], sum_w["bottom"][1]],
        color="#0f766e", lw=1.6, zorder=3)
ax.add_patch(FancyArrowPatch((sum_w["cx"], sum_w["bottom"][1]-0.2), sum_w["bottom"],
                             arrowstyle="-|>", mutation_scale=14.0, color="#0f766e", lw=1.6, zorder=3))
ax.text(sum_w["cx"] + 0.20, 0.45, r"$\hat{\boldsymbol{\omega}}$", ha="left", va="center", fontsize=14.0, color="#0f766e",
        bbox=dict(fc="white", ec="none", pad=1.5))

out_png = "tulisan/proposal/figures/low_level_controller.png"
out_pdf = "tulisan/proposal/figures/low_level_controller.pdf"
fig.savefig(out_png, dpi=300, bbox_inches="tight", facecolor="white")
fig.savefig(out_pdf, bbox_inches="tight", facecolor="white")
print("Saved successfully to", out_png, "and", out_pdf)
