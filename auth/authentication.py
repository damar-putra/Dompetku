import hashlib
import secrets
import uuid
import re
import getpass
from utils.storage import baca_json, simpan_json
from config.settings import FILE_AKUN_USER

def hash_password(password):
    salt = secrets.token_hex(16)
    hash_objek = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), bytes.fromhex(salt), 100000)
    return salt, hash_objek.hex()

def verifikasi_password(password_input, salt, hash_tersimpan):
    hash_objek = hashlib.pbkdf2_hmac('sha256', password_input.encode('utf-8'), bytes.fromhex(salt), 100000)
    return hash_objek.hex() == hash_tersimpan

def registrasi_user():
    print("=== Registrasi User Baru ===")
    nama = input("Masukkan nama lengkap: ").strip()
    if not nama:
        print(">> Error: Nama tidak boleh kosong.")
        return False

    username = input("Masukkan username: ").strip().lower().replace(" ", "")
    if not re.match(r'^[a-z0-9_]+$', username):
        print(">> Error: Username hanya boleh mengandung huruf, angka, dan underscore.")
        return False

    data_akun_user = baca_json(FILE_AKUN_USER)
    for user in data_akun_user:
        if user["username"] == username:
            print(">> Error: Username sudah digunakan.")
            return False

    password = getpass.getpass("Masukkan password: ")
    konfirmasi_password = getpass.getpass("Konfirmasi password: ")
    if password != konfirmasi_password:
        print(">> Error: Password dan konfirmasi password tidak cocok.")
        return False
    if len(password) < 6:
        print(">> Error: Password harus memiliki minimal 6 karakter.")
        return False

    user_id = "U-" + str(uuid.uuid4())[:8]
    salt, hash_password_tersimpan = hash_password(password)

    user_baru = {
        "user_id": user_id,
        "nama": nama,
        "username": username,
        "salt": salt,
        "password": hash_password_tersimpan
    }
    data_akun_user.append(user_baru)
    simpan_json(FILE_AKUN_USER, data_akun_user)

    print(f"\n[INFO] Registrasi berhasil! User ID Anda adalah {user_id}. Silakan login.")
    return True

def login_user():
    print("=== Login User ===")
    username = input("Masukkan username: ").strip().lower()
    password = getpass.getpass("Masukkan password: ")

    data_akun_user = baca_json(FILE_AKUN_USER)
    for user in data_akun_user:
        if user["username"] == username:
            if verifikasi_password(password, user["salt"], user["password"]):
                print(f"\n[INFO] Login berhasil! Selamat datang, {user['nama']}.")
                return user
            else:
                print(">> Error: Password salah.")
                return None

    print(">> Error: Username tidak ditemukan.")
    return None