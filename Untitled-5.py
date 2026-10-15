# =====================================================================
#  SISTEM PENCATATAN KOLEKSI PARFUM
#  Posttest 5 - Praktikum Algoritma Pemrograman Dasar
#  Nama  : Rafie Gendhi S
#  NIM   : 2609106072
#  Kelas : C1'26
# =====================================================================

# ================= [A] INISIALISASI DATA =============================
import os

# Perintah clear terminal disesuaikan dengan sistem operasi
if os.name == "nt":
    perintah_clear = "cls"
else:
    perintah_clear = "clear"

# Data pengguna (NESTED LIST) -> [username, password, role]
users = [
    ["admin", "admin123", "admin"],
    ["sinta", "sinta123", "user"],
]

# Data koleksi parfum (NESTED LIST)
# -> [id, nama, brand, aroma, ukuran_ml, harga, stok]
parfum = [
    [1, "Bleu de Chanel", "Chanel", "Woody Aromatic", 100, 1500000, 5],
    [2, "Sauvage", "Dior", "Fresh Spicy", 60, 1250000, 8],
    [3, "Ombre Nomade", "Louis Vuitton", "Oriental", 100, 5500000, 2],
]

program_berjalan = True

while program_berjalan:
    login_berhasil = False
    role_aktif = ""
    username_aktif = ""

    # ================== MENU LOGIN / REGISTER =======================
    while login_berhasil == False and program_berjalan == True:
        os.system(perintah_clear)
        print("=" * 60)
        print("         SISTEM PENCATATAN KOLEKSI PARFUM")
        print("=" * 60)
        print("  [1] Login")
        print("  [2] Register")
        print("  [3] Keluar Program")
        print("-" * 60)
        pilih_auth = input("  Pilih menu >> ")

        # ==================== [B] FITUR LOGIN ========================
        if pilih_auth == "1":
            os.system(perintah_clear)
            print("=" * 60)
            print("                        LOGIN")
            print("=" * 60)
            nama_login = input("  Username : ")
            sandi_login = input("  Password : ")

            akun_ditemukan = False
            for akun in users:
                if akun[0] == nama_login and akun[1] == sandi_login:
                    akun_ditemukan = True
                    username_aktif = akun[0]
                    role_aktif = akun[2]
                    break

            if akun_ditemukan == True:
                login_berhasil = True
                os.system(perintah_clear)
                print("=" * 60)
                print(f"  Login berhasil! Selamat datang, {username_aktif}")
                print(f"  Status : {role_aktif.upper()}")
                print("=" * 60)
                input("  Tekan ENTER untuk melanjutkan...")
            else:
                print("-" * 60)
                print("  ERROR : Username atau password salah!")
                input("  Tekan ENTER untuk kembali...")

        # =================== [C] FITUR REGISTER ======================
        elif pilih_auth == "2":
            os.system(perintah_clear)
            print("=" * 60)
            print("                       REGISTER")
            print("=" * 60)
            user_baru = input("  Username baru : ")

            if user_baru == "":
                print("-" * 60)
                print("  ERROR : Username tidak boleh kosong!")
            else:
                nama_terpakai = False
                for akun in users:
                    if akun[0] == user_baru:
                        nama_terpakai = True
                        break

                if nama_terpakai == True:
                    print("-" * 60)
                    print("  ERROR : Username sudah digunakan!")
                else:
                    sandi_baru = input("  Password baru : ")
                    if sandi_baru == "":
                        print("-" * 60)
                        print("  ERROR : Password tidak boleh kosong!")
                    else:
                        users.append([user_baru, sandi_baru, "user"])
                        print("-" * 60)
                        print("  Register berhasil! Akun baru berstatus")
                        print("  pengguna biasa. Silakan login.")
            input("  Tekan ENTER untuk kembali...")

        # ========= [D] KELUAR PROGRAM DAN VALIDASI MENU ==============
        elif pilih_auth == "3":
            os.system(perintah_clear)
            print("Terima kasih telah menggunakan program ini!")
            program_berjalan = False

        else:
            print("  ERROR : Pilihan tidak tersedia!")
            input("  Tekan ENTER untuk kembali...")

    # ================ [E] MENU UTAMA APLIKASI =======================
    while login_berhasil == True and program_berjalan == True:
        os.system(perintah_clear)
        print("=" * 60)
        print("         SISTEM PENCATATAN KOLEKSI PARFUM")
        print(f"  Login sebagai : {username_aktif} ({role_aktif})")
        print("=" * 60)

        if role_aktif == "admin":
            print("  [1] Lihat Semua Koleksi        (Read)")
            print("  [2] Cari Parfum")
            print("  [3] Tambah Parfum              (Create)")
            print("  [4] Update Data Parfum         (Update)")
            print("  [5] Hapus Data Parfum          (Delete)")
            print("  [6] Logout")
            print("  [7] Keluar Program")
        else:
            print("  [1] Lihat Semua Koleksi        (Read)")
            print("  [2] Cari Parfum")
            print("  [3] Logout")
            print("  [4] Keluar Program")

        print("-" * 60)
        pilih_menu = input("  Pilih menu >> ")

        # ================== [F] FITUR READ ===========================
        if pilih_menu == "1":
            os.system(perintah_clear)
            print("=" * 95)
            print("                    DAFTAR KOLEKSI PARFUM")
            print("=" * 95)
            if len(parfum) == 0:
                print("  Data koleksi masih kosong!")
            else:
                print(f"  {'ID':<4}{'Nama Parfum':<20}{'Brand':<16}{'Aroma':<17}{'Ukuran (ml)':<12}{'Harga (Rp)':<14}{'Stok':>4}")
                print("-" * 95)
                for data in parfum:
                    print(f"  {data[0]:<4}{data[1]:<20}{data[2]:<16}{data[3]:<17}{data[4]:<12}{data[5]:<14,}{data[6]:>4}")
                print("-" * 95)
                print(f"  Total koleksi : {len(parfum)} parfum")
            input("\n  Tekan ENTER untuk kembali...")

        # ================== [G] FITUR CARI ===========================
        elif pilih_menu == "2":
            os.system(perintah_clear)
            print("=" * 95)
            print("                         CARI PARFUM")
            print("=" * 95)
            kunci = input("  Kata kunci (nama/brand/aroma) : ")

            if kunci == "":
                print("  ERROR : Kata kunci tidak boleh kosong!")
            else:
                hasil_cari = []
                for data in parfum:
                    if (kunci.lower() in data[1].lower()
                            or kunci.lower() in data[2].lower()
                            or kunci.lower() in data[3].lower()):
                        hasil_cari.append(data)

                if len(hasil_cari) == 0:
                    print("  Parfum tidak ditemukan!")
                else:
                    print(f"  Ditemukan {len(hasil_cari)} parfum :")
                    print(f"  {'ID':<4}{'Nama Parfum':<20}{'Brand':<16}{'Aroma':<17}{'Ukuran (ml)':<12}{'Harga (Rp)':<14}{'Stok':>4}")
                    print("-" * 95)
                    for data in hasil_cari:
                        print(f"  {data[0]:<4}{data[1]:<20}{data[2]:<16}{data[3]:<17}{data[4]:<12}{data[5]:<14,}{data[6]:>4}")
                    print("-" * 95)
            input("\n  Tekan ENTER untuk kembali...")

        # ================= [H] FITUR CREATE ==========================
        elif pilih_menu == "3" and role_aktif == "admin":
            os.system(perintah_clear)
            print("=" * 60)
            print("              TAMBAH PARFUM (CREATE)")
            print("=" * 60)

            id_valid = False
            while id_valid == False:
                id_baru = input("  ID Parfum   : ")
                if id_baru == "":
                    print("  ERROR : ID tidak boleh kosong!")
                elif id_baru.isdigit() == False:
                    print("  ERROR : ID harus berupa angka!")
                else:
                    id_baru = int(id_baru)
                    id_terpakai = False
                    for data in parfum:
                        if data[0] == id_baru:
                            id_terpakai = True
                            break
                    if id_terpakai == True:
                        print("  ERROR : ID sudah digunakan, pilih ID lain!")
                    else:
                        id_valid = True

            nama_valid = False
            while nama_valid == False:
                nama_baru = input("  Nama Parfum : ")
                if nama_baru == "":
                    print("  ERROR : Nama tidak boleh kosong!")
                else:
                    nama_valid = True

            brand_valid = False
            while brand_valid == False:
                brand_baru = input("  Brand       : ")
                if brand_baru == "":
                    print("  ERROR : Brand tidak boleh kosong!")
                else:
                    brand_valid = True

            aroma_valid = False
            while aroma_valid == False:
                aroma_baru = input("  Aroma       : ")
                if aroma_baru == "":
                    print("  ERROR : Aroma tidak boleh kosong!")
                else:
                    aroma_valid = True

            ukuran_valid = False
            while ukuran_valid == False:
                ukuran_baru = input("  Ukuran (ml) : ")
                if ukuran_baru == "":
                    print("  ERROR : Ukuran tidak boleh kosong!")
                elif ukuran_baru.isdigit() == False:
                    print("  ERROR : Ukuran harus berupa angka!")
                elif int(ukuran_baru) <= 0:
                    print("  ERROR : Ukuran harus lebih dari 0!")
                else:
                    ukuran_baru = int(ukuran_baru)
                    ukuran_valid = True

            harga_valid = False
            while harga_valid == False:
                harga_baru = input("  Harga (Rp)  : ")
                if harga_baru == "":
                    print("  ERROR : Harga tidak boleh kosong!")
                elif harga_baru.isdigit() == False:
                    print("  ERROR : Harga harus berupa angka!")
                elif int(harga_baru) <= 0:
                    print("  ERROR : Harga harus lebih dari 0!")
                else:
                    harga_baru = int(harga_baru)
                    harga_valid = True

            stok_valid = False
            while stok_valid == False:
                stok_baru = input("  Stok        : ")
                if stok_baru == "":
                    print("  ERROR : Stok tidak boleh kosong!")
                elif stok_baru.isdigit() == False:
                    print("  ERROR : Stok harus berupa angka!")
                else:
                    stok_baru = int(stok_baru)
                    stok_valid = True

            parfum.append([id_baru, nama_baru, brand_baru, aroma_baru,
                           ukuran_baru, harga_baru, stok_baru])
            print("-" * 60)
            print("  Data parfum berhasil ditambahkan!")
            input("  Tekan ENTER untuk kembali...")

        # ================== [I] FITUR UPDATE =========================
        elif pilih_menu == "4" and role_aktif == "admin":
            os.system(perintah_clear)
            print("=" * 60)
            print("              UPDATE PARFUM (UPDATE)")
            print("=" * 60)
            id_ubah = input("  ID parfum yang akan diupdate : ")

            if id_ubah == "":
                print("  ERROR : ID tidak boleh kosong!")
                input("  Tekan ENTER untuk kembali...")
            elif id_ubah.isdigit() == False:
                print("  ERROR : ID harus berupa angka!")
                input("  Tekan ENTER untuk kembali...")
            else:
                id_ubah = int(id_ubah)
                posisi = -1
                for i in range(len(parfum)):
                    if parfum[i][0] == id_ubah:
                        posisi = i
                        break

                if posisi == -1:
                    print("  ERROR : ID tidak ditemukan!")
                    input("  Tekan ENTER untuk kembali...")
                else:
                    print("-" * 60)
                    print(f"  Data ditemukan : {parfum[posisi][1]}")
                    print("  Tekan ENTER untuk mempertahankan nilai lama")
                    print("-" * 60)

                    nama_baru = input(f"  Nama baru    [{parfum[posisi][1]}] : ")
                    if nama_baru != "":
                        parfum[posisi][1] = nama_baru

                    brand_baru = input(f"  Brand baru   [{parfum[posisi][2]}] : ")
                    if brand_baru != "":
                        parfum[posisi][2] = brand_baru

                    aroma_baru = input(f"  Aroma baru   [{parfum[posisi][3]}] : ")
                    if aroma_baru != "":
                        parfum[posisi][3] = aroma_baru

                    ukuran_baru = input(f"  Ukuran (ml)  [{parfum[posisi][4]}] : ")
                    if ukuran_baru != "":
                        if ukuran_baru.isdigit() == True:
                            parfum[posisi][4] = int(ukuran_baru)
                        else:
                            print("  ERROR : Ukuran harus angka, nilai lama dipakai!")

                    harga_baru = input(f"  Harga (Rp)   [{parfum[posisi][5]}] : ")
                    if harga_baru != "":
                        if harga_baru.isdigit() == True:
                            parfum[posisi][5] = int(harga_baru)
                        else:
                            print("  ERROR : Harga harus angka, nilai lama dipakai!")

                    stok_baru = input(f"  Stok baru    [{parfum[posisi][6]}] : ")
                    if stok_baru != "":
                        if stok_baru.isdigit() == True:
                            parfum[posisi][6] = int(stok_baru)
                        else:
                            print("  ERROR : Stok harus angka, nilai lama dipakai!")

                    print("-" * 60)
                    print("  Data parfum berhasil diupdate!")
                    input("  Tekan ENTER untuk kembali...")

        # ================== [J] FITUR DELETE =========================
        elif pilih_menu == "5" and role_aktif == "admin":
            os.system(perintah_clear)
            print("=" * 60)
            print("              HAPUS PARFUM (DELETE)")
            print("=" * 60)
            id_hapus = input("  ID parfum yang akan dihapus : ")

            if id_hapus == "":
                print("  ERROR : ID tidak boleh kosong!")
                input("  Tekan ENTER untuk kembali...")
            elif id_hapus.isdigit() == False:
                print("  ERROR : ID harus berupa angka!")
                input("  Tekan ENTER untuk kembali...")
            else:
                id_hapus = int(id_hapus)
                posisi = -1
                for i in range(len(parfum)):
                    if parfum[i][0] == id_hapus:
                        posisi = i
                        break

                if posisi == -1:
                    print("  ERROR : ID tidak ditemukan!")
                    input("  Tekan ENTER untuk kembali...")
                else:
                    print("-" * 60)
                    print(f"  Nama   : {parfum[posisi][1]}")
                    print(f"  Brand  : {parfum[posisi][2]}")
                    print(f"  Aroma  : {parfum[posisi][3]}")
                    print("-" * 60)
                    konfirmasi = input("  Yakin ingin menghapus? (y/t) : ")

                    if konfirmasi.lower() == "y":
                        parfum.pop(posisi)
                        print("  Data parfum berhasil dihapus!")
                    else:
                        print("  Penghapusan dibatalkan.")
                    input("  Tekan ENTER untuk kembali...")

        # ========= [K] LOGOUT, KELUAR, DAN VALIDASI MENU =============
        elif (pilih_menu == "6" and role_aktif == "admin") or (pilih_menu == "3" and role_aktif == "user"):
            login_berhasil = False
            os.system(perintah_clear)
            print("  Logout berhasil!")
            input("  Tekan ENTER untuk kembali ke menu login...")

        elif (pilih_menu == "7" and role_aktif == "admin") or (pilih_menu == "4" and role_aktif == "user"):
            os.system(perintah_clear)
            print("Terima kasih telah menggunakan program ini!")
            program_berjalan = False

        else:
            print("  ERROR : Pilihan tidak tersedia!")
            input("  Tekan ENTER untuk kembali...")


            git add posttest/posttest-apd-5/
            git status
            