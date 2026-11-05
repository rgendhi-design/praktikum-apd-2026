# =====================================================================
#  admin.py - FITUR KHUSUS ADMIN: tambah (Create), ubah (Update),
#             dan hapus (Delete) data parfum
# =====================================================================
from data import parfum, kolom_parfum
from tampilan import (bersihkan_layar, tampil_judul, tampil_detail,
                      error, sukses, tunggu)
from validasi import input_angka


def tambah_parfum():
    """PROSEDUR fitur CREATE: menambah satu parfum baru."""
    bersihkan_layar()
    tampil_judul("TAMBAH PARFUM (CREATE)")
    while True:                              # ulangi sampai ID valid
        try:
            id_baru = input_angka("  ID Parfum    : ", 1)
            if id_baru in parfum:
                raise ValueError("ID sudah digunakan, pilih ID lain!")
        except ValueError as e:
            error(e)
        else:
            break
    data_baru = {}
    for kolom, label, batas in kolom_parfum:
        if batas is None:                    # kolom teks: tidak boleh kosong
            isian = ""
            while isian == "":
                isian = input(f"  {label:<13}: ")
                if isian == "":
                    error(f"{label} tidak boleh kosong!")
            data_baru[kolom] = isian
        else:                                # kolom angka
            data_baru[kolom] = input_angka(f"  {label:<13}: ", batas)
    parfum[id_baru] = data_baru
    print("-" * 60)
    sukses("Data parfum berhasil ditambahkan!")
    tunggu()


def ubah_parfum():
    """PROSEDUR fitur UPDATE: mengubah data parfum berdasarkan ID."""
    bersihkan_layar()
    tampil_judul("UPDATE PARFUM (UPDATE)")
    id_ubah = input_angka("  ID parfum yang akan diupdate : ", 1)
    try:
        data = parfum[id_ubah]               # KeyError kalau ID tidak ada
    except KeyError:
        error("ID tidak ditemukan!")
    else:
        print("  Data lama :")
        tampil_detail(data)
        print("  Tekan ENTER untuk mempertahankan nilai lama")
        print("-" * 60)
        for kolom, label, batas in kolom_parfum:
            isian = input(f"  {label:<13}[{data[kolom]}] : ")
            if isian != "":
                if batas is None:
                    data[kolom] = isian
                else:
                    try:
                        nilai = int(isian)
                        if nilai < batas:
                            raise ValueError("terlalu kecil")
                    except ValueError:
                        error(f"{label} harus angka bulat minimal "
                              f"{batas}, nilai lama dipakai!")
                    else:
                        data[kolom] = nilai
        print("-" * 60)
        sukses("Data parfum berhasil diupdate!")
    finally:
        tunggu()


def hapus_parfum():
    """PROSEDUR fitur DELETE: menghapus parfum setelah konfirmasi."""
    bersihkan_layar()
    tampil_judul("HAPUS PARFUM (DELETE)")
    id_hapus = input_angka("  ID parfum yang akan dihapus : ", 1)
    try:
        data = parfum[id_hapus]              # KeyError kalau ID tidak ada
    except KeyError:
        error("ID tidak ditemukan!")
    else:
        tampil_detail(data)
        konfirmasi = input("  Yakin ingin menghapus? (y/t) : ")
        if konfirmasi.lower() == "y":
            parfum.pop(id_hapus)
            sukses("Data parfum berhasil dihapus!")
        else:
            print("  Penghapusan dibatalkan.")
    finally:
        tunggu()
