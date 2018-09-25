class Stack(object):
    def __init__(self):
        self._items = []

    def __str__(self):
        return str(self._items)  

    def __len__(self):
        return len(self._items)

    def isEmpty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def peek(self):
        return self._items[-1]

    def pop(self):
        return self._items.pop()

class Queue(object):
    def __init__(self):
        self._items = []

    def __str__(self):
        return str(self._items)

    def __len__(self):
        return len(self._items)

    def isEmpty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

class Deque(Queue):
    def __init__(self):
        super().__init__()

    def enqueueLeft(self, item):
        return self._items.insert(0, item)

    def dequeueRight(self):
        return self._items.pop(-1)
        
class Node(object):
    def __init__(self, data):
        self._data = data
        self._nextNode = None
        self._prevNode = None

    @property
    def data(self):
        """Return the data in the node"""
        return self._data

    @property
    def nextNode(self):
        """Return the next node of the Node"""
        return self._nextNode

    @property
    def prevNode(self):
        """Return the previous node of the Node"""
        return self._prevNode
  
    @nextNode.setter
    def nextNode(self, newNextNode):
        self._nextNode = newNextNode
  
    @prevNode.setter
    def prevNode(self, newPrevNode):
        self._prevNode = newPrevNode

class LinkedList(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __str__(self):
        alist = []
        if self._size is 0:
            return str(alist)
        node = self._head
        alist.append(node.data)
        for _ in range(self._size-1): # O(n)
            node = node.nextNode
            alist.append(node.data)
        return str(alist)

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._head == None and self._tail == None

    def append(self, item):
        newNode = Node(item)
        if self._head and self._tail:
            temp = self._tail
            newNode.prevNode = temp
            temp.nextNode = newNode
            self._tail = newNode
        else:
            self._head = self._tail = newNode
        self._size += 1

    def pop(self, index=-1):
        theNode = self._getNodeAt(index)
        self._remove(theNode)
        self._size -= 1
        return theNode.data

    def _getNodeAt(self, index):
        theNode = None
        if index >= 0 and index < self._size:
            theNode = self._head
            for _ in range(index):
                theNode = theNode.nextNode
        elif index < 0 and abs(index)-1 < self._size:
            theNode = self._tail
            for _ in range(abs(index)-1):
                theNode = theNode.prevNode
        else:
            raise IndexError
        return theNode
    
    def _remove(self, item):
        if item.nextNode and item.prevNode:             # for items in middle
            item.nextNode.prevNode = item.prevNode
            item.prevNode.nextNode = item.nextNode
        elif item.nextNode:                             # for index 0
            item.nextNode.prevNode = None
            self._head = item.nextNode
        elif item.prevNode:                             # for index -1
            item.prevNode.nextNode = None
            self._tail = item.prevNode
        else:                                           # for single item
            self._head = None
            self._tail = None

class BinaryHeap(object):
    def __init__(self):
        self._items = [0]
        self._size = 0

    def __len__(self):
        return self._size

    @property
    def items(self):
        return self._items[1:]

    def _percUp(self, idx):
        while idx//2 > 0:
            if self._items[idx] < self._items[idx//2]:
                self._items[idx], self._items[idx//2] = self._items[idx//2], self._items[idx]
            idx //= 2

    def insert(self, item):
        self._items.append(item)
        self._size += 1
        self._percUp(self._size)

    def _percDown(self, idx):
        while idx*2 <= self._size:
            minIdx = self._minChild(idx)
            if self._items[idx] > self._items[minIdx]:
                self._items[idx], self._items[minIdx] = self._items[minIdx], self._items[idx]
            idx = minIdx

    def _minChild(self, idx):
        if idx*2+1 > self._size:
            return idx*2
        else:
            if self._items[idx*2] < self._items[idx*2+1]:
                return idx*2
            else:
                return idx*2+1

    def delMin(self):
        item = self._items[1]
        self._items[1] = self._items[self._size]
        self._size -= 1
        self._items.pop()
        self._percDown(1)
        return item
    
    def buildHeap(self, alist):
        idx = len(alist)//2
        self._size = len(alist)
        self._items = [0] + alist
        while idx > 0:
            self._percDown(idx)
            idx -= 1