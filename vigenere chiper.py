# Fungsi untuk mengenkripsi pesan dengan Vigenere cipher
def encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            # Ubah karakter menjadi huruf besar
            char = char.upper()
            # Hitung nilai shift berdasarkan huruf di key
            shift = ord(key[key_index % len(key)].upper()) - 65
            # Shift karakter berdasarkan nilai shift
            char = chr((ord(char) + shift - 65) % 26 + 65)
            # Tambahkan karakter key_index
            key_index += 1
        ciphertext += char
    return ciphertext

# Fungsi untuk mendekripsi pesan dengan Vigenere cipher
def decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            # Ubah karakter menjadi huruf besar
            char = char.upper()
            # Hitung nilai shift berdasarkan huruf di key
            shift = ord(key[key_index % len(key)].upper()) - 65
            # Shift karakter berdasarkan nilai shift
            char = chr((ord(char) - shift - 65) % 26 + 65)
            # Tambahkan karakter key_index
            key_index += 1
        plaintext += char
    return plaintext

# Contoh penggunaan
plaintext = "Ini adalah pesan rahasia"
key = "259"
ciphertext = encrypt(plaintext, key)
print("Pesan terenkripsi:", ciphertext)
decrypted = decrypt(ciphertext, key)
print("Pesan didekripsi:", decrypted)
