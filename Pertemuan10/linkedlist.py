#implementasi menggunakan linkedlist
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 

    def is_empty(self):
        return self.size == 0
    
    def push(self, url):
        new_node = Node(url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count += 1
        
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_node = self.top
        self.top = self.top.next
        self.count -= 1
        return popped_node.url
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.url
    
    def size(self):
         return self.count
    
    
    def traverseAndPrint(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.url, end=" -> ")
            currentNode = currentNode.next
        print()

myStack = StackLinkedList()

myStack.push('https:fira//.id')
myStack.push('https:serin//.id')
myStack.push('https:zcc//.id')

print("LinkedList: ", end="")
myStack.traverseAndPrint()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
myStack.traverseAndPrint()
print("isEmpty: ", myStack.is_empty())
print("Size: ", myStack.size())

