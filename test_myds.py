import unittest
from myds import Stack, Queue, Deque, LinkedList, BinaryHeap, BinarySearchTree

class TestDsMethods(unittest.TestCase):
    def test_Stack(self):
        stk = Stack()
        stk.push(1)
        stk.push('a')
        self.assertEqual('[1, \'a\']', str(stk))
        self.assertEqual('a', stk.peek())
        self.assertEqual(2, len(stk))
        self.assertEqual('a', stk.pop())
        self.assertEqual(1, len(stk))
        self.assertEqual(False, stk.isEmpty())
        stk.pop()
        self.assertEqual(True, stk.isEmpty())
        self.assertEqual(0, len(stk))

    def test_Queue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue('a')
        self.assertEqual(2, len(q))
        self.assertEqual(1, q.dequeue())
        self.assertEqual(1, len(q))
        q.dequeue()
        self.assertEqual(True, q.isEmpty())

    def test_Deque(self):
        dq = Deque()
        dq.enqueue(1)
        dq.enqueueLeft('a')
        dq.enqueue(2)
        dq.enqueueLeft('b')
        self.assertEqual('[\'b\', \'a\', 1, 2]', str(dq))
        self.assertEqual(4, len(dq)) # ['b', 'a', 1, 2]
        self.assertEqual('b', dq.dequeue())
        self.assertEqual('a', dq.dequeue())
        self.assertEqual(2, dq.dequeueRight())
        self.assertEqual(1, dq.dequeueRight())
        self.assertEqual(True, dq.isEmpty())

    def test_LinkedList(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        self.assertEqual('[1, 2, 3, 4]', str(ll))
        self.assertEqual(2, ll.pop(1))
        self.assertEqual(4, ll.pop(2))
        self.assertEqual(2, len(ll))
        self.assertEqual(3, ll.pop())
        self.assertEqual(1, ll.pop())
        self.assertEqual(True, ll.isEmpty())

    def test_BinaryHeap(self):
        bh = BinaryHeap()
        bh.buildHeap([9, 5, 6, 2, 3])
        self.assertEqual([2, 3, 6, 5, 9], bh.items)
        self.assertEqual(5, len(bh))
        self.assertEqual(2, bh.delMin())
        self.assertEqual(3, bh.delMin())
        self.assertEqual(3, len(bh))
        self.assertEqual(5, bh.delMin())
        self.assertEqual(6, bh.delMin())
        self.assertEqual(9, bh.delMin())

    def test_BinarySearchTree(self):
        bst = BinarySearchTree()
        bst[1] = 1
        bst[2] = 2
        bst[3] = 3
        self.assertEqual(3, bst[3])
        self.assertEqual(3, len(bst))

if __name__ == '__main__':
    unittest.main()