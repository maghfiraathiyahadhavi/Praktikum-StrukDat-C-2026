def hitung_komisi(total_penjualan, skema, index=0):
    if (total_penjualan >= skema[index][0]
            or index >= len(skema) - 1):
        return skema[index][1]
    else:
        return hitung_komisi(total_penjualan, skema, index + 1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class AntrianPasien:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    def tampilkan(self):
        cur = self.head
        i = 1
        print("=== ANTRIAN ===")
        while cur:
            d = cur.data
            print(f"[{i}] {d['id']} - {d['nama']}")
            cur = cur.next
            i += 1

    def panggil(self):
        if self.head:
            print("Panggil:", self.head.data["nama"])
            self.head = self.head.next

    def cari(self, nama):
        cur = self.head
        i = 1
        while cur:
            if cur.data["nama"] == nama:
                print("Ditemukan di posisi", i)
                return
            cur = cur.next
            i += 1
        print("Tidak ditemukan")

    def hapus_berdasarkan_id(self, id):
        cur = self.head
        prev = None

        if cur and cur.data["id"] == id:
            self.head = cur.next
            return

        while cur and cur.data["id"] != id:
            prev = cur
            cur = cur.next

        if not cur:
            print("ID tidak ada")
            return

        prev.next = cur.next

    def hitung(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count


