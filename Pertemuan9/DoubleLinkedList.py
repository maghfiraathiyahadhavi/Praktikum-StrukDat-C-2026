class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def tampil_maju(self):
        temp = self.head
        print("[Maju]")
        while temp:
            print(temp.data)
            temp = temp.next

    def tampil_mundur(self):
        temp = self.head
        if not temp:
            return

        while temp.next:
            temp = temp.next

        print("[Mundur]")
        while temp:
            print(temp.data)
            temp = temp.prev

    def hapus(self, data):
        temp = self.head

        while temp:
            if temp.data == data:
                if temp.prev is None:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
                return
            temp = temp.next

        print("Data tidak ditemukan")

dll = DoubleLinkedList()

dll.tambah("B 1111 AA")
dll.tambah("D 2222 BB")
dll.tambah("A 3333 CC")
dll.tambah("B 4444 DD")

print("Sebelum:")
dll.tampil_maju()

dll.hapus("A 3333 CC")

print("Sesudah:")
dll.tampil_maju()