class Stack():
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

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

    def __str__(self):
        return str(self.items)

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

    def __str__(self):
        return str(self.items)

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
            prevNode=self.prevNode.getData() if self.prevNode is not None else "None",
            nextNode=self.nextNode.getData() if self.nextNode is not None else "None"
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

    def __str__(self):
        alist = []
        if self.size is 0:
            return alist
        node = self.head
        alist.append(node.getData())
        for _ in range(self.size-1): # O(n)
            node = node.getNext()
            alist.append(node.getData())
        return str(alist)

    def isEmpty(self):
        return self.head == None and self.tail == None

    def getSize(self):
        return self.size

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

    def pop(self, index=-1):
        theNode = None
        if index >= 0 and index < self.size:
            theNode = self.head
            for _ in range(index):
                theNode = theNode.getNext()
        elif index < 0 and abs(index)-1 < self.size:
            theNode = self.tail
            for _ in range(abs(index)-1):
                theNode = theNode.getPrev()
        else:
            raise IndexError
        if theNode.getNext() and theNode.getPrev():         # for itmes in middle
            theNode.getNext().setPrev(theNode.getPrev())
            theNode.getPrev().setNext(theNode.getNext())
        elif theNode.getNext():                             # for index 0
            theNode.getNext().setPrev(None)
            self.head = theNode.getNext
        elif theNode.getPrev():                             # for index -1
            theNode.getPrev().setNext(None)
            self.tail = theNode.getPrev()
        else:                                               # for single item
            self.head = None
            self.tail = None
        
        self.size -= 1
        return theNode.getData()
        
if __name__ == '__main__':
    stk = Stack()
    stk.push(1)
    stk.push(2)
    print(stk)

        