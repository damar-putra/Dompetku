import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

FILE_AKUN_USER = os.path.join(DATA_DIR, "akun_user.json")

FILE_AKUN_KEUANGAN = os.path.join(DATA_DIR, "akun_keuangan.json")