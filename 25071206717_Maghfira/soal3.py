def update_stok(katalog, sn_target, jumlah_tambah):
    for x in katalog:
        if sn_target == x["sn"]:
            try:
                x["stok"] += jumlah_tambah
            except KeyError:
                x["stok"] = jumlah_tambah
            print(f"Update berhasil! Stok {x["merk"]} {x["tipe"]}: {x["stok"]}")
class Pasien: #class
    jumlah = 0 #variable class

    def __init__(self, id, nama, penyakit):
        self.__id = id #atribut
        self.__nama = nama
        self.__penyakit = penyakit

        Pasien.jumlah += 1

    def get_id(self):   # Get
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_penyakit(self):
        return self.__penyakit

    def tampilkan_info(self):  # Method tampilkan info
        print("ID      :", self.__id)
        print("Nama    :", self.__nama)
        print("Penyakit:", self.__penyakit)

    @staticmethod
    def hitung_pasien():
        return Pasien.jumlah

class PasienPrioritas(Pasien): #class turunan
    def __init__(self, id, nama, penyakit, prioritas):
        super().__init__(id, nama, penyakit)
        self.prioritas = prioritas

    def tampilkan_info(self): # Override method
        super().tampilkan_info()
        print("Prioritas :", self.prioritas)

        if self.prioritas == "Darurat":
            print("** Segera tangani! **")


p1 = Pasien("P001", "Andi", "Flu") # objek
p2 = PasienPrioritas("P007", "Ghani", "Sesak Napas", "Darurat") # objek prioritas

p1.tampilkan_info()
print()
p2.tampilkan_info()

print("\nTotal pasien:", Pasien.hitung_pasien()) #menampilkan total pasien