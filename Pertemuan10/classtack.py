#implementasi menggunakan class

class StackList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, url):
        self.items.append(url)
        
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.items[-1]

    def size(self):
        return len(self.items)
    
myStack = StackList()

myStack.push('https:fira.id')
myStack.push('https:serin.id')
myStack.push('https:zcc.id')

print("Stack: ", myStack.items)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.items)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.is_empty())
print("Size: ", myStack.size())

