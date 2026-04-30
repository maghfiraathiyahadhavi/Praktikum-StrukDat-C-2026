def filter_harga(data, min_harga, max_harga):
    result = []
    for x in data:
        if (x["harga"] >= min_harga
                and x["harga"] <= max_harga):
            result.append(x)
    return result

def main():
    stok_gadget = [
        {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000},
        {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000},
        {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000},
        {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000},
    ]
    
    min_harga = int(input("Masukkkan harga minimal: "))
    max_harga = int(input("Masukkan harga maksimal: "))
    result = filter_harga(stok_gadget, min_harga, max_harga)
    if len(result) > 0:
        print(result)
    else:
        print("Tidak ada gadget dalam rentang harga tersebut.")


if __name__ == "__main__":
    main()