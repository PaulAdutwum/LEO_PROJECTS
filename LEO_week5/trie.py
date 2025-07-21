class TrieNode:
    def __init__(self):
        """
        - children: A dictionary to hold children TrieNodes for each character.
        - is_end_of_word: Flag indicating if the node terminates a complete word.
        """
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        """
        Initializes the Trie with an empty root node.
        The root doesn't represent any character.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the Trie.

        Args:
            word (str): The word to be inserted.
        """
        node = self.root
        for char in word.lower():  # normalize to lowercase
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """
        Searches for an exact word in the Trie.

        Args:
            word (str): The word to search.

        Returns:
            bool: True if the word exists in the Trie, False otherwise.
        """
        node = self._traverse(word.lower())
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix):
        """
        Checks if any word in the Trie starts with the given prefix.

        Args:
            prefix (str): The prefix to check.

        Returns:
            bool: True if any word in the Trie starts with the prefix, False otherwise.
        """
        return self._traverse(prefix.lower()) is not None

    def _traverse(self, text):
        """
        Helper method to walk through the Trie along the given text (prefix or word).

        Args:
            text (str): The word or prefix to traverse.

        Returns:
            TrieNode or None: The final node if found, otherwise None.
        """
        node = self.root
        for char in text:
            if char not in node.children:
                return None
            node = node.children[char]
        return node