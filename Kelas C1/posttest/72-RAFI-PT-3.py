# POSTTEST 3 - SISTEM TOP UP GAME
# Nama : Rafi
# NIM  : 72

# Data login yang dianggap benar
username_benar = "Rafi"
password_benar = "72"  # 2 digit NIM

print("╔" + "═" * 44 + "╗")
print("║" + "SISTEM TOP UP GAME".center(44) + "║")
print("║" + "Isi saldo game favoritmu di sini".center(44) + "║")
print("╚" + "═" * 44 + "╝")

# 1. Input login
username = input("Username : ")
password = input("Password : ")

# 2. Validasi login dengan IF/ELSE
if username == username_benar and password == password_benar:
    print("\n[ OK ] Login Berhasil\n")

    # 3. Input data top up
    print("Game      : Genshin Impact / Minecraft / Mobile Legends")
    print("Kategori  : Kecil / Menengah / Besar")
    print("Pembayaran: Pulsa / E-Wallet\n")
    id_player = input("ID Player   : ")
    game = input("Nama Game   : ").strip().title()
    kategori = input("Kategori    : ").strip().title()
    metode = input("Pembayaran  : ").strip().title()

    # Cek apakah pilihan user sesuai daftar
    game_valid = game in ("Genshin Impact", "Minecraft", "Mobile Legends")
    kategori_valid = kategori in ("Kecil", "Menengah", "Besar")
    metode_valid = metode in ("Pulsa", "E-Wallet")

    if game_valid and kategori_valid and metode_valid:
        # 4. Harga dasar berdasarkan kategori (IF/ELIF/ELSE)
        if kategori == "Kecil":
            harga_dasar = 15000
        elif kategori == "Menengah":
            harga_dasar = 50000
        else:
            harga_dasar = 150000

        # 5. Biaya admin dengan ternary operator
        biaya_admin = 2500 if metode == "Pulsa" else 500

        # 6. Total bayar
        total_bayar = harga_dasar + biaya_admin

        # Poin plus: tampilkan total, lalu minta uang pembayaran
        print("\n" + "-" * 46)
        print("Total Bayar : Rp " + f"{total_bayar:,}".replace(",", "."))
        print("-" * 46)
        uang_bayar = int(input("Uang dibayarkan : Rp "))

        if uang_bayar < total_bayar:
            print("\n[ X ] Transaksi Gagal Saldo tidak mencukupi")
        else:
            kembalian = uang_bayar - total_bayar

            # Ubah angka jadi format rupiah (contoh 15000 -> Rp 15.000)
            rp_harga = "Rp " + f"{harga_dasar:,}".replace(",", ".")
            rp_admin = "Rp " + f"{biaya_admin:,}".replace(",", ".")
            rp_total = "Rp " + f"{total_bayar:,}".replace(",", ".")
            rp_uang = "Rp " + f"{uang_bayar:,}".replace(",", ".")
            rp_kembali = "Rp " + f"{kembalian:,}".replace(",", ".")

            # 7. Struk pembelian
            print("\n╔" + "═" * 44 + "╗")
            print("║" + "STRUK PEMBELIAN TOP UP".center(44) + "║")
            print("╠" + "═" * 44 + "╣")
            print(f"║ ID Player    : {id_player:<27} ║")
            print(f"║ Nama Game    : {game:<27} ║")
            print(f"║ Kategori     : {kategori:<27} ║")
            print(f"║ Pembayaran   : {metode:<27} ║")
            print("╟" + "─" * 44 + "╢")
            print(f"║ Harga Dasar  : {rp_harga:<27} ║")
            print(f"║ Biaya Admin  : {rp_admin:<27} ║")
            print(f"║ Total Bayar  : {rp_total:<27} ║")
            print(f"║ Uang Bayar   : {rp_uang:<27} ║")
            print(f"║ Kembalian    : {rp_kembali:<27} ║")
            print("╠" + "═" * 44 + "╣")
            print("║" + "Terima kasih, top up berhasil!".center(44) + "║")
            print("╚" + "═" * 44 + "╝")
    else:
        print("\n[ X ] Data tidak valid, transaksi dibatalkan")
else:
    print("\n[ X ] Login Gagal")