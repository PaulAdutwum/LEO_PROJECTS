import unittest
from hashtable import Hashtable, Node

class TestHashtable(unittest.TestCase):
    def setUp(self):
        # Start with small capacity to force resizing
        self.ht = Hashtable(initial_capacity=4, load_factor=0.75)

    def test_empty_table(self):
        self.assertTrue(self.ht.is_empty())
        self.assertEqual(self.ht.size(), 0)
        self.assertIsNone(self.ht.get("no_key"))
        self.assertFalse(self.ht.remove("no_key"))

    def test_put_and_get(self):
        self.ht.put("a", 1)
        self.ht.put("b", 2)
        self.ht.put("c", 3)
        self.assertEqual(self.ht.size(), 3)
        self.assertEqual(self.ht.get("a"), 1)
        self.assertEqual(self.ht.get("b"), 2)
        self.assertEqual(self.ht.get("c"), 3)

    def test_overwrite(self):
        self.ht.put("key", "first")
        self.ht.put("key", "second")
        self.assertEqual(self.ht.size(), 1)
        self.assertEqual(self.ht.get("key"), "second")

    def test_remove(self):
        self.ht.put("x", 10)
        self.ht.put("y", 20)
        self.assertTrue(self.ht.remove("x"))
        self.assertIsNone(self.ht.get("x"))
        self.assertEqual(self.ht.size(), 1)
        self.assertFalse(self.ht.remove("x"))
        self.assertTrue(self.ht.remove("y"))
        self.assertTrue(self.ht.is_empty())

    def test_collision_chaining(self):
        # Force a bucket collision
        k1, k2 = "Aa", "BB"
        self.assertEqual(self.ht._hash(k1), self.ht._hash(k2))
        self.ht.put(k1, "val1")
        self.ht.put(k2, "val2")
        self.assertEqual(self.ht.get(k1), "val1")
        self.assertEqual(self.ht.get(k2), "val2")
        # Remove the second node in the chain
        self.assertTrue(self.ht.remove(k2))
        self.assertIsNone(self.ht.get(k2))
        self.assertEqual(self.ht.get(k1), "val1")
        self.assertEqual(self.ht.size(), 1)

    def test_resize(self):
        initial_cap = self.ht.capacity
        for i in range(1, 6):
            self.ht.put(f"key{i}", i)
        self.assertGreater(self.ht.capacity, initial_cap)
        for i in range(1, 6):
            self.assertEqual(self.ht.get(f"key{i}"), i)
        self.assertEqual(self.ht.size(), 5)

    def test_none_key_and_value(self):
        self.ht.put(None, "none_key")
        self.ht.put("none_value", None)
        self.assertEqual(self.ht.get(None), "none_key")
        self.assertIsNone(self.ht.get("none_value"))
        self.assertTrue(self.ht.remove(None))
        self.assertIsNone(self.ht.get(None))

    def test_repeated_insert_remove(self):
        for i in range(3):
            self.ht.put("temp", i)
            self.assertEqual(self.ht.get("temp"), i)
            self.assertTrue(self.ht.remove("temp"))
            self.assertFalse(self.ht.remove("temp"))
        self.assertTrue(self.ht.is_empty())

if __name__ == "__main__":
    unittest.main(verbosity=2)