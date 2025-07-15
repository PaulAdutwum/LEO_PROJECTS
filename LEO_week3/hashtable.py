class Node:
    def __init__(self, key, value):
        """
        Initialize a Node with a key, value, and reference to the next node.
        """
        self.key = key
        self.value = value
        self.next = None

class Hashtable:
    def __init__(self, initial_capacity=10, load_factor=0.75):
        """
        Initialize the Hashtable with a fixed initial capacity.
        """
        self.capacity = initial_capacity
        self._count = 0
        self.buckets = [None] * self.capacity
        self.load_factor = load_factor

    def put(self, key, value):
        """
        Add or update a key-value pair in the Hashtable.
        """
        idx = self._hash(key)
        node = self.buckets[idx]

        # If key exists, update it
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next

        # Otherwise insert new node at head
        new_node = Node(key, value)
        new_node.next = self.buckets[idx]
        self.buckets[idx] = new_node
        self._count += 1

        # Resize if load factor exceeded
        if self._count / self.capacity > self.load_factor:
            self._resize()

    def get(self, key):
        """
        Retrieve the value associated with the given key, or None if missing.
        """
        idx = self._hash(key)
        node = self.buckets[idx]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def remove(self, key):
        """
        Remove the key-value pair for `key`. Return True if removed, False otherwise.
        """
        idx = self._hash(key)
        node = self.buckets[idx]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.buckets[idx] = node.next
                self._count -= 1
                return True
            prev, node = node, node.next

        return False

    def size(self):
        """
        Return the current number of elements in the Hashtable.
        """
        return self._count

    def is_empty(self):
        """
        Check if the Hashtable is empty.
        """
        return self._count == 0

    def _hash(self, key):
        """
        Compute a non-negative bucket index.
        """
        return (hash(key) & 0x7FFFFFFF) % self.capacity

    def _resize(self):
        """
        Double capacity and rehash all existing entries.
        """
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        old_count = self._count
        self._count = 0

        for head in old_buckets:
            node = head
            while node:
                self.put(node.key, node.value)
                node = node.next

        self._count = old_count  # restore correct count