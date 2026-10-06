# =====================================================================
# POSTTEST 4 - ALGORITMA PEMROGRAMAN DASAR
# Program : ATM Sederhana (Login, Cek Saldo, Tarik Tunai, Setor Tunai)
# Nama    : Rafie Gendhi S
# NIM     : 2609106072
# Kelas   : C1
# =====================================================================

# ---------- Data akun (ditulis di source code agar mudah diperiksa) ----------
username_benar = "rafie"
pin_benar = "072"            # PIN = 3 digit terakhir NIM

# ---------- Inisialisasi saldo awal ----------
saldo = 1000000

# ---------- Pengaturan tampilan ----------
lebar = 46
garis = "=" * lebar
garis_tipis = "-" * lebar

print(garis)
print("SELAMAT DATANG DI ATM".center(lebar))
print("BANK NUSANTARA".center(lebar))
print(garis)

# =====================================================================
# 1. SISTEM LOGIN DENGAN PERCOBAAN TERBATAS (maksimal 3 kali)
# =====================================================================
sisa_percobaan = 3
login_berhasil = False

while sisa_percobaan > 0:
    print()
    print("[ LOGIN ]".center(lebar))
    print(garis_tipis)
    username = input("Username : ")
    pin = input("PIN      : ")

    if username == username_benar and pin == pin_benar:
        print("Login Berhasil!")
        login_berhasil = True
        break
    else:
        sisa_percobaan = sisa_percobaan - 1
        if sisa_percobaan > 0:
            print("Login Gagal! Sisa percobaan:", sisa_percobaan)
        else:
            print("Akun Anda Terblokir!")

# =====================================================================
# 3. MENU UTAMA & PERULANGAN PROGRAM (hanya jika login berhasil)
# =====================================================================
if login_berhasil == True:
    while True:
        print()
        print(garis)
        print("MENU UTAMA ATM".center(lebar))
        print(garis)
        print("  [1] Cek Saldo")
        print("  [2] Tarik Tunai")
        print("  [3] Setor Tunai")
        print("  [4] Keluar")
        print(garis_tipis)
        pilihan = input("Pilih menu (1-4) : ")
        print()

        # -------------------------------------------------------------
        # 4. PEMROSESAN TRANSAKSI
        # -------------------------------------------------------------
        if pilihan == "1":
            # ----- Pilihan 1 : Cek Saldo -----
            print("[ CEK SALDO ]".center(lebar))
            print(garis_tipis)
            print(f"Saldo Anda saat ini : Rp {saldo:,}".replace(",", "."))

        elif pilihan == "2":
            # ----- Pilihan 2 : Tarik Tunai -----
            print("[ TARIK TUNAI ]".center(lebar))
            print(garis_tipis)
            print("Pilih kelipatan penarikan:")
            print("  [1] Kelipatan Rp 50.000")
            print("  [2] Kelipatan Rp 100.000")
            pilih_kelipatan = input("Pilihan (1-2) : ")

            kelipatan = 0
            teks_kelipatan = ""
            if pilih_kelipatan == "1":
                kelipatan = 50000
                teks_kelipatan = "50.000"
            elif pilih_kelipatan == "2":
                kelipatan = 100000
                teks_kelipatan = "100.000"

            if kelipatan == 0:
                print("Pilihan kelipatan tidak valid!")
            else:
                nominal_teks = input("Masukkan nominal penarikan : Rp ")

                if nominal_teks.isdigit() == False:
                    print("Nominal harus berupa angka!")
                else:
                    nominal = int(nominal_teks)

                    if nominal <= 0:
                        print("Nominal harus lebih dari 0!")
                    elif nominal % kelipatan != 0:
                        print("Nominal harus kelipatan Rp", teks_kelipatan)
                    elif nominal > saldo:
                        print("Saldo tidak mencukupi!")
                    else:
                        saldo = saldo - nominal
                        print("Transaksi berhasil!")
                        print(f"Nominal ditarik : Rp {nominal:,}".replace(",", "."))
                        print(f"Sisa saldo      : Rp {saldo:,}".replace(",", "."))

        elif pilihan == "3":
            # ----- Pilihan 3 : Setor Tunai -----
            print("[ SETOR TUNAI ]".center(lebar))
            print(garis_tipis)
            nominal_teks = input("Masukkan nominal setoran : Rp ")

            if nominal_teks.isdigit() == False:
                print("Nominal harus berupa angka!")
            else:
                nominal = int(nominal_teks)

                if nominal <= 0:
                    print("Nominal setor harus lebih dari 0!")
                elif nominal % 50000 != 0:
                    print("Nominal harus kelipatan Rp 50.000")
                else:
                    saldo = saldo + nominal
                    print("Setor tunai berhasil!")
                    print(f"Nominal disetor : Rp {nominal:,}".replace(",", "."))
                    print(f"Total saldo     : Rp {saldo:,}".replace(",", "."))

        elif pilihan == "4":
            # ----- Pilihan 4 : Keluar -----
            print(garis)
            print("Terima kasih telah menggunakan ATM kami.".center(lebar))
            print("Sampai jumpa kembali!".center(lebar))
            print(garis)
            break

        else:
            print("Pilihan tidak valid! Masukkan angka 1 - 4.")
