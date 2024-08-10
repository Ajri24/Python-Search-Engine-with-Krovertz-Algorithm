# Python-Search-Engine-with-Krovertz-Algorithm
Krovertz Search
Krovertz Search adalah aplikasi web sederhana berbasis Flask yang digunakan untuk melakukan pencarian teks dalam dokumen-dokumen yang terdapat dalam folder tertentu. Aplikasi ini mendukung pencarian pada file teks (.txt), Microsoft Word (.docx), dan PDF (.pdf). Aplikasi ini juga melakukan preprocessing teks, termasuk case folding, tokenisasi, filtering, dan stemming, untuk memastikan hasil pencarian yang lebih akurat.

Fitur
Pencarian Teks: Melakukan pencarian teks berdasarkan kata kunci yang dimasukkan pengguna.
Preprocessing Teks: Termasuk case folding (mengubah teks menjadi huruf kecil), tokenisasi (memecah teks menjadi kata-kata), filtering (menghapus tanda baca), dan stemming (mengubah kata ke bentuk dasarnya) menggunakan pustaka Sastrawi.
Pencarian Berbasis Dokumen: Mampu mencari kata kunci di berbagai tipe dokumen, termasuk .txt, .docx, dan .pdf.
Perhitungan Skor Kesamaan: Menghitung dan menampilkan skor kesamaan antara kata kunci dengan teks dalam dokumen, serta jumlah dan frekuensi kemunculan kata dalam dokumen.
Tampilan Hasil: Menyortir dan menampilkan hasil pencarian berdasarkan skor kesamaan.
Cara Penggunaan
Instalasi: Pastikan Python 3 dan pip sudah terinstal di sistem Anda. Install dependencies yang diperlukan dengan menjalankan perintah berikut:
pip install flask docx2txt PyPDF2 Sastrawi
Copy code
pip install flask docx2txt PyPDF2 Sastrawi
Struktur Folder: Pastikan Anda memiliki folder bernama files di direktori yang sama dengan script ini. Letakkan semua dokumen yang ingin dicari di dalam folder tersebut.

Menjalankan Aplikasi: Jalankan aplikasi dengan perintah:
python nama_script.py
Copy code
python nama_script.py
Mengakses Aplikasi: Buka browser dan akses http://127.0.0.1:5000 untuk menggunakan aplikasi.

Pencarian: Masukkan kata kunci di kotak pencarian dan tekan tombol Search. Aplikasi akan menampilkan daftar dokumen yang mengandung kata kunci, beserta skor kesamaan dan statistik terkait.

Struktur Kode
app.py: File utama yang mengandung logika aplikasi.
templates/index.html: Template HTML untuk tampilan antarmuka pengguna.
Prasyarat
Python 3.x
Flask
docx2txt
PyPDF2
Sastrawi
Lisensi
Aplikasi ini dirancang untuk tujuan pembelajaran dan pengembangan lebih lanjut. Silakan gunakan, modifikasi, dan distribusikan sesuai kebutuhan Anda.
