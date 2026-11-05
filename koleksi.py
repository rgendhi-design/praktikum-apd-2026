# =====================================================================
#  koleksi.py - FITUR UNTUK SEMUA PENGGUNA: lihat (Read) dan cari
# =====================================================================
from data import parfum
from tampilan import (bersihkan_layar, tampil_judul, tampil_tabel,
                      error, tunggu)


def total_nilai(daftar_id):
    """FUNGSI REKURSIF dengan parameter: menjumlahkan harga x stok dari
    setiap ID di daftar_id."""
    if len(daftar_id) == 0:                  # base case: daftar sudah habis
        return 0
    data = parfum[daftar_id[0]]              # parfum pertama di daftar
    # recursive case: parfum pertama + total sisa daftar (lebih pendek 1)
    return data["harga"] * data["stok"] + total_nilai(daftar_id[1:])


def cari_parfum():
    """FUNGSI tanpa parameter: meminta kata kunci, mengembalikan
    dictionary parfum yang cocok."""
    kunci = input("  Kata kunci (nama/brand/aroma) : ").lower()
    if kunci == "":
        raise ValueError("Kata kunci tidak boleh kosong!")
    hasil = {}
    for id_parfum, data in parfum.items():
        if (kunci in data["nama"].lower() or kunci in data["brand"].lower()
                or kunci in data["aroma"].lower()):
            hasil[id_parfum] = data
    return hasil


def lihat_koleksi():
    """PROSEDUR fitur READ: menampilkan semua parfum, jumlah, dan nilai."""
    bersihkan_layar()
    tampil_judul("DAFTAR KOLEKSI PARFUM", 90)
    if len(parfum) == 0:
        print("  Data koleksi masih kosong!")
    else:
        tampil_tabel(parfum)
        print(f"  Total koleksi : {len(parfum)} parfum")
        # fungsi rekursif: argumennya daftar semua ID parfum
        print(f"  Total nilai   : Rp {total_nilai(list(parfum)):,}")
    tunggu()


def fitur_cari():
    """PROSEDUR fitur CARI: cari_parfum() dibungkus try-except."""
    bersihkan_layar()
    tampil_judul("CARI PARFUM", 90)
    try:
        hasil_cari = cari_parfum()           # bisa melempar ValueError
    except ValueError as e:
        error(e)
    else:
        if len(hasil_cari) == 0:
            print("  Parfum tidak ditemukan!")
        else:
            print(f"  Ditemukan {len(hasil_cari)} parfum :")
            tampil_tabel(hasil_cari)
    finally:
        tunggu()
