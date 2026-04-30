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
        sn = input("Masukkan sn: ")
        print("==================\n")
        
        gadget = registrasi_gadget(merk, tipe, harga, sn)
        while gadget == None:
            merk = input("Masukkan merk: ")
            tipe = input("Masukkan tipe: ")
            harga = int(input("Masukkan harga: "))
            sn = input("Masukkan sn: ")
            print("==================\n")
            gadget = registrasi_gadget(merk, tipe, harga, sn)
        inventaris.append(gadget)
        
    print(inventaris)