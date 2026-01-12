<div align="center">

# 🎥 3D Camera Transformation Engine
### Tugas Grafika Komputer 3D | Semester 5

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Computation-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Arch Linux](https://img.shields.io/badge/Arch_Linux-Compatible-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white)
![NvChad](https://img.shields.io/badge/Editor-NvChad-46a55f?style=for-the-badge&logo=neovim&logoColor=white)

<p align="center">
  <a href="#-demo-preview">Lihat Demo</a> •
  <a href="#-cara-instalasi">Instalasi</a> •
  <a href="#-matematika-di-balik-layar">Teori</a>
</p>

</div>

---

## 🚀 Tentang Proyek

Repositori ini adalah implementasi algoritma **World-to-View Transformation** dalam Grafika Komputer. Program ini mengubah koordinat objek dari sistem dunia (*World Space*) ke sistem kamera (*View Space*) menggunakan operasi matriks dan vektor basis $(n, u, v)$.

**Kasus Studi:**
> Membuktikan secara matematis dan komputasi bahwa titik $P(2,0,5)$ yang dilihat oleh kamera di $Eye(6,3,5)$ akan berada tepat di tengah layar $(0,0)$ dengan jarak 5 satuan.

---

## 📊 Demo Preview

| Input (World Space) 🌍 | Output (Camera Space) 📷 |
| :--- | :--- |
| **Titik Objek:** `(2, 0, 5)` | **Posisi X:** `0.0` (Tengah) |
| **Posisi Kamera:** `(6, 3, 5)` | **Posisi Y:** `0.0` (Tengah) |
| **Target Pandang:** `(2, 0, 5)` | **Posisi Z:** `-5.0` (Jarak) |

> *Program ini juga menghasilkan visualisasi plot 3D interaktif menggunakan Matplotlib.*

---

## 🧠 Matematika di Balik Layar

<details>
<summary><b>🔻 Klik untuk melihat Rumus & Penjelasan (Interaktif)</b></summary>
<br>

Untuk mengubah sudut pandang, kita membangun matriks $M_{view}$ dengan langkah berikut:

### 1. Menentukan Vektor Basis $(n, u, v)$
Sistem koordinat kamera dibangun dari 3 vektor yang saling tegak lurus (ortogonal):

* **Vektor $n$ (Forward):** Arah dari target ke mata (sumbu Z).
    $$n = \frac{P_{eye} - P_{ref}}{|P_{eye} - P_{ref}|}$$

* **Vektor $u$ (Right):** Arah kanan kamera (sumbu X).
    $$u = \frac{V_{up} \times n}{|V_{up} \times n|}$$

* **Vektor $v$ (Up):** Arah atas kamera yang tegak lurus (sumbu Y).
    $$v = n \times u$$
