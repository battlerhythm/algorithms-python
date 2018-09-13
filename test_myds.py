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
        self.dq.enqueue(1)
        self.dq.enqueueLeft('a')
        self.dq.enqueue(2)
        self.dq.enqueueLeft('b')
        self.assertEqual('[\'b\', \'a\', 1, 2]', str(self.dq))
        self.assertEqual(4, len(self.dq)) # ['b', 'a', 1, 2]
        self.assertEqual('b', self.dq.dequeue())
        self.assertEqual('a', self.dq.dequeue())
        self.assertEqual(2, self.dq.dequeueRight())
        self.assertEqual(1, self.dq.dequeueRight())
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
        self.assertEqual([2, 3, 6, 5, 9], self.bh.items)
        self.assertEqual(5, len(self.bh))
        self.assertEqual(2, self.bh.delMin())
        self.assertEqual(3, self.bh.delMin())
        self.assertEqual(3, len(self.bh))
        self.assertEqual(5, self.bh.delMin())
        self.assertEqual(6, self.bh.delMin())
        self.assertEqual(9, self.bh.delMin())


if __name__ == '__main__':
    unittest.main()