pengunjung_hari_ini = [
{"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi",
"kembali": False},
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",
"kembali": True},
{"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi",
"kembali": False},
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",
"kembali": True},
{"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains",
"kembali": False},
{"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum",
"kembali": False},
]

#soal 2
def info_perpustakaan():
    perpustakaan = (
        "Perpustakaan Kampus Terpadu",
        "JL. Pendidikan no. 5, Pekanbaru",
        "0761-54321"
    )

    print("\n Info perpustakaan:")
    print("Nama :", perpustakaan [0])
    print("Alamat :", perpustakaan[1])
    print("Nomor Telepon :", perpustakaan[2])

def rekap_kategori ():
    unik =  {p["kategori"] for p in pengunjung_hari_ini}

    print("\n kategori buku unik: ", unik)
    print("Jumlah pengujung: ", (len(unik)))

    rekap = {}
    for p in pengunjung_hari_ini:
        buku = p["buku"]
        rekap[buku] = rekap.get(buku, 0) + 1

    print("\n rekap perbukuan: ")
    for k, v in rekap.items():
        print(f"{k} : {v} buku")
    
    maks = max(rekap.values())
    terbanyak = [p for p in rekap if rekap[p] == maks]

    print("\n Buku terbanyak:", ", ".join(terbanyak), f"({maks} pengunjung)")

info_perpustakaan()
rekap_kategori()