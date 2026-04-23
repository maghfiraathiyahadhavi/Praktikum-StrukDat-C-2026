class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def giliran(self, n):
        if not self.head:
            return

        temp = self.head
        for i in range(1, n + 1):
            print(f"Giliran {i}: {temp.data}")
            temp = temp.next

cll = CircularLinkedList()

cll.tambah("Andi")
cll.tambah("Budi")
cll.tambah("Citra")
cll.tambah("Dewi")

cll.giliran(6)