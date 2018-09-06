import unittest
from myds import Stack, Queue

class TestDsMethods(unittest.TestCase):
    stk = Stack()
    q = Queue()

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
        

if __name__ == '__main__':
    unittest.main()