# Fungsi untuk mengenkripsi pesan dengan transposition cipher
def encrypt(plaintext, key):
    # Hitung jumlah baris dan kolom matriks berdasarkan panjang kunci
    num_columns = len(key)
    num_rows = len(plaintext) // num_columns + 1
    # Tambahkan padding untuk melengkapi baris terakhir
    plaintext += " " * (num_rows * num_columns - len(plaintext))
    # Buat matriks pesan dengan dimensi num_rows x num_columns
    matrix = [list(plaintext[i:i+num_columns]) for i in range(0, len(plaintext), num_columns)]
    # Buat matriks hasil enkripsi dengan dimensi num_columns x num_rows
    encrypted_matrix = [[None] * num_rows for _ in range(num_columns)]
    for i, char in enumerate(key):
        # Temukan indeks kolom di matriks pesan yang sesuai dengan karakter kunci
        col_index = ord(char) - ord("1")
        # Salin isi kolom tersebut ke kolom i di matriks hasil enkripsi
        for j in range(num_rows):
            encrypted_matrix[i][j] = matrix[j][col_index]
    # Gabungkan karakter-karakter dalam matriks hasil enkripsi menjadi string terenkripsi
    ciphertext = "".join(char for row in encrypted_matrix for char in row)
    return ciphertext

# Fungsi untuk mendekripsi pesan dengan transposition cipher
def decrypt(ciphertext, key):
    # Hitung jumlah baris dan kolom matriks berdasarkan panjang kunci
    num_columns = len(key)
    num_rows = len(ciphertext) // num_columns
    # Buat matriks hasil enkripsi dengan dimensi num_rows x num_columns
    encrypted_matrix = [list(ciphertext[i:i+num_rows]) for i in range(0, len(ciphertext), num_rows)]
    # Buat matriks pesan dengan dimensi num_columns x num_rows
    matrix = [[None] * num_rows for _ in range(num_columns)]
    for i, char in enumerate(key):
        # Temukan indeks kolom di matriks pesan yang sesuai dengan karakter kunci
        col_index = ord(char) - ord("1")
        # Salin isi kolom tersebut ke kolom i di matriks pesan
        for j in range(num_rows):
            matrix[col_index][j] = encrypted_matrix[i][j]
    # Gabungkan karakter-karakter dalam matriks pesan menjadi string pesan asli
    plaintext = "".join(char for row in matrix for char in row).rstrip()
    return plaintext

# Contoh penggunaan
plaintext = "Ini adalah pesan rahasia"
key = "3142"
ciphertext = encrypt(plaintext, key)
print("Pesan terenkripsi:", ciphertext)
decrypted = decrypt(ciphertext, key)
print("Pesan didekripsi:", decrypted)
