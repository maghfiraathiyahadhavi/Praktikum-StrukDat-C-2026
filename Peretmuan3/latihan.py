class MyJussBuah:
    def __init__(self, buah, color, weight):
        self.buah = buah
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f"Haloo buah saya {self.buah} dengan color {self.color}")

    def update_color(self, new_color):
        self.color = new_color


buah1 = MyJussBuah("Jeruk", "Kuning", "80")
buah2 = MyJussBuah("Anggur", "Ungu", "78")
buah3 = MyJussBuah("Melon", "Hijau", "67")

# update warna
buah3.update_color("Pink")

# cek hasil
buah3.introduce_self()