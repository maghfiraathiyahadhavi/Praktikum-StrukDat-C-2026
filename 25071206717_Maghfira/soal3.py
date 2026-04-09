def update_stok(katalog, sn_target, jumlah_tambah):
    for x in katalog:
        if sn_target == x["sn"]:
            try:
                x["stok"] += jumlah_tambah
            except KeyError:
                x["stok"] = jumlah_tambah
            print(f"Update berhasil! Stok {x["merk"]} {x["tipe"]}: {x["stok"]}")
