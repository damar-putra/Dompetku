import datetime
import os

FILE_DATA = "data_keuangan.txt"

def tampilkan_menu():
    print("\n=== Menu Dompetku ===")
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Cek Saldo")
    print("4. Lihat Riwayat Keuangan")
    print("5. Keluar")

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

        with open(FILE_DATA, "a") as file:
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

        with open(FILE_DATA, "a") as file:
            file.write(f"{waktu}|{tipe}|{pengeluaran}|{keterangan}|{metode}\n")

        print("\nPengeluaran berhasil ditambahkan!")
        break

def cek_saldo():
    saldo = 0.0
    if os.path.exists(FILE_DATA):
        with open(FILE_DATA, "r") as file:
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
    if os.path.exists(FILE_DATA):
        print("\n=== Riwayat Keuangan ===")
        with open(FILE_DATA, "r") as file:
            for baris in file:
                data = baris.strip().split("|")
                if len(data) == 5:
                    waktu, tipe, jumlah, keterangan, metode = data
                    print(f"Waktu: {waktu} |Tipe: {tipe} |Jumlah: Rp {float(jumlah):,.2f} |Keterangan: {keterangan} |Metode: {metode}")
    else:
        print("\n>> Belum ada riwayat keuangan.")

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