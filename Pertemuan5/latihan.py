#1
stok_barang = [15, 40, 30, 10, 25]

stok_barang[3]= 50
print(stok_barang)

stok_barang.append(5)
print(stok_barang)

stok_barang.sort(reverse=True)
print(stok_barang)

jumlah= sum(stok_barang)
print(jumlah)

rata= jumlah/len(stok_barang)
print('aman') if rata>20 else print('waspada')



#2
data_aktivitas = [("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]

d1, d2, d3, d4 =data_aktivitas
for x in data_aktivitas:
   nama, poin = x

   if poin > 80:
      print(f"{nama} mendapatkan predikat gold")
   elif 50 >= poin <= 80:
      print(f"{nama} mendapatkan predikat silver")

   else:
      print(f"{nama} mendapatkan predikat bronze")






#3
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

irisan = ukm_coding - ukm_robotik
print(irisan)

salah_satu = ukm_coding.union(ukm_robotik)
print(salah_satu)

print("andi" in ukm_robotik)



#4
gudang_pc = [
{"item": "Monitor", "harga": 1500000, "stok": 5},
{"item": "Keyboard", "harga": 400000, "stok": 12},
{"item": "Mouse", "harga": 250000, "stok": 20}
]


gudang_pc[1]["kategori"] = "Aksesoris"
gudang_pc.append({"item": "Headset", "harga": 350000, "stok": 8},)
print(gudang_pc)


for x in gudang_pc: 
   total = x['harga'] * x['stok']
   print(f'items : {x['harga']} | Total_aset : Rp{total}')