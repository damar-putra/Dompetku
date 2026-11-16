from auth import authentication

def menu_sebelum_login():
    print("\n" + "=" *40)
    print("=== Aplikasi DompetKu ===")
    print("=" *40)
    print("1. Registrasi User")
    print("2. Login User")
    print("3. Keluar")
    print("=" *40)

def main():
    while True:
        menu_sebelum_login()
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            authentication.registrasi_user()

        elif pilihan == "2":
            user_aktif = authentication.login_user()
            if user_aktif:
                print(f"\n Dasboard untuk {user_aktif['nama']} belum dibuat.") #sementara, cuma tes
                input("Tekan Enter untuk kembali ke menu utama...")

        elif pilihan == "3":
            print("Terima kasih telah menggunakan Aplikasi DompetKu. Sampai jumpa!")
            break
        else:
            print(">> Pilihan tidak valid. Silakan coba lagi.")
            continue

if __name__ == "__main__":
    main()