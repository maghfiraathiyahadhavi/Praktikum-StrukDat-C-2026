def filter_harga(data, min_harga, max_harga):
    result = []
    for x in data:
        if (x["harga"] >= min_harga
                and x["harga"] <= max_harga):
            result.append(x)
    return result

