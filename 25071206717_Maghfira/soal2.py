def filter_harga(data, min_harga, max_harga):
    result = []
    for x in data:
        if (x["harga"] >= min_harga
                and x["harga"] <= max_harga):
            result.append(x)
    return result

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


def info_klinik(): #tuple
    klinik = (
        "Klinik Sehat Bersama",
        "Jl. Merdeka No. 10, Pekanbaru",
        "0761-12345"
    )
    
    print("Info Klinik:")
    print("Nama   :", klinik[0])
    print("Alamat :", klinik[1])
    print("Telp   :", klinik[2])
    
def rekap_penyakit(): #rekap jenis penyakit dengan set
    penyakit_unik = {p["penyakit"] for p in pasien_hari_ini} # set
    
    print("\nJenis Penyakit Unik:", penyakit_unik)
    print("Jumlah jenis penyakit:", len(penyakit_unik))
    
    rekap = {} # menghitung jumlah pasien per penyakit dengan dictionary
    for p in pasien_hari_ini: #loop
        penyakit = p["penyakit"]
        if penyakit in rekap:
            rekap[penyakit] += 1
        else:
            rekap[penyakit] = 1
    
    print("\nRekap per penyakit:") #menampilkan hasil rekap
    for penyakit in rekap:
        print(f"{penyakit} : {rekap[penyakit]} pasien")
    
    maks = max(rekap.values()) #pasien jumlah terbanyak
    
    terbanyak = [p for p in rekap if rekap[p] == maks] # penyakit dengan jumlah terbanyak
    
    print("\nPenyakit terbanyak:", ", ".join(terbanyak), f"({maks} pasien)")
    
info_klinik() #memanggil fungsi untuk  menampilkan output
rekap_penyakit()
