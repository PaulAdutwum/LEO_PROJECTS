import unittest
from arraylist import ArrayList

class TestArrayList(unittest.TestCase):
    
    def test_add_element(self):
        arr = ArrayList()
        arr.add(1)
        arr.add(2)
        arr.add(3)
        arr.add(4)
        
        self.assertEqual(str(arr), "[1, 2, 3, 4]")
        self.assertEqual(arr.get_size(),4)
        
        
    def test_insert_elements(self):
        arr = ArrayList()
        arr.add(15)
        arr.add(35)
        arr.insert(1,25)
        self.assertEqual(str(arr), "[15, 25, 35]")
        
        
    def test_get_element(self):
        arr = ArrayList()
        arr.add(50)
        self.assertEqual(arr.get(0), 50)
        with self.assertRaises(IndexError):
            arr.get(1)  
    
    def test_remove_element(self):
        arr = ArrayList()
        arr.add(5)
        arr.add(15)
        arr.add(25)
        removed = arr.remove(1)
        self.assertEqual(removed, 15)
        self.assertEqual(str(arr), "[5, 25]")
        self.assertEqual(arr.get_size(), 2)

    def test_is_empty(self):
        arr = ArrayList()
        self.assertTrue(arr.is_empty())
        arr.add(1)
        self.assertFalse(arr.is_empty())

    def test_get_size(self):
        arr = ArrayList()
        for i in range(7):
            arr.add(i)
        self.assertEqual(arr.get_size(), 7)

    def test_resize_with_load_factor(self):
        arr = ArrayList()
        for i in range(10):  
            arr.add(i)
        self.assertEqual(arr.get_size(), 10)
        self.assertEqual(str(arr), "[" + ", ".join(str(i) for i in range(10)) + "]")

    def test_insert_invalid_index(self):
        arr = ArrayList()
        arr.add(1)
        with self.assertRaises(IndexError):
            arr.insert(5, 100)

    def test_remove_from_empty_list(self):
        arr = ArrayList()
        with self.assertRaises(IndexError):
            arr.remove(0)

    def test_get_invalid_index(self):
        arr = ArrayList()
        arr.add(99)
        with self.assertRaises(IndexError):
            arr.get(-1)
        with self.assertRaises(IndexError):
            arr.get(2)
    
    def test_remove_until_empty_then_fail(self):
        arr = ArrayList()
        arr.add(1)
        arr.remove(0) 
        with self.assertRaises(IndexError):
            arr.remove(0)  

    def test_insert_negative_index(self):
        arr = ArrayList()
        arr.add(1)
        with self.assertRaises(IndexError):
            arr.insert(-1, 999)

if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
        
    

