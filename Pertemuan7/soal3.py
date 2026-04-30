class  Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def tampilkan_antrian(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")


def sisipkan_vip(head, plat_baru, plat_target):
  currentNode = head

  while currentNode:
    if currentNode.data == plat_target:
      newNode = Node(plat_baru)
      newNode.next = currentNode.next
      currentNode.next = newNode
      break
    currentNode = currentNode.next

  return head


node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("A 111 TUV")
node4 = Node("B 2022 EFG")

node1.next = node2
node2.next = node3
node3.next = node4

head = node1


print("Antrian awal:")
tampilkan_antrian(head)

head = sisipkan_vip(head, "B 0384 CUY", "D 7689 BRO")

print("Setelah VIP disisipkan:")
tampilkan_antrian(head)