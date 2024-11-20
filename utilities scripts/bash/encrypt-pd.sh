#input folder dan output folder
read -p "Masukkan path folder PDF: " input_folder
read -p "Masukkan path folder output: " output_folder

# Prompt untuk memasukkan password
read -sp "Masukkan password untuk enkripsi: " password
echo

encrypt_pdfs_in_folder() {
    folder="$1"
    encrypted_folder="$2"
    user_password="$3"

    # Buat folder output kalau belum ada
    mkdir -p "$encrypted_folder"

    # Loop untuk mengenkripsi semua file PDF
    for file in "$folder"/*.pdf; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            qpdf --encrypt "$user_password" "$user_password" 256 -- "$file" "$encrypted_folder/${filename%.pdf}-secured.pdf"
        fi
    done
}

# Validasi folder input
if [ -d "$input_folder" ]; then
    echo "Encrypting PDFs in folder: $input_folder"
    encrypt_pdfs_in_folder "$input_folder" "$output_folder" "$password"
    echo "Encryption selesai! File terenkripsi disimpan di $output_folder"
else
    echo "Folder $input_folder tidak ditemukan."
fi
