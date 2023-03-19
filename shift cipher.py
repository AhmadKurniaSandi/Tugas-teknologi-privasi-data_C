# Fungsi untuk mengenkripsi pesan dengan shift cipher
def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Ubah karakter menjadi huruf besar
            char = char.upper()
            # Shift karakter berdasarkan nilai shift
            char = chr((ord(char) + shift - 65) % 26 + 65)
        ciphertext += char
    return ciphertext

# Fungsi untuk mendekripsi pesan dengan shift cipher
def decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Ubah karakter menjadi huruf besar
            char = char.upper()
            # Shift karakter berdasarkan nilai shift
            char = chr((ord(char) - shift - 65) % 26 + 65)
        plaintext += char
    return plaintext

# Contoh penggunaan
plaintext = "Ini adalah pesan rahasia"
shift = 59
ciphertext = encrypt(plaintext, shift)
print("Pesan terenkripsi:", ciphertext)
decrypted = decrypt(ciphertext, shift)
print("Pesan didekripsi:", decrypted)
