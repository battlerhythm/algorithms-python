from myds.node import Node

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