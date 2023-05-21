from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_text(key, text):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
    encrypted_text = base64.b64encode(encrypted_bytes).decode()
    return encrypted_text

def decrypt_text(key, encrypted_text):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_bytes = base64.b64decode(encrypted_text)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    decrypted_text = unpad(decrypted_bytes, AES.block_size).decode()
    return decrypted_text

# Meminta input dari pengguna
key = input("Masukkan kunci (16, 24, atau 32 karakter): ")
text = input("Masukkan teks yang akan dienkripsi: ")

# Mengenkripsi dan mendekripsi teks
encrypted_text = encrypt_text(key.encode(), text)
decrypted_text = decrypt_text(key.encode(), encrypted_text)

# Menampilkan hasil
print("Teks Setelah Dienkripsi:", encrypted_text)
print("Teks Setelah Didekripsi:", decrypted_text)
