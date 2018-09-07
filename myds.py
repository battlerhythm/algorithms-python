class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

class Deque():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFront(self, item):
        self.items.insert(0, item)
    
    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

class Node():
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None

    def __str__(self):
        string = "currentNode: {data}\t prevNode: {prevNode}\t nextNode: {nextNode}\n".format(
            data=self.data,
            prevNode=self.prevNode,
            nextNode=self.nextNode
        )
        return string

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def getPrev(self):
        return self.prevNode

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNextNode):
        self.nextNode = newNextNode
    
    def setPrev(self, newPrevNode):
        self.prevNode = newPrevNode

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.head == None and self.tail == None

    def getSize(self):
        return self.size

    def show(self):
        alist = []
        if self.size is 0:
            return alist
        node = self.head
        alist.append(node.getData())
        for _ in range(self.size-1):
            node = node.getNext()
            alist.append(node.getData())
        return alist

    def append(self, item):
        newNode = Node(item)
        if self.head and self.tail:
            temp = self.tail
            newNode.setPrev(temp)
            temp.setNext(newNode)
            self.tail = newNode
        else:
            self.head = self.tail = newNode
        self.size += 1

    def pop(self):
        data = self.tail.getData()
        if self.size is 1:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.getPrev()
            self.tail.setNext = None
        self.size -= 1
        return data
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.pop()
    ll.pop()
    ll.pop()
    print(ll.show())

        