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
        
class Node():
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

class LinkedList():
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

class BinaryHeap():
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

class TreeNode():
    def __init__(self, key, value, leftChild=None, rightChild=None, parent=None):
        self._key = key
        self._value = value
        self._leftChild = leftChild
        self._rightChild = rightChild
        self._parent = parent

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, newTreeNode):
        self._parent = newTreeNode

    @property
    def leftChild(self):
        return self._leftChild

    @leftChild.setter
    def leftChild(self, newTreeNode):
        self._leftChild = newTreeNode

    @property
    def rightChild(self):
        return self._rightChild

    @rightChild.setter
    def rightChild(self, newTreeNode):
        self._rightChild = newTreeNode

    def isLeftChild(self):
        return self._parent and self._parent.leftChild == self

    def isRightChild(self):
        return self._parent and self._parent.rightChild == self

    def isRoot(self):
        return not self._parent

    def isLeaf(self):
        return not (self._leftChild or self._rightChild)

    def hasAnyChildren(self):
        return self._leftChild or self._rightChild

    def hasBothChildren(self):
        return self._leftChild and self._rightChild

    def replaceNodeData(self, newKey, newValue, newLeftChild, newRightChild):
        self._key = newKey
        self._value = newValue
        self._leftChild = newLeftChild
        self._rightChild = newRightChild
        if self._leftChild:
            self._leftChild.parent = self
        if self._rightChild:
            self._rightChild.parent = self
    
class BinarySearchTree():
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __setitem__(self, k, v):
        self.put(k, v)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self._root):
            return True
        else:
            return False

    def __delitem__(self, key):
        self.delete(key)

    def put(self, key, value):
        if self._root:
            self._put(key, value, self._root)
        else:
            self._root = TreeNode(key, value)
        self._size += 1

    def _put(self, key, value, theNode):
        if key < theNode.key:
            if theNode.leftChild:
                self._put(key, value, theNode.leftChild)
            else:
                theNode.leftChild = TreeNode(key, value, parent=theNode)
        else:
            if theNode.rightChild:
                self._put(key, value, theNode.rightChild)
            else:
                theNode.rightChild = TreeNode(key, value, parent=theNode)

    def get(self, key):
        if self._root:
            node = self._get(key, self._root)
            if node:
                return node.value
            else:
                raise KeyError
        else:
            raise KeyError

    def _get(self, key, theNode):
        if not theNode:
            return None
        elif theNode.key == key:
            return theNode
        elif key < theNode.key:
            return self._get(key, theNode.leftChild)
        else:
            return self._get(key, theNode.rightChild)

    def delete(self, key):
        if self._size > 1:
            nodeToRemove = self._get(key, self._root)
            if nodeToRemove:
                self._remove(nodeToRemove)
                self._size -= 1
            else:
                raise KeyError
        elif self._size == 1 and self._root.key == key:
            self._root = None
            self._size -= 1
        else:
            raise KeyError
        
    def _remove(self, theNode):
        if theNode.isLeaf(): # Leaf
            if theNode == theNode.parent.leftChild:
                theNode.parent.leftChild = None
            else:
                theNode.parent.rightChild = None
        elif theNode.hasBothChildren(): # Interior Node that has two child
            successor = self._findSuccessor(theNode)
            self._spliceOut(successor)
            theNode.key, theNode.value = successor.key, successor.value
        else: # Node, which has one child
            if theNode.leftChild:
                if theNode.isLeftChild():
                    theNode.leftChild.parent = theNode.parent
                    theNode.parent.leftChild = theNode.leftChild
                elif theNode.isRightChild():
                    theNode.leftChild.parent = theNode.parent
                    theNode.parent.rightChild = theNode.leftChild
                else:
                    theNode.replaceNodeData(
                        theNode.leftChild.key,
                        theNode.leftChild.value,
                        theNode.leftChild.leftChild,
                        theNode.leftChild.rightChild
                    )
            else:
                if theNode.isLeftChild():
                    theNode.rightChild.parent = theNode.parent
                    theNode.parent.leftChild = theNode.rightChild
                elif theNode.isRightChild():
                    theNode.rightChild.parent = theNode.parent
                    theNode.parent.rightChild = theNode.rightChild
                else:
                    theNode.replaceNodeData(
                        theNode.rightChild.key,
                        theNode.rightChild.value,
                        theNode.rightChild.leftChild,
                        theNode.rightChild.rightChild
                    )

    def _spliceOut(self, theNode):
        if theNode.isLeaf():
            if theNode.isLeftChild():
                theNode.parent.leftChild = None
            else:
                theNode.parent.rightChild = None
        else: # if theNode has any children
            if theNode.leftChild:
                if theNode.isLeftChild():
                    theNode.parent.leftChild = theNode.leftChild
                else:
                    theNode.parent.rightChild = theNode.leftChild
                theNode.leftChild.parent = theNode.parent
            else:
                if theNode.isLeftChild():
                    theNode.parent.leftChild = theNode.rightChild
                else:
                    theNode.parent.rightChild = theNode.rightChild
                theNode.rightChild.parent = theNode.parent

    def _findSuccessor(self, theNode):
        successor = None
        if theNode.rightChild:
            successor = self._findMinChild(theNode.rightChild)
        else:
            if theNode.parent:
                if theNode.isLeftChild():
                    successor = theNode.parent
                else:
                    theNode.parent.rightChild = None
                    successor = self._findSuccessor(theNode.parent)
                    theNode.parent.rightChild = theNode
        return successor              
    
    def _findMinChild(self, theNode):
        minChild = theNode
        while theNode.leftChild:
            minChild = minChild.leftChild
        return minChild

        