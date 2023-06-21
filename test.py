from cryptography.fernet import Fernet


# Fungsi untuk melakukan enkripsi
def encrypt(plaintext, key):
    f = Fernet(key)
    encrypted_text = f.encrypt(plaintext)
    return encrypted_text


# Fungsi untuk melakukan dekripsi
def decrypt(ciphertext, key):
    f = Fernet(key)
    decrypted_text = f.decrypt(ciphertext)
    return decrypted_text


# Contoh penggunaan
plaintext = b"This is a secret message."
key = Fernet.generate_key()  # Menghasilkan kunci acak

# Enkripsi
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

# Dekripsi
decrypted_text = decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text.decode("utf-8"))
