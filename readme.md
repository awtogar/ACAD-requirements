# Project Setup Guide  
Repository ini menyediakan semua tools dan script yang diperlukan untuk mendukung workflow proyek ACAD - MSIB 7.
Ikuti langkah-langkah berikut untuk menjalankan alur kerja ini. Pastikan semua persyaratan dan dependensi telah diinstal.   

## Setup  

Ikuti langkah-langkah berikut untuk menginstal paket dan dependensi yang diperlukan.  

### Prerequisites  

- **Python 3.9** atau lebih tinggi. 
  -  Pastikan Python dan `pip` telah terinstal:  
        ```bash
        python --version
        pip --version
        ```  
        Jika belum:  
     - **Windows**: Download Python dari [python.org](https://www.python.org/) dan centang **Add Python to PATH** saat instalasi.  
     - **macOS**: Python 3 biasanya sudah terinstal. Alternatifnya, gunakan Homebrew:  
       ```bash
       brew install python
       ``` 
- **pip** (Python package installer).  


### Environment Setup (Optional)

1. **Buat Virtual Environment**  
   ```bash
   python -m venv acad-venv
   ```
2. **Aktifkan Virtual Environment**
    **Mac**
        > source acad-venv/bin/activate
    **Windows**
        > acad-venv\Scripts\activate
---

### Package Library

1. **Installing Dependensi**
    Pilih salah satu dari dua perintah berikut:
    - **Versi tertentu**
            ```pip install chardet==5.2.0 numpy==2.1.2 pandas==2.2.3 pdf2image==1.17.0 pillow==10.4.0 PyPDF2==3.0.1 python-dateutil==2.9.0.post0 pytz==2024.2 qrcode==8.0 reportlab==4.2.5 six==1.16.0 tzdata==2024.2
             ```
             
    - **Versi umum**
            ```pip install chardet numpy pandas pdf2image pillow PyPDF2 python-dateutil pytz qrcode reportlab six tzdata
             ```
2. **Uninstalling Dependensi**
   Jika package library yang di install mengalami error atau package sudah discontinued bisa di uninstall
   - **Cara Ke-1**
        ```
        pip uninstall <packagename>
        ```
    - **Cara Ke-2**
      menguninstall sebuah package dari virtual environtment
        ```
        pipenv uninstall <packagename>
        ```

3. **Verifikasi Instalasi**
untuk memastikan paket sudah terinstall di sistem
    ```
    pip list
    ```
---
### PDF Encrypter  

Script untuk mengenkripsi file PDF menggunakan Bash tersedia di repository `acad-requirement`. Langkah-langkah penggunaan:  

1. **Download Script**  
   Download script enkripsi dari repository [🔗 acad-requirements](https://github.com/awtogar/ACAD-requirements).  

2. **Menggunakan Script**  
   Ikuti panduan berikut untuk mengenkripsi file PDF:  
   - Input folder: Masukkan lokasi folder file PDF asli.  
   - Output folder: Tentukan lokasi untuk menyimpan file PDF yang sudah terenkripsi.  
   - Password: Masukkan password untuk mengenkripsi seluruh file PDF.  
   - Selesai

    **Output:**  
    Setiap file PDF akan terenkripsi dan diberi tambahan nama `-secured`.  

---
### Generate QR Code 
Script untuk generate QR Code dapat dijalankan dengan: 
    ```
    python generate-qr-automatic.py
    ```

**Input dan Output:**  
-   **Input**: Path CSV file dalam format absolute.  
            ```
            /Users/awtogar/Desktop/belajar/sumber-data.csv  
            ```
-   **Output**: Lokasi folder untuk menyimpan QR Code.  
        ```
        /Users/awtogar/Desktop/belajar/qr/codes/  
        ```
          
<!-- 1. **Related Repository**  
    Kunjungi repository utama untuk penjelasan proyek lebih lengkap:  
    [🔗 ACAD Main Repository](https://github.com/awtogar/acad) -->
