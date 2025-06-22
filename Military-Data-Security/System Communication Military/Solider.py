from cryptography.fernet import Fernet
import bcrypt
import json
from datetime import datetime
from getpass import getpass
from colorama import init, Fore
import os

init(autoreset=True)

DATA_FILE = "data_rahasia.json"
KEY_FILE = "key.key"
LOG_FILE = "log_akses.txt"

# Fungsi baca file JSON
def baca_data():
    if not os.path.exists(DATA_FILE):
        print(Fore.RED + "❌ File pesan tidak ditemukan.")
        return None
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Fungsi untuk validasi waktu
def pesan_masih_aktif(expired_at_str):
    expired_at = datetime.fromisoformat(expired_at_str)
    return datetime.now() <= expired_at

# Fungsi log akses
def catat_log(status):
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, "a") as log:
        log.write(f"{timestamp} - Status: {status}\n")

# Fungsi baca key dari file
def ambil_key():
    if not os.path.exists(KEY_FILE):
        print(Fore.RED + "❌ File key tidak ditemukan.")
        return None
    with open(KEY_FILE, "rb") as f:
        return f.read()

# Contoh penggunaan lambda & list comprehension untuk menampilkan metadata pesan
def tampilkan_metadata(data):
    print(Fore.MAGENTA + "\n📌 Metadata Pesan:")
    metadata = {k: v for k, v in data.items() if k not in ["pesan_enkripsi", "token_hash"]}
    [print(Fore.YELLOW + f"{k.capitalize()}: {v}") for k, v in metadata.items()]

def baca_pesan():
    print(Fore.CYAN + "\n=== MODE PASUKAN: BACA PESAN RAHASIA ===")

    data = baca_data()
    if not data:
        return

    tampilkan_metadata(data)

    key_input = getpass("🔑 Masukkan kunci enkripsi (dari Komandan): ").encode()
    token_input = getpass("🔐 Masukkan token akses: ").encode()

    if not pesan_masih_aktif(data["berlaku_sampai"]):
        print(Fore.RED + "❌ Pesan sudah kadaluarsa!")
        catat_log("Gagal - Kadaluarsa")
        return

    try:
        cipher = Fernet(key_input)
    except Exception:
        print(Fore.RED + "❌ Kunci enkripsi tidak valid.")
        catat_log("Gagal - Kunci Salah")
        return

    hashed_token = data["token_hash"].encode()
    if not bcrypt.checkpw(token_input, hashed_token):
        print(Fore.RED + "❌ Token salah! Akses ditolak.")
        catat_log("Gagal - Token Salah")
        return

    try:
        decrypted_msg = cipher.decrypt(data["pesan_enkripsi"].encode()).decode()
        print(Fore.GREEN + "\n📩 Pesan Rahasia:")
        print(Fore.YELLOW + decrypted_msg)
        catat_log("Berhasil")
    except Exception:
        print(Fore.RED + "❌ Gagal mendekripsi pesan.")
        catat_log("Gagal - Dekripsi Gagal")

if __name__ == "__main__":
    baca_pesan()
