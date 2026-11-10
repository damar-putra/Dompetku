import datetime
import os

DATA_KEUANGAN = "data_keuangan.txt"
DATA_USER = "user_data.txt"

# Modul Akun User
def id_user():
    if not os.path.exists(DATA_USER):
        return 1

    with open(DATA_USER, "r") as file: 
        baris = file.readlines()
        return len(baris) + 1

def registrasi_user():
    print("=== Registrasi User ===")
    nama = input("Masukkan nama lengkap: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    user_id = "ID" + str(id_user()).zfill(3) 
    
    user_sudah_ada = False
    if os.path.exists(DATA_USER):
        with open(DATA_USER, "a") as file:
            for baris in file:
                data = baris.strip().split("|")
                if data[2] == username:
                    user_sudah_ada = True
                    break

    if user_sudah_ada:
        print(">> Error: Username sudah digunakan. Silakan coba lagi.")
        return False
    else:
        with open(DATA_USER, "a") as file:
            file.write(f"{user_id}\n")
    with open("user_data.txt", "a") as file:
        file.write(f"{user_id}|{nama}|{username}|{password}\n")

    print("\nRegistrasi berhasil! Silakan login.")

def login_user():
    print("=== Login User ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if not os.path.exists(DATA_USER):
        print(">> Error: Belum ada user terdaftar. Silakan registrasi terlebih dahulu.")
        return False

    with open(DATA_USER, "r") as file:
        for baris in file:
            data = baris.strip().split("|")
            if len(data) == 4:
                user_id, nama, user_username, user_password = data
                if user_username == username and user_password == password:
                    print(f"\nLogin berhasil! Selamat datang, {nama}.")
                    return True

    print(">> Error: Username atau password salah.")
    return False


# Modul Manajemen transaksi
def metode_pembayaran():
    print("1. Tunai")
    print("2. Transfer")
    print("3. Qris")
    print("4. Lainnya")
    while True:
        pilihan_metode = input("Pilih metode pembayaran: ")
        if pilihan_metode == "1":
            return "Tunai"
        elif pilihan_metode == "2":
            return "Transfer"
        elif pilihan_metode == "3":
            return "Qris"
        elif pilihan_metode == "4":
            return "Lainnya"
        else:
            print(">> Error: Pilihan tidak valid!")

def tambah_pemasukan():
    while True:
        tipe = "Pemasukan"
        try:
            pemasukan = float(input("Masukkan jumlah pemasukan: "))
            if pemasukan <= 0:
                print(">> Error: Jumlah pemasukan tidak boleh negatif!")
                continue
        except ValueError:
            print(">> Error: Input harus berupa angka!")
            continue

        keterangan = input("Keterangan (Misal: Gaji): ")

        metode = metode_pembayaran()

        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(DATA_KEUANGAN, "a") as file:
            file.write(f"{waktu}|{tipe}|{pemasukan}|{keterangan}|{metode}\n")

        print("\nPemasukan berhasil ditambahkan!")
        break

def tambah_pengeluaran():
    while True:
        tipe = "Pengeluaran"
        try:
            pengeluaran = float(input("Masukkan jumlah pengeluaran: "))
            if pengeluaran < 0:
                print(">> Error: Jumlah pengeluaran tidak boleh negatif!")
                continue
        except ValueError:
            print(">> Error: Input harus berupa angka!")
            continue

        keterangan = input("Keterangan (Misal: Makan): ")

        metode = metode_pembayaran()

        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(DATA_KEUANGAN, "a") as file:
            file.write(f"{waktu}|{tipe}|{pengeluaran}|{keterangan}|{metode}\n")

        print("\nPengeluaran berhasil ditambahkan!")
        break

def cek_saldo():
    saldo = 0.0
    if os.path.exists(DATA_KEUANGAN):
        with open(DATA_KEUANGAN, "r") as file:
            for baris in file:
                data = baris.strip().split("|")
                if len(data) == 5:
                    tipe = data[1]
                    jumlah = float(data[2])
                    if tipe == "Pemasukan":
                        saldo += jumlah
                    elif tipe == "Pengeluaran":
                        saldo -= jumlah
    print(f"\nSaldo saat ini: Rp {saldo:,.2f}")

def lihat_riwayat():
    if os.path.exists(DATA_KEUANGAN):
        print("\n=== Riwayat Keuangan ===")
        with open(DATA_KEUANGAN, "r") as file:
            for baris in file:
                data = baris.strip().split("|")
                if len(data) == 5:
                    waktu, tipe, jumlah, keterangan, metode = data
                    print(f"Waktu: {waktu} |Tipe: {tipe} |Jumlah: Rp {float(jumlah):,.2f} |Keterangan: {keterangan} |Metode: {metode}")
    else:
        print("\n>> Belum ada riwayat keuangan.")

def tampilkan_menu():
    print("\n=== Menu Dompetku ===")
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Cek Saldo")
    print("4. Lihat Riwayat Keuangan")
    print("5. Keluar")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_pemasukan()
            input("Tekan Enter untuk kembali ke menu...")
        elif pilihan == "2":
            tambah_pengeluaran()
            input("Tekan Enter untuk kembali ke menu...")
        elif pilihan == "3":
            cek_saldo()
            input("Tekan Enter untuk kembali ke menu...")
        elif pilihan == "4":
            lihat_riwayat()
            input("Tekan Enter untuk kembali ke menu...")
        elif pilihan == "5":
            print("Terima kasih telah menggunakan Dompetku!")
            break
        else:
            print(">> Error: Pilihan tidak valid!")

if __name__ == "__main__":
    main()