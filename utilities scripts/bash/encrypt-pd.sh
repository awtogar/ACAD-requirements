# path
read -p "Masukkan path folder PDF: " input_folder
read -p "Masukkan path folder output: " output_folder

# Password yang bakal dipakai untuk encrypt
password="1982"

encrypt_pdfs_in_folder() {
    folder="$1"
    encrypted_folder="$2"

    # Buat folder output kalau belum ada
    mkdir -p "$encrypted_folder"

    # Loop buat encrypt semua file yg bakal digenerate
    for file in "$folder"/*.pdf; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            qpdf --encrypt "$password" "$password" 256 -- "$file" "$encrypted_folder/${filename%.pdf}-secured.pdf"
        fi
    done
}

# Cek cek folder inputnya udh valid blm
if [ -d "$input_folder" ]; then
    echo "Encrypting PDFs in folder: $input_folder"
    encrypt_pdfs_in_folder "$input_folder" "$output_folder"
    echo "Encryption selesai! File terenkripsi disimpan di $output_folder"
else
    echo "Folder $input_folder tidak ditemukan."
fi