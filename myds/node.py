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