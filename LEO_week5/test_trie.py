import unittest

from trie import Trie
class TestTrie(unittest.TestCase):

    def setUp(self):
        """Initialize a fresh Trie before each test."""
        self.trie = Trie()
        words = ["apple", "app", "apex", "bat", "bath", "banana"]
        for word in words:
            self.trie.insert(word)

    def test_search_existing_words(self):
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("apex"))
        self.assertTrue(self.trie.search("bat"))
        self.assertTrue(self.trie.search("bath"))
        self.assertTrue(self.trie.search("banana"))

    def test_search_non_existing_words(self):
        self.assertFalse(self.trie.search("appl"))
        self.assertFalse(self.trie.search("bathe"))
        self.assertFalse(self.trie.search("band"))
        self.assertFalse(self.trie.search("bananas"))

    def test_starts_with_valid_prefixes(self):
        self.assertTrue(self.trie.starts_with("ap"))
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("b"))
        self.assertTrue(self.trie.starts_with("bat"))
        self.assertTrue(self.trie.starts_with("ban"))

    def test_starts_with_invalid_prefixes(self):
        self.assertFalse(self.trie.starts_with("cat"))
        self.assertFalse(self.trie.starts_with("z"))
        self.assertFalse(self.trie.starts_with("banaana"))

    def test_insert_and_search_single_letter(self):
        self.trie.insert("a")
        self.assertTrue(self.trie.search("a"))
        self.assertTrue(self.trie.starts_with("a"))

    def test_empty_string_insertion(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))
        self.assertTrue(self.trie.starts_with(""))

    def test_overlapping_insertions(self):
        self.trie.insert("batman")
        self.assertTrue(self.trie.search("batman"))
        self.assertTrue(self.trie.starts_with("batm"))
        self.assertTrue(self.trie.starts_with("bat"))
        self.assertTrue(self.trie.search("bat"))  
    def test_prefix_not_full_word(self):
        self.assertFalse(self.trie.search("ba"))  

if __name__ == "__main__":
    unittest.main()