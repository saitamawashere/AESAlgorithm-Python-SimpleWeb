from flask import Flask, render_template, request
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

app = Flask(__name__)

# Kunci AES yang digunakan untuk enkripsi dan dekripsi
key = b'ThisIsASecretKey'

# Fungsi untuk melakukan enkripsi menggunakan AES
def encrypt_file(file_path):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    with open(file_path + '.enc', 'wb') as file:
        file.write(ciphertext)

# Fungsi untuk melakukan dekripsi menggunakan AES
def decrypt_file(file_path):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(file_path, 'rb') as file:
        ciphertext = file.read()
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    with open(file_path[:-4], 'wb') as file:
        file.write(plaintext)

# Rute untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Rute untuk menangani permintaan pengunggahan dokumen dan enkripsi
@app.route('/encrypt', methods=['POST'])
def encrypt():
    file = request.files['file']
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        encrypt_file(file_path)
        return 'Dokumen berhasil dienkripsi.'
    else:
        return 'Gagal mengunggah dokumen.'

# Rute untuk menangani permintaan dekripsi
@app.route('/decrypt', methods=['POST'])
def decrypt():
    file = request.files['file']
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        decrypt_file(file_path)
        return 'Dokumen berhasil didekripsi.'
    else:
        return 'Gagal mengunggah dokumen.'

if __name__ == '__main__':
    app.run(debug=True)
