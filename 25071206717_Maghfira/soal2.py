def filter_harga(data, min_harga, max_harga):
    result = []
    for x in data:
        if (x["harga"] >= min_harga
                and x["harga"] <= max_harga):
            result.append(x)
    return result

def info_klinik():
    info = ("Klinik Sehat Bersama", "Jl. Merdeka No.10", "0761-12345")
    
    print("Info Klinik:")
    print("Nama   :", info[0])
    print("Alamat :", info[1])
    print("Telp   :", info[2])

def rekap_penyakit():
    data = rekap_penyakit
    
    # set (unik)
    unik = set([p["penyakit"] for p in data])
    print("\nJenis Penyakit Unik:", unik)
    print("Jumlah jenis penyakit:", len(unik))
    
    # frekuensi
    frek = {}
    for p in data:
        penyakit = p["penyakit"]
        frek[penyakit] = frek.get(penyakit, 0) + 1
    
    print("\nRekap per penyakit:")
    for k, v in frek.items():
        print(f"{k} : {v} pasien")
    
    # terbanyak
    maks = max(frek.values())
    hasil = [k for k in frek if frek[k] == maks]
    
    print("Penyakit terbanyak:", ", ".join(hasil), f"({maks} pasien)")

info_klinik()
rekap_penyakit()



