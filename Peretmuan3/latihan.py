class MyJussBuah:
    def __init__(self, buah, color, weight):
        self.buah = buah
        self.color = color
        self.weight = weight

def introduce_self(self, buah, color):
    print(f"Haloo buah saya {buah} dengan color {color}")

def update_color (self, buah, new_color):
    self.color = new_color

buah1 = MyJussBuah("Jeruk", "kuning", "80")
buah2 = MyJussBuah("Anggur", "Unggu", "78")
buah3 = MyJussBuah("Melon", "Hijau", "67")
        


buah3.update_color("Pink")