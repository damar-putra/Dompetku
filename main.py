from auth import authentication
from modules import akun_keuangan

def menu_sebelum_login():
    print("\n" + "=" *40)
    print("=== Aplikasi DompetKu ===")
    print("=" *40)
    print("1. Registrasi User")
    print("2. Login User")
    print("3. Keluar")
    print("=" *40)

def menu_dashboard(user):
    """Menu yang muncul setelah user berhasl login"""
    while True:
        print("\n" + "=" * 40)
        print(f" Dashboard Dompetku - {user['nama']}")
        print("=" * 40)
        print("1. Lihat Akun Keuangan")
        print("2. Tambah Akun Keuangan") #menyusul
        print("3. Manajemen transaksi")
        print("4. Logout")

        pilihan = input("Pilihan menu: ")

        if pilihan == "1":
            akun_keuangan.lihat_akun_keuangan(user["user_id"])
        elif pilihan == "2":
            akun_keuangan.tambah_akun_keuangan(user["user_id"])
        elif pilihan == "3":
            print("\n[INFO] Fitur dalam pengembangan")
        elif pilihan == "4":
            print("\n[INFO] Anda telah logout.")
            break
        else:
            ("\n>> Pilihan tidak valid!")
            continue

def main():
    while True:
        menu_sebelum_login()
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            authentication.registrasi_user()

        elif pilihan == "2":
            user_aktif = authentication.login_user()
            if user_aktif:
                menu_dashboard(user_aktif)

        elif pilihan == "3":
            print("Terima kasih telah menggunakan Aplikasi DompetKu. Sampai jumpa!")
            break
        else:
            print(">> Pilihan tidak valid. Silakan coba lagi.")
            continue

if __name__ == "__main__":
    main()