import unittest
from myds import Stack

class TestDsMethods(unittest.TestCase):
    stk = Stack()

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
        

if __name__ == '__main__':
    unittest.main()