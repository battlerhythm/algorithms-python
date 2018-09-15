import unittest
import cProfile
from mysort import BubbleSort, InsertionSort, SelectionSort, MergeSort, QuickSort

class TestSortMethods(unittest.TestCase):
    answer = [e for e in range(5)]

    def test_BubbleSort(self):
        alist1 = [4, 3, 2, 1, 0]
        alist2 = [0, 1, 4, 3, 2]
        self.assertEqual(BubbleSort.sort(alist1), self.answer)
        self.assertEqual(BubbleSort.sort(alist2), self.answer)

    def test_InsertionSort(self):
        alist1 = [4, 3, 2, 1, 0]
        alist2 = [0, 1, 4, 3, 2]
        self.assertEqual(InsertionSort.sort(alist1), self.answer)
        self.assertEqual(InsertionSort.sort(alist2), self.answer)

    def test_SelectionSort(self):
        alist1 = [4, 3, 2, 1, 0]
        alist2 = [0, 1, 4, 3, 2]
        self.assertEqual(SelectionSort.sort(alist1), self.answer)
        self.assertEqual(SelectionSort.sort(alist2), self.answer)

    def test_MergeSort(self):
        alist1 = [4, 3, 2, 1, 0]
        alist2 = [0, 1, 4, 3, 2]
        self.assertEqual(MergeSort.sort(alist1), self.answer)
        self.assertEqual(MergeSort.sort(alist2), self.answer)

    def test_QuickSort(self):
        alist1 = [4, 3, 2, 1, 0]
        alist2 = [0, 1, 4, 3, 2]
        self.assertEqual(QuickSort.sort(alist1), self.answer)
        self.assertEqual(QuickSort.sort(alist2), self.answer)

if __name__ == '__main__':
    unittest.main()
    # cProfile.run('unittest.main()')
    