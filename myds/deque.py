from myds.queue import Queue

class Deque(Queue):
    def __init__(self):
        super().__init__()

    def enqueueLeft(self, item):
        return self._items.insert(0, item)

    def dequeueRight(self):
        return self._items.pop(-1)

