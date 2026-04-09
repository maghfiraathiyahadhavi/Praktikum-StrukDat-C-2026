import soal1, soal2, soal3, soal4


def main():
    try:
        inventaris = []
        skema_komisi = (
            (100000000, 10), # Penjualan >= 100jt -> Komisi 10%
            (50000000,  5),  # Penjualan >= 50jt  -> Komisi 5%
            (20000000,  2),  # Penjualan >= 20jt  -> Komisi 2%
            (0,         0)   # Di bawah 20jt      -> Tidak ada komisi
        )
        while True:
            print("=== PyGadget Hub ===")
            print("1. Tambah Gadget")
            print("2. Daftar Inventaris")
            print("3. Update Stok")
            print("4. Cek Komisi")
            print("5. Keluar")

            menu = input("Pilih menu: ")
            print()
            match menu:
                case "1":
                    merk = input("Masukkan merk: ")
                    tipe = input("Masukkan tipe: ")
                    harga = int(input("Masukkan harga: "))
                    sn = input("Masukkan SN: ")
                    gadget = soal1.registrasi_gadget(merk, tipe, harga, sn)
                    if gadget:
                        inventaris.append(gadget)
                        print("Registrasi gadget berhasil!")
                case "2":
                    min_harga = int(input("Masukkkan harga minimal: "))
                    max_harga = int(input("Masukkan harga maksimal: "))
                    result = soal2.filter_harga(inventaris, min_harga, max_harga)
                    if len(result) > 0:
                        print("==================================")
                        for x in result:
                            print(f"Merk: {x["merk"]}")
                            print(f"Tipe: {x["tipe"]}")
                            print(f"Harga: {x["harga"]}")
                            print(f"SN: {x["sn"]}")
                            print(f"Status: {x["status"]}\n")
                    else:
                        print("Tidak ada gadget dalam rentang harga tersebut.")
                case "3":
                    sn_target = input("Masukkan SN: ")
                    tambah = int(input("Masukkan tambahan stok: "))
                    soal3.update_stok(inventaris, sn_target, tambah)
                case "4":
                    nama_sales = input("Masukkan nama sales: ")
                    total_penjualan = int(input("Masukkan total penjualan: "))
                    komisi = soal4.hitung_komisi(total_penjualan, skema_komisi)
                    print(f"Nama Sales: {nama_sales}")
                    print(f"Komisi    : {total_penjualan * (komisi / 100)}")
                case _:
                    break
            
            print("==================================\n")
    except KeyboardInterrupt:
        print()
        pass


if __name__ == "__main__":
    main()


