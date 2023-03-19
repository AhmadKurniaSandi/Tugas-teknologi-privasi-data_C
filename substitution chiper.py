# Fungsi untuk mengenkripsi pesan dengan substitution cipher
def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Ubah karakter menjadi huruf besar
            char = char.upper()
            # Substitusi karakter berdasarkan key
            char = key[ord(char) - 65]
        ciphertext += char
    return ciphertext

# Fungsi untuk mendekripsi pesan dengan substitution cipher
def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Ubah karakter menjadi huruf besar
            char = char.upper()
            # Kembalikan karakter ke nilai aslinya berdasarkan key
            char = chr(key.index(char) + 65)
        plaintext += char
    return plaintext

# Contoh penggunaan
plaintext = "Ini adalah pesan rahasia"
key = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
ciphertext = encrypt(plaintext, key)
print("Pesan terenkripsi:", ciphertext)
decrypted = decrypt(ciphertext, key)
print("Pesan didekripsi:", decrypted)
