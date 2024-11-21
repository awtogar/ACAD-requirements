import pandas as pd
import qrcode
import os
import math

os.system('clear')

def load_data(file_path):
    # ngambil data sesuai format file
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.txt'):
        return pd.read_excel(file_path)
    else:
        raise ValueError('Format file harus csv, xlsx, atau txt')

def generate_qr_codes(df, path_output, url_column, name_column):
    # bikin folder output jika belum ada
    os.makedirs(path_output, exist_ok=True)
    
    for _, row in df.iterrows():
        # cek dan bersihkan nama file
        file_name = str(row[name_column]).replace('/', '-') if pd.notna(row[name_column]) else 'unknown'
        url = row[url_column]
        
        # Generate QR Code
        qr = qrcode.QRCode(
            version=1, 
            error_correction=qrcode.constants.ERROR_CORRECT_L, 
            box_size=10, 
            border=4
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        # Simpan QR Code sebagai file PNG
        img = qr.make_image(fill='black', back_color='white')
        img.save(f"{path_output}/{file_name}.png")

if __name__ == "__main__":
    print("=== QR Code Generator ===")
    
    # Input dari user
    path_input = input("1. Masukkan path file data (CSV/XLSX): ").strip()
    print("   ✓ File data berhasil dimuat.")
    path_output = input("2. Masukkan folder tujuan untuk menyimpan QR Code (misal: 'output/'): ").strip()
    print("   ✓ Folder output disiapkan.")
    url_column = input("3. Masukkan nama kolom yang berisi URL/Link: ").strip()
    name_column = input("4. Masukkan nama kolom untuk nama file QR Code: ").strip()
    
    # Proses pembuatan QR Code
    print("\nMemulai proses pembuatan QR Code...")
    df = load_data(path_input)
    generate_qr_codes(df, path_output, url_column, name_column)
    print("Semua QR Code berhasil dibuat!")
