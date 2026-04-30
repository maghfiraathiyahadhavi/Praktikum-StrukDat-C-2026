class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")



def tambah(head, newNode, position):
  if position == 1:
    newNode.next = head
    return newNode

  currentNode = head
  for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  newNode.next = currentNode.next
  currentNode.next = newNode
  return head

def minus(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next

  return head



plat1 = Node("B 1234 ABC")
plat2 = Node("D 8888 XYZ")
plat3 = Node("A 111 TUV")
plat4 = Node("B 2022 EFG")


plat1.next = plat2
plat2.next = plat3
plat3.next = plat4

print("Original")
traverseAndPrint(plat1)

newPlat = Node("D 1212 KKK")
plat1 = tambah(plat1, newPlat, 5)
print("\n Setelah ditambah")
traverseAndPrint(plat1)

plat1 = minus(plat1,plat3)
print("\n Setelah di Kurang")
traverseAndPrint(plat1)