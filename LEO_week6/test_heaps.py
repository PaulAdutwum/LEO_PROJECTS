import unittest
from heaps import Heap

class TestHeap(unittest.TestCase):

    def test_min_heap_basic(self):
        h = Heap(is_min_heap=True)
        # empty
        self.assertTrue(h.is_empty())
        self.assertEqual(h.size(), 0)
        self.assertIsNone(h.peek())
        self.assertIsNone(h.extract())

        # insert & peek
        h.insert(5)
        self.assertFalse(h.is_empty())
        self.assertEqual(h.size(), 1)
        self.assertEqual(h.peek(), 5)

        # inserting smaller and larger
        h.insert(3)
        self.assertEqual(h.peek(), 3)
        h.insert(4)
        self.assertEqual(h.peek(), 3)

        # extract sequence
        all_vals = [h.extract() for _ in range(h.size())]
        self.assertEqual(all_vals, [3, 4, 5])
        self.assertTrue(h.is_empty())

    def test_min_heap_full_extract(self):
        h = Heap(is_min_heap=True)
        for v in [5, 1, 3, 2, 4]:
            h.insert(v)
        extracted = [h.extract() for _ in range(5)]
        self.assertEqual(extracted, [1, 2, 3, 4, 5])
        self.assertIsNone(h.extract())

    def test_max_heap_basic(self):
        h = Heap(is_min_heap=False)
        self.assertIsNone(h.peek())
        h.insert(5)
        self.assertEqual(h.peek(), 5)
        h.insert(10)
        self.assertEqual(h.peek(), 10)
        h.insert(7)
        self.assertEqual(h.peek(), 10)

        # size/is_empty behavior
        self.assertEqual(h.size(), 3)
        self.assertFalse(h.is_empty())

    def test_max_heap_full_extract(self):
        h = Heap(is_min_heap=False)
        for v in [5, 1, 3, 2, 4]:
            h.insert(v)
        extracted = [h.extract() for _ in range(5)]
        self.assertEqual(extracted, [5, 4, 3, 2, 1])
        self.assertIsNone(h.extract())

    def test_internal_heap_property_after_inserts(self):
        # Test that after inserts, the array always obeys heap property
        for is_min in (True, False):
            h = Heap(is_min_heap=is_min)
            for v in [8, 3, 10, 1, 6, 14, 4]:
                h.insert(v)

            data = h.heap
            for i in range(1, len(data)):
                parent = (i - 1) // 2
                if is_min:
                    self.assertLessEqual(data[parent], data[i],
                        f"Min-heap violation at parent {parent} ({data[parent]}) vs child {i} ({data[i]})")
                else:
                    self.assertGreaterEqual(data[parent], data[i],
                        f"Max-heap violation at parent {parent} ({data[parent]}) vs child {i} ({data[i]})")

    def test_rebuild_whole_heap_by_sifting_down(self):
        # If you want to fully restore a broken heap, you must sift-down from every internal node.
        h = Heap(is_min_heap=False)
        # start with a completely bogus array
        h.heap = [1, 3, 2, 9, 7, 8, 5, 10]
        # rebuild: sift-down from the last parent back to the root
        for idx in range((len(h.heap) // 2) - 1, -1, -1):
            h._heapify_down(idx)

        # now root should be the overall maximum (10) and property holds everywhere
        self.assertEqual(h.peek(), 10)
        data = h.heap
        for i in range(1, len(data)):
            parent = (i - 1) // 2
            self.assertGreaterEqual(data[parent], data[i])

if __name__ == "__main__":
    unittest.main()