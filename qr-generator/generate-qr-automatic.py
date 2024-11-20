import pandas as pd
import qrcode
import os
import math

os.system('clear')

def load_data(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    elif file_path.endswith('.txt'):
        df = pd.read_excel(file_path)
    else:
        raise ValueError('format file harus csv, xlsx atau txt')
    return df

def generate_qr_codes(df, path_output, url_column, name_column):
    # Buat folder output jika belum ada
    if not os.path.exists(path_output):
        os.makedirs(path_output)
    
    for index, row in df.iterrows():
        # Cek dan bersihkan nama file
        file_name = row[name_column]
        if isinstance(file_name, float) and math.isnan(file_name):
            file_name = 'unknown'
        else:
            file_name = str(file_name).replace('/', '-')
        
        # Ambil URL untuk QR Code
        url = row[url_column]
        
        # Generate QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        #QR Code terbentuk
        img = qr.make_image(fill='black', back_color='white')
        #QR code disimpan ke
        img.save(f"{path_output}/{file_name}.png")

if __name__ == "__main__":
    path_input = input("Masukkan path file CSV/XLSX kamu (misal: 'data/daftar_link.xlsx'): ")
    path_output = input("Masukkan path untuk simpan hasil QR Code (misal: 'output/'): ")
    
    url_column = input("Masukkan column yang berisi kolom untuk URL (contoh: 'link' atau 'url'): ")
    name_column = input("Masukkan nama kolom untuk nama file QR (contoh: 'kode', 'itemId', dll.): ")
    
    df = load_data(path_input)
    generate_qr_codes(df, path_output, url_column, name_column)
    print("Semua QR Code berhasil dibuat!")
