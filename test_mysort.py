import unittest
import cProfile
from mysort import BubbleSort, InsertionSort, SelectionSort, MergeSort, QuickSort

class TestSortMethods(unittest.TestCase):
    bb = BubbleSort()
    ins = InsertionSort()
    sel = SelectionSort()
    mrg = MergeSort()
    qck = QuickSort()

    def test_BubbleSort(self):
        alist = [e for e in reversed(range(5))]
        alist = self.bb.sort(alist)
        self.assertEqual(alist, [e for e in range(5)])

    def test_InsertionSort(self):
        alist = [e for e in reversed(range(5))]
        alist = self.ins.sort(alist)
        self.assertEqual(alist, [e for e in range(5)])

    def test_SelectionSort(self):
        alist = [e for e in reversed(range(5))]
        alist = self.sel.sort(alist)
        self.assertEqual(alist, [e for e in range(5)])

    def test_MergeSort(self):
        alist = [e for e in reversed(range(5))]
        alist = self.mrg.sort(alist)
        self.assertEqual(alist, [e for e in range(5)])

    def test_QuickSort(self):
        alist = [e for e in reversed(range(5))]
        alist = self.qck.sort(alist)
        self.assertEqual(alist, [e for e in range(5)])

if __name__ == '__main__':
    unittest.main()
    # cProfile.run('unittest.main()')
    