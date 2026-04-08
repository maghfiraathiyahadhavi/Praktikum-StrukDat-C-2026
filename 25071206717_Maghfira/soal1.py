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



pasien_hari_ini = [
    {"id": "P001", "nama": "Andi",  "usia": 34, "penyakit": "Flu",   "bayar": False},
    {"id": "P002", "nama": "Budi",  "usia": 22, "penyakit": "Tifus", "bayar": True},
    {"id": "P003", "nama": "Cici",  "usia": 45, "penyakit": "Flu",   "bayar": False},
    {"id": "P004", "nama": "Dani",  "usia": 30, "penyakit": "Maag",  "bayar": True},
    {"id": "P005", "nama": "Eva",   "usia": 28, "penyakit": "Tifus", "bayar": False},
    {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag",  "bayar": False},
]

def tampilkan_pasien(): #menampilkan data pasien
    print("===== DATA PASIEN ====")
    print("No | ID   | Nama  | Usia | Penyakit | Status Bayar")
    
    for i in range(len(pasien_hari_ini)): #looping
        n = pasien_hari_ini[i]  
        status = "Lunas" if n["bayar"] else "Belum Bayar"
        print(f"{i+1} | {n['id']} | {n['nama']} | {n['usia']} | {n['penyakit']} | {status}")
        
def filter_belum_bayar(): #list pasien yg belum bayar
    belum = []

    for p in pasien_hari_ini: #loop
        if not p["bayar"]:
            belum.append(p["nama"]) #list comprehension
    
    belum.sort()    # sorting
    
    print("\n===== PASIEN BELUM BAYAR =====") #menampilkan pasien yg belum bayar
    for i in range(len(belum)):
        print(f"{i+1}. {belum[i]}")

    print("Total belum bayar:", len(belum))

tampilkan_pasien() #memanggil fungsi untuk output
filter_belum_bayar() 
