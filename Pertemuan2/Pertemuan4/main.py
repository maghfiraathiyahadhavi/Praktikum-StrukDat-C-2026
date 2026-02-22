from kurs import kurs
from konverter import konversi
from tabulate import tabulate

print("=== KONVERTER MATA UANG ===")

# menampilkan tabel kurs
data = []
for kode, nilai in kurs.items():
    data.append([kode, f"{nilai:,}" .replace(".", ".")])

print(tabulate(data, headers=["kode", "kurs"], tablefmt="grid"))

mata_uang_dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
mata_uang_ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input("Jumlah: "))

hasil = konversi(mata_uang_dari, mata_uang_ke, jumlah)

if mata_uang_ke == "IDR":
    print(f"Hasil: Rp {hasil:,.0f}".replace(",", "."))
else:
    print(f"Hasil: {hasil:.2f} {mata_uang_ke}") 