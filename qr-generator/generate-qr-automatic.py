import pandas as pd
import qrcode
import os
import math


def load_data(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        raise ValueError('File must be .csv or .xlsx')
    return df

def generate_qr_codes(df, path_output):
    if not os.path.exists(path_output):
        os.makedirs(path_output)

    # Nyari row dengan index _Kode
    for index, row in df.iterrows():
        file_name = row['_Kode']

        if isinstance(file_name, float) and math.isnan(file_name):
            file_name = 'unknown'
        else:
            file_name = str(file_name).replace('/', '-')

        url = row['_Link']

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        qr.add_data(url)
        qr.make(fit=True)
    
        img = qr.make_image(fill='black', back_color='white')
        
        # Simpan image sesuai dengan nama di folder output
        img.save(f"{path_output}/{file_name}.png")


if __name__ == "__main__":
    path_input = input("Masukkan path file CSV/XLSX kamu: ")
    path_output = input("Masukkan path untuk simpan hasilnya: ")

    df = load_data(path_input)
    generate_qr_codes(df, path_output)
    print("Semua QR udah dibuat!")
