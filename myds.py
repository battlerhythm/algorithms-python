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

class Queue():
    def __init__(self):
        self.alist = []

    def isEmpty(self):
        return self.alist == []

    def size(self):
        return len(self.alist)

    def enqueue(self, e):
        self.alist.insert(0, e)

    def dequeue(self):
        return self.alist.pop()

