class Graph:
    def __init__(self):
        # adjacency list
        self.graph = {}

    # 1. tambah kota
    def tambah_kota(self, nama):
        if nama not in self.graph:
            self.graph[nama] = []

    # 2. tambah jalan (undirected)
    def tambah_jalan(self, u, v, jarak):
        self.tambah_kota(u)
        self.tambah_kota(v)

        self.graph[u].append((v, jarak))
        self.graph[v].append((u, jarak))

        print(f'[INPUT] Menambahkan jalan: {u} - {v} ({jarak} km)')

    # 3. tampilkan graph
    def tampilkan_graph(self):
        print("\n[INFO] Struktur Jaringan Distribusi:")

        for kota in self.graph:
            print(f"- {kota} terhubung ke: ", end="")

            tetangga = []
            for tujuan, jarak in self.graph[kota]:
                tetangga.append(f"{tujuan} ({jarak})")

            print(", ".join(tetangga))

    # 4. algoritma dijkstra
    def dijkstra(self, kota_asal):

        # inisialisasi jarak
        jarak = {}
        for kota in self.graph:
            jarak[kota] = float('inf')

        jarak[kota_asal] = 0

        visited = []

        while len(visited) < len(self.graph):

            # cari kota dengan jarak terkecil
            min_kota = None
            min_jarak = float('inf')

            for kota in self.graph:
                if kota not in visited and jarak[kota] < min_jarak:
                    min_jarak = jarak[kota]
                    min_kota = kota

            # jika tidak ada kota ditemukan
            if min_kota is None:
                break

            visited.append(min_kota)

            # update jarak tetangga
            for tetangga, bobot in self.graph[min_kota]:

                if tetangga not in visited:
                    jarak_baru = jarak[min_kota] + bobot

                    if jarak_baru < jarak[tetangga]:
                        jarak[tetangga] = jarak_baru

        # tampil hasil
        print(f"\n[PROSES] Menghitung rute terpendek dari: {kota_asal}...")

        print(f"\n[HASIL] Jarak Terpendek dari {kota_asal}:")

        nomor = 1
        for kota, nilai in jarak.items():
            if kota != kota_asal:
                print(f"{nomor}. Ke {kota}: {nilai} km")
                nomor += 1


# =====================================
# PROGRAM UTAMA
# =====================================

print("SISTEM NAVIGASI LOGISTIK 'KILAT MAJU'")
print("=========================================")

g = Graph()

# input jalan
g.tambah_jalan("Jakarta", "Bandung", 150)
g.tambah_jalan("Jakarta", "Cirebon", 200)
g.tambah_jalan("Bandung", "Tasikmalaya", 100)
g.tambah_jalan("Bandung", "Cirebon", 130)
g.tambah_jalan("Cirebon", "Semarang", 250)
g.tambah_jalan("Tasikmalaya", "Semarang", 200)

# tampil graph
g.tampilkan_graph()

# jalankan dijkstra
g.dijkstra("Jakarta")

print("\n=========================================")
print("Simulasi Navigasi Selesai!")