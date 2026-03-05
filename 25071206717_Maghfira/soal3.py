def update_stok(katalog, sn_target, jumlah_tambah):
    for x in katalog:
        if sn_target == x["sn"]:
            try:
                x["stok"] += jumlah_tambah
            except KeyError:
                x["stok"] = jumlah_tambah
            print(f"Update berhasil! Stok {x["merk"]} {x["tipe"]}: {x["stok"]}")

def main():
    katalog = [
        {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok':2},
        {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5}
    ]

    daftar_merk = {x["merk"] for x in katalog}
    for x in range(3):
        sn_target = input("Masukkan SN: ")
        tambah = int(input("Masukkan tambahan stok: "))
        update_stok(katalog, sn_target, tambah)
        print("==================\n")

    print(daftar_merk)
    print(katalog)

if __name__ == "__main__":
    main()