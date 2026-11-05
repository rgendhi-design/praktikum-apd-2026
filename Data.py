# =====================================================================
#  data.py - DATA GLOBAL (akun, koleksi parfum, kolom, daftar menu)
#  File lain memakainya lewat: from data import users, parfum, ...
# =====================================================================

# Akun (DICTIONARY) -> {username: {"password": ..., "role": ...}}
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "sinta": {"password": "sinta123", "role": "user"},
}

# Koleksi parfum (DICTIONARY BERSARANG) -> {id: {nama, brand, aroma, ...}}
parfum = {
    1: {"nama": "Bleu de Chanel", "brand": "Chanel", "aroma": "Woody Aromatic",
        "ukuran": 100, "harga": 1500000, "stok": 5},
    2: {"nama": "Sauvage", "brand": "Dior", "aroma": "Fresh Spicy",
        "ukuran": 60, "harga": 1250000, "stok": 8},
    3: {"nama": "Ombre Nomade", "brand": "Louis Vuitton", "aroma": "Oriental",
        "ukuran": 100, "harga": 5500000, "stok": 2},
}

# Kolom data parfum: (key, label, batas angka terkecil / None = teks)
kolom_parfum = (
    ("nama", "Nama Parfum", None),
    ("brand", "Brand", None),
    ("aroma", "Aroma", None),
    ("ukuran", "Ukuran (ml)", 1),
    ("harga", "Harga (Rp)", 1),
    ("stok", "Stok", 0),
)

# Daftar menu: (nomor, nama menu). Dicetak oleh tampil_menu()
menu_awal = (
    ("1", "Login"),
    ("2", "Register"),
    ("3", "Keluar Program"),
)
menu_user = (
    ("1", "Lihat Semua Koleksi"),
    ("2", "Cari Parfum"),
    ("8", "Logout"),
    ("9", "Keluar Program"),
)
# Menu admin = menu pengguna + tiga menu CRUD di tengahnya
menu_admin = menu_user[:2] + (
    ("3", "Tambah Parfum"),
    ("4", "Update Data Parfum"),
    ("5", "Hapus Data Parfum"),
) + menu_user[2:]
