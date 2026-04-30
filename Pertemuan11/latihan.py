# ===
# Node (Pasien)
class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

# ===
# Queue Linked List
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # 1. Enqueue
    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._size})")

    # 2. Dequeue
    def dequeue(self):
        if self.is_empty():
            print("[ERROR] Antrian kosong!")
            return None

        removed = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._size -= 1
        print(f"[PANGGIL] Dokter memanggil: {removed.nama} (keluhan: {removed.keluhan})")
        return removed

    # 3. Peek / Front
    def peek(self):
        if self.is_empty():
            print("[PEEK] Antrian kosong!")
        else:
            print(f"[PEEK] Pasien berikutnya: {self.head.nama.upper()} — {self.head.keluhan}")

    # 4. Is Empty
    def is_empty(self):
        return self._size == 0

    # 5. Size
    def size(self):
        return self._size

    # 6. Clear
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    # Tambahan: tampilkan semua antrian
    def display(self):
        if self.is_empty():
            print("[ANTRIAN] Kosong")
            return

        print("\n[ANTRIAN SAAT INI]")
        current = self.head
        i = 1
        while current:
            print(f"{i}. {current.nama.upper()} → {current.keluhan}")
            current = current.next
            i += 1


# ===
# SIMULASI SESUAI SOAL
print("====================================")
print(" SISTEM ANTRIAN POLI UMUM")
print(" RS Sehat Bersama")
print("====================================\n")

antrian = Queue()

print("[CEK] Apakah antrian kosong?", "→ YA, antrian masih kosong." if antrian.is_empty() else "→ TIDAK")
antrian.enqueue("ZCC", "demam tinggi")
antrian.enqueue("JII", "batuk pilek")
antrian.enqueue("HCC", "sakit kepala")
print(f"\n[INFO] Jumlah pasien menunggu: {antrian.size()} orang")
antrian.peek()
antrian.dequeue()
antrian.enqueue("WWE", "nyeri perut")
antrian.display()
antrian.dequeue()
print(f"\n[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang")
antrian.clear()
print("[CEK] Apakah antrian kosong?", "→ YA, antrian sudah kosong." if antrian.is_empty() else "→ TIDAK")

print("\n====================================")
print(" Simulasi Selesai!")
print("====================================")