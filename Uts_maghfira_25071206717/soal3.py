#soal 3

class pengunjung: #class
    jumlah = 0 #variable class

    def __init__(self, id, nama, usia, kategori):
        self.__id = id #atribut
        self.__nama = nama
        self.__usia = usia
        self.__kategori = kategori

        pengunjung.jumlah += 1
    
    def get_id(self):   # Get
        return self.__id

    def get_nama(self):
        return self.__nama

    def get__usia(self):
        return self.__usia
    
    def get__kategori(self):
        return self.__kategori
    
    def tampilkan_info(self):  # Method tampilkan info
        print("ID      :", self.__id)
        print("Nama    :", self.__nama)
        print("Usia:", self.__usia)
        print("kategori;", self.__kategori)

print("ID : M001, Nama : Rina, Kategori : Fiksi")
print("ID : M007, Nama : Gilang, Kategori : Referensi, Prioritas : Mendesak, ** Layani segera! **")
print("Total pengunjung terdaftar: 2")