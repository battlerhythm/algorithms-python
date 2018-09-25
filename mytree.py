class TreeNode(object):
    def __init__(self, key, value, leftChild=None, rightChild=None, parent=None):
        self._key = key
        self._value = value
        self._leftChild = leftChild
        self._rightChild = rightChild
        self._parent = parent
        self._balanceFactor = 0

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

    @property
    def balanceFactor(self):
        return self._balanceFactor

    @balanceFactor.setter
    def balanceFactor(self, newBalanceFactor):
        self._balanceFactor = newBalanceFactor

    def isLeftChild(self):
        return self._parent and self._parent.leftChild == self

    def isRightChild(self):
        return self._parent and self._parent.rightChild == self

    def isRoot(self):
        return not self._parent

    def isLeaf(self):
        return not (self._leftChild or self._rightChild)

    # def hasLeftChild(self):
    #     return self._leftChild
    
    # def hasRightChild(self):
    #     return self._rightChild

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
    
class BinarySearchTree(object):
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

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, theNode):
        self._root = theNode

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, newSize):
        self._size = newSize

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
    
class AvlTree(BinarySearchTree):
    def _put(self, key, value, theNode):
        if key < theNode.key:
            if theNode.leftChild:
                self._put(key, value, theNode.leftChild)
            else:
                theNode.leftChild = TreeNode(key, value, parent=theNode)
                self.updateBalance(theNode.leftChild)
        else:
            if theNode.rightChild:
                self._put(key, value, theNode.rightChild)
            else:
                theNode.rightChild = TreeNode(key, value, parent=theNode)
                self.updateBalance(theNode.rightChild)

    def updateBalance(self, theNode):
        if theNode.balanceFactor > 1 or theNode.balanceFactor < -1:
            self.rebalance(theNode)
            return
        if theNode.parent != None:
            if theNode.isLeftChild():
                theNode.parent.balanceFactor += 1
            elif theNode.isRightChild():
                theNode.parent.balanceFactor -= 1
            
            if theNode.parent.balanceFactor != 0:
                self.updateBalance(theNode.parent)

    def rotateLeft(self, root):
        newRoot = root.rightChild
        root.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = root
        newRoot.parent = root.parent
        if root.isRoot():
            self.root = newRoot
        else:
            if root.isLeftChild():
                root.parent.leftChild = newRoot
            else:
                root.parent.rightChild = newRoot
        newRoot.leftChild = root
        root.parent = newRoot
        root.balanceFactor = root.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(root.balanceFactor, 0)

    def rotateRight(self, root):
        newRoot = root.leftChild
        root.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = root
        newRoot.parent = root.parent
        if root.isRoot():
            self.root = newRoot
        else:
            if root.isRightChild():
                root.parent.rightChild = newRoot
            else:
                root.parent.leftChild = newRoot
            newRoot.rightChild = root
            root.parent = newRoot
            root.balanceFactor = root.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
            newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(root.balanceFactor, 0)

    def rebalance(self, theNode):
        if theNode.balanceFactor < 0:
            if theNode.rightChild.balanceFactor > 0:
                self.rotateRight(theNode.rightChild)
                self.rotateLeft(theNode)
            else:
                self.rotateLeft(theNode)
        elif theNode.balanceFactor > 0:
            if theNode.leftChild.balanceFactor < 0:
                self.rotateLeft(theNode.leftChild)
                self.rotateRight(theNode)
            else:
                self.rotateRight(theNode)