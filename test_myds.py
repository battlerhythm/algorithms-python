import unittest
from myds import Stack, Queue, Deque, LinkedList

class TestDsMethods(unittest.TestCase):
    stk = Stack()
    q = Queue()
    dq = Deque()
    ll = LinkedList()

    def test_Stack(self):
        self.stk.push(1)
        self.stk.push('a')
        self.assertEqual('a', self.stk.peek())
        self.assertEqual(2, self.stk.size())
        self.assertEqual('a', self.stk.pop())
        self.assertEqual(1, self.stk.size())
        self.assertEqual(False, self.stk.isEmpty())
        self.stk.pop()
        self.assertEqual(True, self.stk.isEmpty())
        self.assertEqual(0, self.stk.size())

    def test_Queue(self):
        self.q.enqueue(1)
        self.q.enqueue('a')
        self.assertEqual(2, self.q.size())
        self.assertEqual(1, self.q.dequeue())
        self.assertEqual(1, self.q.size())
        self.q.dequeue()
        self.assertEqual(True, self.q.isEmpty())

    def test_Deque(self):
        self.dq.addFront(1)
        self.dq.addRear('a')
        self.dq.addFront(2)
        self.dq.addRear('b')
        self.assertEqual(4, self.dq.size()) # [2, 1, 'a', 'b']
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
        self.assertEqual(2, self.ll.pop(1))
        self.assertEqual(4, self.ll.pop(2))
        self.assertEqual(2, self.ll.getSize())
        self.assertEqual(3, self.ll.pop())
        self.assertEqual(1, self.ll.pop())
        self.assertEqual(True, self.ll.isEmpty())


if __name__ == '__main__':
    unittest.main()