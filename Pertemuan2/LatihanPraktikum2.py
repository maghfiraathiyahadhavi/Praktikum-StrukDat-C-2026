#soal1
thislist = [15, 50, 30, 25, 40, 100 ]

thislist.sort()
print(thislist)

rata_rata = sum(thislist) / len(thislist)
print(rata_rata)

thislist = [15, 50, 30, 25, 40 ]

thislist.insert(-2, 75)
print(thislist)

thislist = [15, 50, 30, 25, 40 ]


#soal2
thistuple = ("B001", "Laptop Gaming", "15000000")
print(thistuple[2])

x = ("B001", "Laptop Gaming", "15000000")
y = list(x)
y [2] = "14000000"
x = tuple(y)

print(x)
#menggunakan tuple update

barang = ("B001", "Laptop Gaming", 15000000)

# Unpacking tuple
kode, nama, harga = barang

print("Kode:", kode)
print("Nama:", nama)
print("Harga:", harga)


#soal3

tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}

# Keahlian yang dimiliki oleh kedua tim (irisan)
irisan = tim_frontend & tim_backend
print("Keahlian yang dimiliki kedua tim:", irisan)


#  Keahlian yang hanya dimiliki oleh tim_backend
khusus_backend = tim_backend - tim_frontend
print("Keahlian khusus tim backend:", khusus_backend)


#  Gabungan kedua set (total skill unik)
gabungan = tim_frontend | tim_backend
print("Total keahlian unik:", gabungan)

#soal4

nilai_siswa = {
"S01": {"nama": "Dina", "tugas": 80, "uts": 75,
"uas": 85},
"S02": {"nama": "Abdul Harris", "tugas": 90, "uts":
88, "uas": 92},
"S03": {"nama": "Sheila", "tugas": 70, "uts": 65,
"uas": 70}
}

#  Tambahkan data siswa baru
nilai_siswa["S04"] = {"nama": "Fafa", "tugas": 85, "uts": 80, "uas": 90}


#  Hitung nilai akhir tiap siswa
print("Nilai Akhir Setiap Siswa:")
for kode, data in nilai_siswa.items():
    nilai_akhir = (data["tugas"] * 0.2) + (data["uts"] * 0.3) + (data["uas"] * 0.5)
    print(f"{data['nama']} : {nilai_akhir:.2f}")


#  Tampilkan siswa dengan UAS di atas 80
print("\nSiswa dengan nilai UAS di atas 80:")
for kode, data in nilai_siswa.items():
    if data["uas"] > 80:
        print(data["nama"])