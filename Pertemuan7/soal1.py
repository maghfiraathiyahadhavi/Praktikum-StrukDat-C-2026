#nomor 1

["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

def pisah_ganjil_genap(plat_array):
    ganjil = []
    genap = []

    for plat in plat_array:
        posisi = plat.split()
        nomor = posisi[1]

        angka_terakhir = int(nomor[-1])

        if angka_terakhir % 2 == 0:
            genap.append(plat)
        else:
            ganjil.append(plat)

    return ganjil, genap

data_plat = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

ganjil, genap = pisah_ganjil_genap(data_plat)

print("Plat Ganjil", ganjil)
print("Plat Genap", genap)