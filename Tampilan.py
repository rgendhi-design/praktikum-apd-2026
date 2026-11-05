# =====================================================================
#  tampilan.py - SEMUA OUTPUT PROGRAM
#  prettytable : tabel koleksi, tabel menu, dan tabel detail data
#  colorama    : warna judul (cyan), ERROR (merah), sukses (hijau)
# =====================================================================
import os
from colorama import Fore, Style, init
from prettytable import PrettyTable
from data import kolom_parfum

init()  # colorama: supaya kode warna juga jalan di terminal Windows

# "cls" di Windows, "clear" di Linux/macOS
perintah_clear = "cls" if os.name == "nt" else "clear"


def warna(teks, kode):
    """FUNGSI dengan parameter: membungkus teks dengan warna colorama."""
    return f"{kode}{teks}{Style.RESET_ALL}"


def bersihkan_layar():
    """PROSEDUR tanpa parameter: membersihkan layar (tanpa return)."""
    os.system(perintah_clear)


def tampil_judul(teks, lebar=60):
    """PROSEDUR: mencetak judul halaman di antara dua garis ===."""
    print(warna("=" * lebar, Fore.CYAN))
    print(warna(teks.center(lebar), Fore.CYAN))
    print(warna("=" * lebar, Fore.CYAN))


def error(teks):
    """PROSEDUR: mencetak pesan kesalahan berwarna merah."""
    print(warna(f"  ERROR : {teks}", Fore.RED))


def sukses(teks):
    """PROSEDUR: mencetak pesan berhasil berwarna hijau."""
    print(warna(f"  {teks}", Fore.GREEN))


def tunggu(pesan="Tekan ENTER untuk kembali..."):
    """PROSEDUR: menahan layar sampai pengguna menekan ENTER."""
    input(f"\n  {pesan}")


def tampil_tabel(data_tampil):
    """PROSEDUR: mencetak dictionary parfum sebagai tabel prettytable."""
    tabel = PrettyTable()
    # kepala tabel: "ID" lalu label setiap kolom di kolom_parfum
    tabel.field_names = ["ID"] + [label for _, label, _ in kolom_parfum]
    tabel.align = "l"
    for kolom in ("ID", "Ukuran (ml)", "Harga (Rp)", "Stok"):
        tabel.align[kolom] = "r"
    tabel.custom_format["Harga (Rp)"] = lambda kolom, nilai: f"{nilai:,}"
    for id_parfum, data in data_tampil.items():
        baris = [data[kunci] for kunci, _, _ in kolom_parfum]
        tabel.add_row([id_parfum] + baris)
    print(tabel)


def tampil_menu(judul, daftar_menu):
    """PROSEDUR: mencetak daftar menu sebagai tabel prettytable."""
    tabel = PrettyTable(["No", "Menu"])
    tabel.title = judul
    tabel.align["Menu"] = "l"
    # kolom Menu dilebarkan supaya judul tidak melebarkan kolom No
    tabel.min_width = {"Menu": len(judul) - 5}
    tabel.add_rows(daftar_menu)
    print(tabel)


def tampil_detail(data):
    """PROSEDUR: mencetak satu parfum sebagai tabel dua kolom."""
    tabel = PrettyTable(["Data", "Isi"])
    tabel.align = "l"
    for kunci, label, _ in kolom_parfum:
        isi = f"{data[kunci]:,}" if kunci == "harga" else data[kunci]
        tabel.add_row([label, isi])
    print(tabel)
