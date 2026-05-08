class HashTableBuku:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # list di dalam list

    # fungsi hash
    def hash_function(self, kode):
        total = 0
        for char in kode:
            total += ord(char)  # Unicode karakter
        return total % self.size

    # insert / update
    def insert(self, kode, judul):
        index = self.hash_function(kode)
        bucket = self.table[index]

        # cek apakah kode sudah ada
        for data in bucket:
            if data[0] == kode:
                data[1] = judul
                print(f"Data buku dengan kode {kode} berhasil diupdate")
                return

        # jika belum ada
        bucket.append([kode, judul])
        print(f"Data buku {kode} berhasil ditambahkan")

    # search
    def search(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]

        for data in bucket:
            if data[0] == kode:
                print(f"{kode} : {data[1]}")
                return

        print("Buku tidak ditemukan")

    # delete
    def delete(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]

        for data in bucket:
            if data[0] == kode:
                bucket.remove(data)
                print(f"Buku dengan kode {kode} berhasil dihapus")
                return

        print("Buku tidak ditemukan")

    # display
    def display(self):
        print("\nIsi Hash Table:")
        for i in range(self.size):
            print(f"Bucket {i} :", end=" ")

            if len(self.table[i]) == 0:
                print("Kosong")
            else:
                for data in self.table[i]:
                    print(f"[{data[0]} : {data[1]}]", end=" ")
                print()


# =========================
# PROGRAM UTAMA
# =========================

buku = HashTableBuku()

# insert data awal
buku.insert("BK111", "Mahir C++ Dalam Satu Jam")
buku.insert("BK222", "Python Dasar")
buku.insert("BK333", "Matematika Diskrit")
buku.insert("BK444", "Atomic Habits")
buku.insert("BK555", "Algoritma Pemrograman")

# display pertama
buku.display()

# insert tambahan
buku.insert("BK045", "Mein Kampf")

# update data BK111
buku.insert("BK111", "Bumi Manusia")

# display kedua
buku.display()

# search data
print("\nPencarian Buku:")
buku.search("BK222")
buku.search("BK999")  # tidak ada

# delete data
print("\nHapus Buku:")
buku.delete("BK333")

# display akhir
buku.display()