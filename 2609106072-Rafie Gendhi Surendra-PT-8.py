# =====================================================================
#  POSTTEST 8 APD - SISTEM PENCATATAN KOLEKSI PARFUM
#  Pengembangan Posttest 7: output pakai prettytable dan program
#  dipecah menjadi beberapa file. JALANKAN FILE INI.
#
#  data.py      : data global (akun, parfum, kolom, daftar menu)
#  tampilan.py  : semua output (prettytable dan colorama)
#  validasi.py  : validasi input angka
#  akun.py      : login dan register
#  koleksi.py   : lihat dan cari parfum (semua pengguna)
#  admin.py     : tambah, ubah, hapus parfum (khusus admin)
# =====================================================================
from data import menu_awal, menu_user, menu_admin
from tampilan import bersihkan_layar, tampil_menu, error, tunggu
from akun import login, register
from koleksi import lihat_koleksi, fitur_cari
from admin import tambah_parfum, ubah_parfum, hapus_parfum

program_jalan = True
akun_aktif = None          # None = belum login, atau (username, role)

# ========================= [A] MENU AWAL =============================
while program_jalan:
    bersihkan_layar()
    tampil_menu("SISTEM PENCATATAN KOLEKSI PARFUM", menu_awal)
    pilih_awal = input("  Pilih menu >> ")

    if pilih_awal == "1":
        akun_aktif = login()                 # fungsi tanpa parameter
    elif pilih_awal == "2":
        register()                           # prosedur tanpa parameter
    elif pilih_awal == "3":
        bersihkan_layar()
        print("Terima kasih telah menggunakan program ini!")
        program_jalan = False
    else:
        error("Pilihan tidak tersedia!")
        tunggu()

    # ================= [B] MENU UTAMA (MULTIUSER) ====================
    while akun_aktif is not None and program_jalan:
        nama_aktif, role_aktif = akun_aktif
        daftar_menu = menu_admin if role_aktif == "admin" else menu_user
        bersihkan_layar()
        tampil_menu(f"MENU {role_aktif.upper()} - {nama_aktif}", daftar_menu)
        pilih_menu = input("  Pilih menu >> ")

        if pilih_menu == "1":
            lihat_koleksi()                  # Read
        elif pilih_menu == "2":
            fitur_cari()                     # Cari
        elif pilih_menu == "3" and role_aktif == "admin":
            tambah_parfum()                  # Create
        elif pilih_menu == "4" and role_aktif == "admin":
            ubah_parfum()                    # Update
        elif pilih_menu == "5" and role_aktif == "admin":
            hapus_parfum()                   # Delete
        elif pilih_menu == "8":
            akun_aktif = None                # kembali ke menu awal
            bersihkan_layar()
            print("  Logout berhasil!")
            tunggu("Tekan ENTER untuk kembali ke menu awal...")
        elif pilih_menu == "9":
            bersihkan_layar()
            print("Terima kasih telah menggunakan program ini!")
            program_jalan = False
        else:
            error("Pilihan tidak tersedia!")
            tunggu()
