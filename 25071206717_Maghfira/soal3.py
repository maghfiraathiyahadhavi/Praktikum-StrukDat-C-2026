def update_stok(katalog, sn_target, jumlah_tambah):
    for x in katalog:
        if sn_target == x["sn"]:
            try:
                x["stok"] += jumlah_tambah
            except KeyError:
                x["stok"] = jumlah_tambah
            print(f"Update berhasil! Stok {x["merk"]} {x["tipe"]}: {x["stok"]}")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AntrianPasien:
    def __init__(self):
        self.head = None

    def tambah(self, data):   # tambah di akhir (FIFO)
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def tampilkan(self): # tampilkan antrian
        print("\n===== ANTRIAN PASIEN =====")
        current = self.head
        i = 1
        
        while current:
            d = current.data
            print(f"[{i}] {d['id']} - {d['nama']} | {d['penyakit']}")
            current = current.next
            i += 1
        
        print("Total antrian:", self.hitung())

    def panggil_berikutnya(self): # panggil (hapus depan)
        if not self.head:
            print("Antrian kosong!")
            return
        
        print("\nMemanggil pasien berikutnya...")
        d = self.head.data
        print(f"Silakan masuk: {d['nama']} ({d['id']}) - {d['penyakit']}")
        
        self.head = self.head.next  # hapus node pertama

    def cari(self, nama): # cari berdasarkan nama
        print(f"\nMencari '{nama}'...")
        current = self.head
        posisi = 1
        
        while current:
            if current.data["nama"] == nama:
                d = current.data
                print(f"Ditemukan: {d['id']} - {d['nama']} | {d['penyakit']} (posisi ke-{posisi})")
                return
            current = current.next
            posisi += 1
        
        print("Tidak ditemukan.")

    def hapus_berdasarkan_id(self, id):    # hapus berdasarkan ID
        print(f"\nMenghapus pasien dengan ID {id}...")
        
        # kasus 1: head
        if self.head and self.head.data["id"] == id:
            d = self.head.data
            self.head = self.head.next
            print(f"{d['nama']} ({d['id']}) berhasil dihapus dari antrian.")
            return
        
        # kasus 2: tengah/akhir
        current = self.head
        while current and current.next:
            if current.next.data["id"] == id:
                d = current.next.data
                current.next = current.next.next
                print(f"{d['nama']} ({d['id']}) berhasil dihapus dari antrian.")
                return
            current = current.next
        
        # kasus 3: tidak ditemukan
        print("ID tidak ditemukan dalam antrian.")

    def hitung(self):  # hitung jumlah node
        count = 0
        current = self.head
        
        while current:
            count += 1
            current = current.next
        
        return count

antrian = AntrianPasien()

# tambah data
antrian.tambah({"id": "P001", "nama": "Andi", "penyakit": "Flu"})
antrian.tambah({"id": "P002", "nama": "Budi", "penyakit": "Tifus"})
antrian.tambah({"id": "P003", "nama": "Cici", "penyakit": "Flu"})
antrian.tambah({"id": "P004", "nama": "Dani", "penyakit": "Maag"})

antrian.tampilkan()

antrian.panggil_berikutnya() # panggil pasien pertama

antrian.tampilkan() # tampilkan lagi

antrian.hapus_berdasarkan_id("P003") # hapus pasien

antrian.tampilkan() # tampilkan lagi

antrian.cari("Dani") # cari pasien

print("Total antrian:", antrian.hitung()) # total akhir