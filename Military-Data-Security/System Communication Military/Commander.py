from cryptography.fernet import Fernet
import bcrypt
import json
from datetime import datetime, timedelta
from getpass import getpass
from colorama import init, Fore
import os

init(autoreset=True)

DATA_FILE = "data_rahasia.json"
KEY_FILE = "key.key"

# Fungsi rekursif untuk memastikan input angka valid
def input_angka(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print(Fore.RED + "Masukkan harus berupa angka.")
        return input_angka(prompt)

# Fungsi membuat set validasi level akses
def validasi_akses(level):
    return level.lower() in {"umum", "terbatas", "rahasia"}

# Fungsi scoping dan pembuatan pesan
def buat_pesan():
    if not os.path.exists(KEY_FILE):
        with open(KEY_FILE, "wb") as f:
            f.write(Fernet.generate_key())

    with open(KEY_FILE, "rb") as f:
        kunci_fernet = Fernet(f.read())

    print(Fore.CYAN + "\n=== MODE KOMANDAN: BUAT PESAN RAHASIA ===")

    pangkat_pengirim = input("Masukkan pangkat Anda: ")
    pesan_rahasia = input("Masukkan isi pesan: ")
    token_rahasia = getpass("Buat token akses: ")
    
    # Gunakan loop untuk validasi level akses
    while True:
        level_akses = input("Level akses pesan (Umum/Terbatas/Rahasia): ")
        if validasi_akses(level_akses):
            break
        print(Fore.RED + "Level akses tidak valid.")

    masa_berlaku_menit = input_angka("Pesan aktif selama berapa menit? ")

    hashed_token = bcrypt.hashpw(token_rahasia.encode(), bcrypt.gensalt()).decode()
    pesan_terenkripsi = kunci_fernet.encrypt(pesan_rahasia.encode()).decode()
    waktu_kedaluwarsa = (datetime.now() + timedelta(minutes=masa_berlaku_menit)).isoformat()

    data_pesan = {
        "pengirim": pangkat_pengirim,
        "level_akses": level_akses.capitalize(),
        "pesan_enkripsi": pesan_terenkripsi,
        "token_hash": hashed_token,
        "berlaku_sampai": waktu_kedaluwarsa
    }

    with open(DATA_FILE, "w") as f:
        json.dump(data_pesan, f, indent=2)

    print(Fore.GREEN + "\n✅ Pesan berhasil dienkripsi dan disimpan.")
    print(Fore.BLUE + f"📅 Pesan berlaku sampai: {waktu_kedaluwarsa}")

if __name__ == "__main__":
    buat_pesan()
