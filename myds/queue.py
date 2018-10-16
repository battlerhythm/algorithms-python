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