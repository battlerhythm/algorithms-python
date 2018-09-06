import unittest
import cProfile
from mysort import BubbleSort, InsertionSort, SelectionSort, MergeSort

class TestSortMethods(unittest.TestCase):
    b = BubbleSort()
    ins = InsertionSort()
    sel = SelectionSort()
    mrg = MergeSort()

    def test_BubbleSort(self):
        l = [e for e in reversed(range(5))]
        l = self.b.sort(l)
        self.assertEqual(l, [e for e in range(5)])

    def test_InsertionSort(self):
        l = [e for e in reversed(range(5))]
        l = self.ins.sort(l)
        self.assertEqual(l, [e for e in range(5)])

    def test_SelectionSort(self):
        l = [e for e in reversed(range(5))]
        l = self.sel.sort(l)
        self.assertEqual(l, [e for e in range(5)])

    def test_MergeSort(self):
        l = [e for e in reversed(range(5))]
        l = self.mrg.sort(l)
        self.assertEqual(l, [e for e in range(5)])

if __name__ == '__main__':
    unittest.main()
    # cProfile.run('unittest.main()')
    