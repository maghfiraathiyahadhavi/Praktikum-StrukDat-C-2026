from kurs import kurs

def konversi(mata_uang_dari, mata_uang_ke, jumlah):
    if mata_uang_dari == "IDR":
        return jumlah / kurs[mata_uang_ke]
    elif mata_uang_ke == "IDR":
        return jumlah * kurs[mata_uang_dari]
    else:
        # konversi ke IDR dulu lalu ke mata uang tujuan 
        dalam_idr = jumlah * [mata_uang_dari]
        return dalam_idr / kurs[mata_uang_ke]