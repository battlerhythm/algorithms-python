class Stack():
    def __init__(self):
        self.__items = []

    def __str__(self):
        return str(self.__items)   

    def isEmpty(self):
        return self.__items == []

    def size(self):
        return len(self.__items)

    def push(self, item):
        self.__items.append(item)

    def peek(self):
        return self.__items[-1]

    def pop(self):
        return self.__items.pop()

class Queue():
    def __init__(self):
        self.__items = []

    def __str__(self):
        return str(self.__items)

    def isEmpty(self):
        return self.__items == []

    def size(self):
        return len(self.__items)

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0)

class Deque():
    def __init__(self):
        self.__items = []

    def __str__(self):
        return str(self.__items)

    def isEmpty(self):
        return self.__items == []

    def size(self):
        return len(self.__items)

    def addFront(self, item):
        self.__items.insert(0, item)
    
    def addRear(self, item):
        self.__items.append(item)

    def removeFront(self):
        return self.__items.pop(0)

    def removeRear(self):
        return self.__items.pop()

class Node():
    def __init__(self, data):
        self.__data = data
        self.__nextNode = None
        self.__prevNode = None

    def __str__(self):
        string = "currentNode: {data}\t prevNode: {prevNode}\t nextNode: {nextNode}\n".format(
            data=self.__data,
            prevNode=self.prevNode.data if self.prevNode is not None else "None",
            nextNode=self.nextNode.data if self.nextNode is not None else "None"
        )
        return string

    @property
    def data(self):
        """Return the data in the node"""
        return self.__data

    @property
    def nextNode(self):
        """Return the next node of the Node"""
        return self.__nextNode

    @property
    def prevNode(self):
        """Return the previous node of the Node"""
        return self.__prevNode

    @data.setter
    def data(self, newData):
        self.__data = newData
  
    @nextNode.setter
    def nextNode(self, newNextNode):
        self.__nextNode = newNextNode
  
    @prevNode.setter
    def prevNode(self, newPrevNode):
        self.__prevNode = newPrevNode

class LinkedList():
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __str__(self):
        alist = []
        if self.__size is 0:
            return alist
        node = self.__head
        alist.append(node.data)
        for _ in range(self.__size-1): # O(n)
            node = node.nextNode
            alist.append(node.data)
        return str(alist)

    def isEmpty(self):
        return self.__head == None and self.__tail == None

    @property
    def size(self):
        """Return the size of the LikedList"""
        return self.__size

    def append(self, item):
        newNode = Node(item)
        if self.__head and self.__tail:
            temp = self.__tail
            newNode.prevNode = temp
            temp.nextNode = newNode
            self.__tail = newNode
        else:
            self.__head = self.__tail = newNode
        self.__size += 1

    def pop(self, index=-1):
        theNode = self.__getNodeAt(index)
        self.__remove(theNode)
        self.__size -= 1
        return theNode.data

    def __getNodeAt(self, index):
        theNode = None
        if index >= 0 and index < self.__size:
            theNode = self.__head
            for _ in range(index):
                theNode = theNode.nextNode
        elif index < 0 and abs(index)-1 < self.__size:
            theNode = self.__tail
            for _ in range(abs(index)-1):
                theNode = theNode.prevNode
        else:
            raise IndexError
        return theNode
    
    def __remove(self, item):
        if item.nextNode and item.prevNode:             # for itmes in middle
            item.nextNode.prevNode = item.prevNode
            item.prevNode.nextNode = item.nextNode
        elif item.nextNode:                             # for index 0
            item.nextNode.prevNode = None
            self.__head = item.nextNode
        elif item.prevNode:                             # for index -1
            item.prevNode.nextNode = None
            self.__tail = item.prevNode
        else:                                           # for single item
            self.__head = None
            self.__tail = None

class BinaryHeap():
    def __init__(self):
        self.__items = [0]
        self.__size = 0

    @property
    def size(self):
        return self.__size

    @property
    def items(self):
        return self.__items[1:]

    def __percUp(self, idx):
        while idx//2 > 0:
            if self.__items[idx] < self.__items[idx//2]:
                self.__items[idx], self.__items[idx//2] = self.__items[idx//2], self.__items[idx]
            idx //= 2

    def insert(self, item):
        self.__items.append(item)
        self.__size += 1
        self.__percUp(self.__size)

    def __percDown(self, idx):
        while idx*2 <= self.__size:
            minIdx = self.__minChild(idx)
            if self.__items[idx] > self.__items[minIdx]:
                self.__items[idx], self.__items[minIdx] = self.__items[minIdx], self.__items[idx]
            idx = minIdx

    def __minChild(self, idx):
        if idx*2+1 > self.__size:
            return idx*2
        else:
            if self.__items[idx*2] < self.__items[idx*2+1]:
                return idx*2
            else:
                return idx*2+1

    def delMin(self):
        item = self.__items[1]
        self.__items[1] = self.__items[self.size]
        self.__size -= 1
        self.__items.pop()
        self.__percDown(1)
        return item
    
    def buildHeap(self, alist):
        idx = len(alist)//2
        self.__size = len(alist)
        self.__items = [0] + alist
        while idx > 0:
            self.__percDown(idx)
            idx -= 1

if __name__ == '__main__':
    bh = BinaryHeap()
    bh.buildHeap([9, 5, 6, 2, 3])
    print(bh.items)
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())

        