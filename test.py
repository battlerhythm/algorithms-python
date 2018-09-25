import unittest
import cProfile
from mysort import BubbleSort, InsertionSort, SelectionSort, MergeSort, QuickSort
from myds import Stack, Queue, Deque, LinkedList, BinaryHeap
from mytree import BinarySearchTree, AvlTree
from mygraphs import Graph

class TestSortMethods(unittest.TestCase):
    def test_BubbleSort(self):
        alist1 = [4, 3, 2, 1, 0]
        alist2 = [0, 1, 4, 3, 2]
        self.assertEqual(BubbleSort.sort(alist1), [0, 1, 2, 3, 4])
        self.assertEqual(BubbleSort.sort(alist2), [0, 1, 2, 3, 4])

    def test_InsertionSort(self):
        alist1 = [4, 3, 2, 1, 0]
        alist2 = [0, 1, 4, 3, 2]
        self.assertEqual(InsertionSort.sort(alist1), [0, 1, 2, 3, 4])
        self.assertEqual(InsertionSort.sort(alist2), [0, 1, 2, 3, 4])

    def test_SelectionSort(self):
        alist1 = [4, 3, 2, 1, 0]
        alist2 = [0, 1, 4, 3, 2]
        self.assertEqual(SelectionSort.sort(alist1), [0, 1, 2, 3, 4])
        self.assertEqual(SelectionSort.sort(alist2), [0, 1, 2, 3, 4])

    def test_MergeSort(self):
        alist1 = [4, 3, 2, 1, 0]
        alist2 = [0, 1, 4, 3, 2]
        self.assertEqual(MergeSort.sort(alist1), [0, 1, 2, 3, 4])
        self.assertEqual(MergeSort.sort(alist2), [0, 1, 2, 3, 4])

    def test_QuickSort(self):
        alist1 = [4, 3, 2, 1, 0]
        alist2 = [0, 1, 4, 3, 2]
        self.assertEqual(QuickSort.sort(alist1), [0, 1, 2, 3, 4])
        self.assertEqual(QuickSort.sort(alist2), [0, 1, 2, 3, 4])

class TestDSMethods(unittest.TestCase):
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
        self.assertEqual('[]', str(ll))
        with self.assertRaises(IndexError): ll.pop()

    def test_BinaryHeap(self):
        bh = BinaryHeap()
        bh.buildHeap([9, 5, 6, 2, 3])
        self.assertEqual([2, 3, 6, 5, 9], bh.items)
        self.assertEqual(5, len(bh))
        self.assertEqual(2, bh.delMin())
        self.assertEqual(3, bh.delMin())
        self.assertEqual(3, len(bh))
        bh.insert(4)
        self.assertEqual(4, len(bh))
        self.assertEqual(4, bh.delMin())
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
        del bst[3]
        with self.assertRaises(KeyError): del bst[3]
        self.assertEqual(2, len(bst))
        self.assertEqual(False, 3 in bst)
        self.assertEqual(True, 2 in bst)
        bst[4] = 4
        bst[7] = 7
        bst[5] = 5
        bst[6] = 6
        self.assertEqual(6, len(bst))
        with self.assertRaises(KeyError): bst[3]
        self.assertEqual(7, bst[7])
        del bst[1], bst[2], bst[4]
        self.assertEqual(3, len(bst))
        del bst[5], bst[6], bst[7]

    def test_AvlTree(self):
        avl = AvlTree()
        avl[1] = 1
        avl[2] = 2
        avl[3] = 3
        avl[4] = 4
        avl[5] = 5
        self.assertEqual(5, len(avl))
        self.assertEqual(2, avl[2])
        avl[-1] = -1
        avl[-2] = -2
        avl[-3] = -3
        avl[-4] = -4
        avl[-5] = -5
        self.assertEqual(10, len(avl))
        self.assertEqual(-3, avl[-3])

    def test_Graph(self):
        g = Graph()
        for i in range(6):
            g.addVertex(i)
        self.assertEqual(set([0, 1, 2, 3, 4, 5]), g.vertices)
        g.addEdge(0,1,5)
        g.addEdge(0,5,2)
        g.addEdge(1,2,4)
        g.addEdge(2,3,9)
        g.addEdge(3,4,7)
        g.addEdge(3,5,3)
        g.addEdge(4,0,1)
        g.addEdge(5,4,8)
        g.addEdge(5,2,1)
        self.assertEqual((6, 9), g.size) # (vertices, edges)

if __name__ == '__main__':
    unittest.main()
    cProfile.run('unittest.main()')
    