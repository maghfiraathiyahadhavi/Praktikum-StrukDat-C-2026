def hitung_komisi(total_penjualan, skema, index=0):
    if (total_penjualan >= skema[index][0]
            or index >= len(skema) - 1):
        return skema[index][1]
    else:
        return hitung_komisi(total_penjualan, skema, index + 1)

