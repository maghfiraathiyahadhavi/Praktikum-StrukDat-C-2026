class Node:
    def __init__(self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    # INSERT
    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)

        if self.root is None:
            self.root = new_node
            print(f"[INSERT] Berhasil memasukan: ID {id_buku} - {judul}]")
            return
        
        cur = self.root
        while True:
            if id_buku < cur.id:
                if cur.left is None:
                    cur.left = new_node
                    print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = new_node
                    print(f"[INSERT]ehasil memasukkan: ID {id_buku} - {judul}")
                    return
                cur = cur.right

    def search(self, id_buku):
        cur = self.root
        while cur:
            if id_buku == cur.id:
                return cur
            cur = cur.left if id_buku < cur.id else cur.right
        return None

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"{node.id} - {node.judul}")
            self.inorder(node.right)

    def traversal_inorder(self):
        self.inorder(self.root)
    
    def get_min(self):
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur
    
    def get_max(self):
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur 
    
    def height(self, node):
        if node is None:
            return -1
        return max (self.height(node.left), self.height(node.right)) + 1
    

    # === MAIN ===
print("SISTEM KATALOG PERPUSTAKAAN 'ILMU TERANG' ")
print("==========================================")

bst = BST()

# INSERT DATA
bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Operasi")

# INORDER
print("\n[INFO] Koleksi Buku (In-Order Tranversal):")
bst.traversal_inorder()

# SEARCH 
for i in range(2):
    id_cari = int(input("/nMasukkan Id yang ingin dicari: "))

    print(f"[SEARCE] Mencari ID {id_cari}...", end=" ")
    hasil = bst.search(id_cari)

    if hasil:
        print(f"Ditemukan! Judul: {hasil.judul}")
    else:
        print("Data tidak di temukan")

# STATISTI
min_buku = bst.get_min()
max_buku = bst.get_max()

print(f"\n[STATISTIK] ID Terkecil: {min_buku.id}")
print(f"[STATISTIK] ID Terbesar: {max_buku.id}")

# HEIGHT
print(f"[INFO] Tinggi (height) Tree: {bst.height(bst.root)}")

print("=========================================")
print("Simulasi Selesai!")