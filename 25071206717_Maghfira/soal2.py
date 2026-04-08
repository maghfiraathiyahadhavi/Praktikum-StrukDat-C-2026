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

def info_klinik():
    info = ("Klinik Sehat Bersama", "Jl. Merdeka No.10", "0761-12345")
    
    print("Info Klinik:")
    print("Nama   :", info[0])
    print("Alamat :", info[1])
    print("Telp   :", info[2])

def rekap_penyakit():
    unik = set([p["penyakit"] for p in pasien_hari_ini])
    print("\nJenis Penyakit Unik:", unik)
    print("Jumlah jenis penyakit:", len(unik))
    
    frek = {}
    for p in pasien_hari_ini:
        penyakit = p["penyakit"]
        frek[penyakit] = frek.get(penyakit, 0) + 1
    
    print("\nRekap per penyakit:")
    for k, v in frek.items():
        print(f"{k} : {v} pasien")
    
    maks = max(frek.values())
    hasil = [k for k in frek if frek[k] == maks]
    
    print("Penyakit terbanyak:", ", ".join(hasil), f"({maks} pasien)")

info_klinik()
rekap_penyakit()