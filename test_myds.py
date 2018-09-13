import unittest
from myds import Stack, Queue, Deque, LinkedList, BinaryHeap

class TestDsMethods(unittest.TestCase):
    stk = Stack()
    q = Queue()
    dq = Deque()
    ll = LinkedList()
    bh = BinaryHeap()

    def test_Stack(self):
        self.stk.push(1)
        self.stk.push('a')
        self.assertEqual('[1, \'a\']', str(self.stk))
        self.assertEqual('a', self.stk.peek())
        self.assertEqual(2, len(self.stk))
        self.assertEqual('a', self.stk.pop())
        self.assertEqual(1, len(self.stk))
        self.assertEqual(False, self.stk.isEmpty())
        self.stk.pop()
        self.assertEqual(True, self.stk.isEmpty())
        self.assertEqual(0, len(self.stk))

    def test_Queue(self):
        self.q.enqueue(1)
        self.q.enqueue('a')
        self.assertEqual(2, len(self.q))
        self.assertEqual(1, self.q.dequeue())
        self.assertEqual(1, len(self.q))
        self.q.dequeue()
        self.assertEqual(True, self.q.isEmpty())

    def test_Deque(self):
        self.dq.addFront(1)
        self.dq.addRear('a')
        self.dq.addFront(2)
        self.dq.addRear('b')
        self.assertEqual('[2, 1, \'a\', \'b\']', str(self.dq))
        self.assertEqual(4, len(self.dq)) # [2, 1, 'a', 'b']
        self.assertEqual('b', self.dq.removeRear())
        self.assertEqual('a', self.dq.removeRear())
        self.assertEqual(1, self.dq.removeRear())
        self.assertEqual(2, self.dq.removeFront())
        self.assertEqual(True, self.dq.isEmpty())

    def test_LinkedList(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.append(4)
        self.assertEqual('[1, 2, 3, 4]', str(self.ll))
        self.assertEqual(2, self.ll.pop(1))
        self.assertEqual(4, self.ll.pop(2))
        self.assertEqual(2, len(self.ll))
        self.assertEqual(3, self.ll.pop())
        self.assertEqual(1, self.ll.pop())
        self.assertEqual(True, self.ll.isEmpty())

    def test_BinaryHeap(self):
        self.bh.buildHeap([9, 5, 6, 2, 3])
        self.assertEqual(5, self.bh.size)
        self.assertEqual(2, self.bh.delMin())
        self.assertEqual(3, self.bh.delMin())
        self.assertEqual(3, self.bh.size)
        self.assertEqual(5, self.bh.delMin())
        self.assertEqual(6, self.bh.delMin())
        self.assertEqual(9, self.bh.delMin())


if __name__ == '__main__':
    unittest.main()