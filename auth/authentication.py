import os

AKUN_USER = "data/akun_user.txt"

def menu_awal():
    print("=== Selamat Datang di Dompetku ===")
    print("1. Registrasi User")
    print("2. Login User")
    print("3. Keluar")


def id_user():
    if not os.path.exists(AKUN_USER):
        return 1

    with open(AKUN_USER, "r") as file: 
        baris = file.readlines()
        return len(baris) + 1

def registrasi_user():
    print("=== Registrasi User ===")
    nama = input("Masukkan nama lengkap: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    user_id = "ID" + str(id_user()).zfill(3) 
    
    user_sudah_ada = False
    if os.path.exists(AKUN_USER):
        with open(AKUN_USER, "r") as file:
            for baris in file:
                data = baris.strip().split("|")
                if data[2] == username:
                    user_sudah_ada = True
                    break

    if user_sudah_ada:
        print(">> Error: Username sudah digunakan. Silakan coba lagi.")
        return False
    else:
        with open(AKUN_USER, "a") as file:
            file.write(f"{user_id}|{nama}|{username}|{password}\n")
        print("\nRegistrasi berhasil! Silakan login.")
        return True

def login_user():
    while True:
        print("=== Login User ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if not os.path.exists(AKUN_USER):
            print(">> Error: Belum ada user terdaftar. Silakan registrasi terlebih dahulu.")
            return False

        with open(AKUN_USER, "r") as file:
            for baris in file:
                data = baris.strip().split("|")
                if len(data) == 4:
                    user_id, nama, user_username, user_password = data
                    if user_username == username and user_password == password:
                        print(f"\nLogin berhasil! Selamat datang, {nama}.")
                        return True

        print(">> Error: Username atau password salah.")
        return False

