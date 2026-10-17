# Tugas Pengolahan Citra dan Video

Repository ini berisi kumpulan tugas mata kuliah **Pengolahan Citra dan Video (PCV)** menggunakan Python, OpenCV, dan NumPy.

## 👤 Identitas

- **Nama:** Sarah Shafira Maulida
- **NRP:** 5024241035
- **Mata Kuliah:** Pengolahan Citra dan Video
- **Bahasa:** Python
- **Library:** OpenCV, NumPy

---

## 📚 Daftar Tugas

### Tugas 1 — Introduction

Tugas 1 merupakan pengenalan dasar pengolahan citra dan video menggunakan library OpenCV.

Materi yang diimplementasikan meliputi:

- Membaca dan menampilkan citra.
- Membuat filter warna pada citra.
- Membuat filter warna secara real-time menggunakan webcam.

Pada bagian filter warna, citra diolah dengan menghilangkan channel **Blue** dan **Red**, sehingga hanya channel **Green** yang dipertahankan dan menghasilkan tampilan filter hijau.

Untuk pengolahan video, webcam digunakan sebagai sumber input. Setiap frame yang ditangkap kemudian diproses menggunakan metode filter warna yang sama secara real-time. Program dapat dihentikan dengan menekan tombol **Q**. 

### Tugas 2 — Transformasi Intensitas

Implementasi beberapa metode transformasi intensitas citra:

- Negatif
- Logaritmik
- Gamma
- Contrast Stretching
- Threshold
- Ekualisasi Histogram

### Tugas 3 — Filter Spasial

Implementasi berbagai filter spasial pada citra:

- Box 3 × 3
- Gaussian 3 × 3
- Median
- Laplacian 4
- Laplacian 8
- Penajam
- Sobel X
- Sobel Y

---

## 🛠️ Tools

- Python
- OpenCV
- NumPy
- Spyder

---

## 📁 Struktur Repository

```text
Tugas-PCV/
│
├── images/
│
│   └── 1-Intro.py
│   └── 2-ti-eq.py
│   └── 3-filter-spasial.py
│
└── README.md
