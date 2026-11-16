import uuid
from config.settings import FILE_AKUN_KEUANGAN
from utils.storage import baca_json, simpan_json

def lihat_akun_keuangan(user_id):
    """Fungsi untuk melihat semua akun keuangan."""
    print("\n=== Daftar Akun Keuangan ===")
    akun_keuangan = baca_json(FILE_AKUN_KEUANGAN)

    akun_user = [akun for akun in akun_keuangan if akun["user_id"] == user_id]

    if not akun_user:
        print("Belum ada akun keuangan yang terdaftar.")
        return

    print(f"{'ID AKUN':<12} | {'NAMA AKUN':<20} | {'SALDO AWAL':<15}")
    print("-" * 60)
    for akun in akun_user:
        saldo_format = f"Rp {akun['saldo_awal']:,}".replace(",", ".")
        print(f"{akun['account_id']:<12} | {akun['nama_akun']:<20} | {saldo_format:<15}")

def tambah_akun_keuangan(user_id):
    """Fungsi untuk menambahkan akun keuangan baru."""
    print("\n=== Tambah Akun Keuangan ===")
    nama_akun = input("Masukkan nama akun: ")
    if not nama_akun:
        print(">> Error: Nama akun tidak boleh kosong.")
        return

    print("Tipe Akun: 1. Tunai | 2. Bank | 3. E-Wallet | 4. Lainnya")
    tipe_input = input("Pilih Tipe: ").strip()

    if tipe_input == "1":
        tipe = "Tunai"
    elif tipe_input == "2":
        tipe = "Bank"
    elif tipe_input == "3":
        tipe = "E-Wallet"
    elif tipe_input == "4":
        tipe = input("Tipe Akun: ")
    else:
        print(">> Error: Pilihan tidak valid")
        return

    while True:
        try:
            saldo_awal = int(input("Masukkan Saldo Awal: Rp").replace(".", "").replace(",", ""))
            if saldo_awal < 0:
                print(">> Error: Saldo awal tidak boleh minus.")
                continue
            break
        except ValueError:
            print(">> Error: Harap masukkan angka yang valid.")

    # Membuat ID unik untuk akun keuangan baru
    account_id = "ACC-" + str(uuid.uuid4())[:8]

    akun_baru = {
        "account_id": account_id,
        "user_id": user_id,
        "nama_akun": nama_akun,
        "tipe": tipe,
        "saldo_awal": saldo_awal,
        "status": "Aktif"
    }

    data_akun = baca_json(FILE_AKUN_KEUANGAN)
    data_akun.append(akun_baru)
    simpan_json(FILE_AKUN_KEUANGAN, data_akun)

    print(f"Akun keuangan '{nama_akun}' berhasil ditambahkan dengan ID: {account_id}.")