import unittest
import cProfile
from mysort import BubbleSort, InsertionSort, SelectionSort, MergeSort, QuickSort

class TestSortMethods(unittest.TestCase):
    dataSet = [e for e in reversed(range(5))]
    answer = [e for e in range(5)]

    def test_BubbleSort(self):
        alist = self.dataSet
        self.assertEqual(BubbleSort.sort(alist), self.answer)

    def test_InsertionSort(self):
        alist = self.dataSet
        self.assertEqual(InsertionSort.sort(alist), self.answer)

    def test_SelectionSort(self):
        alist = self.dataSet
        self.assertEqual(SelectionSort.sort(alist), self.answer)

    def test_MergeSort(self):
        alist = self.dataSet
        self.assertEqual(MergeSort.sort(alist), self.answer)

    def test_QuickSort(self):
        alist = self.dataSet
        self.assertEqual(QuickSort.sort(alist), self.answer)

if __name__ == '__main__':
    unittest.main()
    # cProfile.run('unittest.main()')
    