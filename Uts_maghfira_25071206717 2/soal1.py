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

#soal 1

def pengunjung_hari_ini ():
    print("===== DATA PENGUNJUNG ====")
    print("ID | Nama | Usia | Kategori | Kembali")

    for i in range(len(pengunjung_hari_ini)): #looping
        n = pengunjung_hari_ini
        kembali = "True" if n ["sudah"] else "False"
        print("{i+1} | {n['Id']} | {n['Nama']} | {n['Usia']} | {n['Kategori']} | {Kembali}")
        
def filter_belum_kembali(): #list pengujung belum kembali
    belum = [] 

    for p in pengunjung_hari_ini: #loop
        if not p["kembali"]:
            belum.append(p["nama"]) #list comprehension

    belum.sort ()

    print("\n=====  BELUM KEMBALI =====") 
    for i in range(len(belum)):
        print(f"{i+1}. {belum[i]}")
    
        print("Total belum kembali:", len(belum))


