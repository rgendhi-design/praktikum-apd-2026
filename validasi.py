# =====================================================================
#  validasi.py - VALIDASI INPUT (error handling dengan try-except)
# =====================================================================
from tampilan import error


def input_angka(pesan, batas_bawah):
    """FUNGSI dengan parameter: meminta bilangan bulat >= batas_bawah,
    diulang sampai input benar."""
    while True:
        try:
            angka = int(input(pesan))
            if angka < batas_bawah:
                raise ValueError("terlalu kecil")
        except ValueError:
            error(f"Input harus angka bulat minimal {batas_bawah}!")
        else:
            return angka
