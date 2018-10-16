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