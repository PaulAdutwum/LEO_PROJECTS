import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_add(self):
        self.ll.add(1)
        self.ll.add(2)
        self.ll.add(3)
        self.assertEqual(self.ll.size(), 3)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 2)
        self.assertEqual(self.ll.get(2), 3)

    def test_insert_head(self):
        self.ll.add(1)
        self.ll.insert(0, 0)
        self.assertEqual(self.ll.get(0), 0)
        self.assertEqual(self.ll.get(1), 1)
        self.assertEqual(self.ll.size(), 2)

    def test_insert_middle(self):
        self.ll.add(1)
        self.ll.add(3)
        self.ll.insert(1, 2)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 2)
        self.assertEqual(self.ll.get(2), 3)

    def test_insert_end(self):
        self.ll.add(1)
        self.ll.insert(1, 2)
        self.assertEqual(self.ll.get(1), 2)
        self.assertEqual(self.ll.size(), 2)

    def test_get_invalid_index(self):
        self.ll.add(1)
        with self.assertRaises(IndexError):
            self.ll.get(-1)
        with self.assertRaises(IndexError):
            self.ll.get(1)

    def test_remove_head(self):
        self.ll.add(1)
        self.ll.add(2)
        self.ll.remove(0)
        self.assertEqual(self.ll.get(0), 2)
        self.assertEqual(self.ll.size(), 1)

    def test_remove_middle(self):
        self.ll.add(1)
        self.ll.add(2)
        self.ll.add(3)
        self.ll.remove(1)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 3)
        self.assertEqual(self.ll.size(), 2)

    def test_remove_last(self):
        self.ll.add(1)
        self.ll.add(2)
        self.ll.remove(1)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.size(), 1)

    def test_remove_invalid_index(self):
        self.ll.add(1)
        with self.assertRaises(IndexError):
            self.ll.remove(-1)
        with self.assertRaises(IndexError):
            self.ll.remove(1)

    def test_is_empty(self):
        self.assertTrue(self.ll.is_empty())
        self.ll.add(1)
        self.assertFalse(self.ll.is_empty())
        self.ll.remove(0)
        self.assertTrue(self.ll.is_empty())
    
    def test_has_cycle(self):
        
        self.ll.add(1)
        self.ll.add(2)
        self.ll.add(3)
        self.assertFalse(self.ll.has_cycle())

        last = self.ll.head
        while last.next:
            last = last.next
        last.next = self.ll.head  

        self.assertTrue(self.ll.has_cycle())


if __name__ == "__main__":
    unittest.main()