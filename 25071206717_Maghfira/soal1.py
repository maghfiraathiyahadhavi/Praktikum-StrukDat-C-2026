def registrasi_gadget(merk, tipe, harga, sn):
    if harga <= 1000000:
        print("Harga harus diatas 1.000.000")
        return
    elif len(sn) < 5:
        print("SN harus berisi minimal 5 karakter")
        return
    
    return {
        "merk": merk,
        "tipe": tipe,
        "harga": harga,
        "sn": sn,
        "status": "Tersedia"
    }

def main():
    inventaris = []
    for x in range(3):
        merk = input("Masukkan merk: ")
        tipe = input("Masukkan tipe: ")
        harga = int(input("Masukkan harga: "))
        sn = input("Masukkan SN: ")
        print("==================\n")
        
        gadget = registrasi_gadget(merk, tipe, harga, sn)
        while gadget == None:
            merk = input("Masukkan merk: ")
            tipe = input("Masukkan tipe: ")
            harga = int(input("Masukkan harga: "))
            sn = input("Masukkan SN: ")
            print("==================\n")
            gadget = registrasi_gadget(merk, tipe, harga, sn)
        inventaris.append(gadget)
        
    print(inventaris)


if __name__ == "__main__":
    main()

pasien_hari_ini = [
    {"id": "P001", "nama": "Andi",  "usia": 34, "penyakit": "Flu",   "bayar": False},
    {"id": "P002", "nama": "Budi",  "usia": 22, "penyakit": "Tifus", "bayar": True},
    {"id": "P003", "nama": "Cici",  "usia": 45, "penyakit": "Flu",   "bayar": False},
    {"id": "P004", "nama": "Dani",  "usia": 30, "penyakit": "Maag",  "bayar": True},
    {"id": "P005", "nama": "Eva",   "usia": 28, "penyakit": "Tifus", "bayar": False},
    {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag",  "bayar": False},
]

def tampilkan_pasien():
    print("===== DATA PASIEN KLINIK =====")
    print("No | ID   | Nama  | Usia | Penyakit | Status Bayar")
    
    for i, p in enumerate(pasien_hari_ini, 1):
        status = "Lunas" if p["bayar"] else "Belum Bayar"
        print(f"{i}  | {p['id']} | {p['nama']} | {p['usia']} | {p['penyakit']} | {status}")

def filter_belum_bayar():
    # list comprehension
    belum = [p["nama"] for p in pasien_hari_ini if not p["bayar"]]
    
    # sorting
    belum.sort()
    
    print("\n===== PASIEN BELUM BAYAR =====")
    for i, nama in enumerate(belum, 1):
        print(f"{i}. {nama}")
    
    print("Total belum bayar:", len(belum))

tampilkan_pasien()
filter_belum_bayar()