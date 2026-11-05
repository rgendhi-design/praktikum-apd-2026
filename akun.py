# =====================================================================
#  akun.py - LOGIN DAN REGISTER (bagian multiuser)
# =====================================================================
from data import users
from tampilan import (bersihkan_layar, tampil_judul, error, sukses,
                      tunggu)


def login():
    """FUNGSI tanpa parameter: mengembalikan (username, role) kalau
    berhasil, atau None kalau gagal."""
    bersihkan_layar()
    tampil_judul("LOGIN")
    nama = input("  Username : ").lower()
    sandi = input("  Password : ")
    try:
        if nama not in users or users[nama]["password"] != sandi:
            raise ValueError("Username atau password salah!")
    except ValueError as e:
        print("-" * 60)
        error(e)
        akun = None
    else:
        akun = (nama, users[nama]["role"])
        print("-" * 60)
        sukses(f"Login berhasil! Selamat datang, {akun[0]} ({akun[1]})")
    finally:
        tunggu("Tekan ENTER untuk melanjutkan...")
    return akun


def register():
    """PROSEDUR tanpa parameter: membuat akun baru, role selalu "user"
    (tanpa return)."""
    bersihkan_layar()
    tampil_judul("REGISTER")
    # lower() agar "ADMIN" dan "admin" dianggap username yang sama
    nama_baru = input("  Username baru : ").lower()
    try:
        if nama_baru == "":
            raise ValueError("Username tidak boleh kosong!")
        if nama_baru in users:
            raise ValueError("Username sudah digunakan!")
        sandi_baru = input("  Password baru : ")
        if sandi_baru == "":
            raise ValueError("Password tidak boleh kosong!")
    except ValueError as e:
        print("-" * 60)
        error(e)
    else:
        users[nama_baru] = {"password": sandi_baru, "role": "user"}
        print("-" * 60)
        sukses("Register berhasil! Akun baru berstatus pengguna biasa.")
    finally:
        tunggu()
