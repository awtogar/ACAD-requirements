# Project Setup Guide  

Repository ini menyediakan semua tools dan script yang diperlukan untuk mendukung workflow proyek ACAD - MSIB 7.  

---

## Setup  

Ikuti langkah-langkah berikut untuk menginstal paket dan dependensi yang diperlukan.  

### Prerequisites  

- **Python 3.9** atau lebih tinggi.  
- **pip** (Python package installer).  

---

### Environment Setup  

1. **Buat Virtual Environment**  
   ```bash
   python -m venv acad-venv
   ```
2. **Aktifkan Virtual Environment**
    **Mac**
        > source acad-venv/bin/activate
    **Windows**
        > acad-venv\Scripts\activate
3. **Install Dependensi**
    Pilih salah satu dari dua perintah berikut:
    - **Versi tertentu**
            ```pip install chardet==5.2.0 numpy==2.1.2 pandas==2.2.3 pdf2image==1.17.0 pillow==10.4.0 PyPDF2==3.0.1 python-dateutil==2.9.0.post0 pytz==2024.2 qrcode==8.0 reportlab==4.2.5 six==1.16.0 tzdata==2024.2
             ```
             
    - **Versi umum**
            ```pip install chardet numpy pandas pdf2image pillow PyPDF2 python-dateutil pytz qrcode reportlab six tzdata
             ```


4. **Verifikasi Instalasi**
untuk memastikan paket sudah terinstall di sistem
    ```
    pip list
    ```

5. **Script Usage**  
    **Generate QR Code**  
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
          
6. **Related Repository**  
    Kunjungi repository utama untuk penjelasan proyek lebih lengkap:  
    [🔗 ACAD Main Repository](https://github.com/awtogar/acad)
