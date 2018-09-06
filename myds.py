class Stack():
    def __init__(self):
        self.alist = []

    def isEmpty(self):
        return self.alist == []

    def size(self):
        return len(self.alist)

    def push(self, e):
        self.alist.append(e)

    def peek(self):
        return self.alist[-1]

    def pop(self):
        return self.alist.pop()

if __name__ == '__main__':
    myStack = Stack()
    print(myStack.isEmpty())
    myStack.push('a')
    print(myStack.size())
    print(myStack.peek())
    print(myStack.size())
    print(myStack.isEmpty())
    print(myStack.pop())
    print(myStack.isEmpty())