class Heap:
    def __init__(self, is_min_heap=True):
        """
        Initialize the Heap.
        
        Args:
            is_min_heap (bool): If True, creates a min-heap; otherwise, a max-heap.
        """
        self.heap = []
        self.is_min_heap = is_min_heap

    def insert(self, element):
        """
        Add an element to the heap while maintaining the heap property.
        """
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        """
        Remove and return the root element (min or max).
        Returns:
            The root element, or None if the heap is empty.
        """
        if self.is_empty():
            return None

        root = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)

        return root

    def peek(self):
        """
        Return the root element (min or max) without removing it.
        """
        return self.heap[0] if not self.is_empty() else None

    def size(self):
        """
        Return the current number of elements in the heap.
        """
        return len(self.heap)

    def is_empty(self):
        """
        Check if the heap is empty.
        """
        return len(self.heap) == 0

    def _heapify_up(self, index):
        """
        Restore the heap property by moving the element at the given index up.
        """
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self._compare(index, parent_index):
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """
        Restore the heap property by moving the element at the given index down.
        """
        child_index = self._get_priority_child(index)

        if child_index != -1 and self._compare(child_index, index):
            self._swap(index, child_index)
            self._heapify_down(child_index)

    def _get_priority_child(self, index):
        """
        Get the child index that should be compared (either left or right).
        """
        left = 2 * index + 1
        right = 2 * index + 2
        size = self.size()

        if left >= size:
            return -1
        if right >= size:
            return left

        if self._compare(left, right):
            return left
        else:
            return right

    def _compare(self, i, j):
        """
        Compare two indices based on min-heap or max-heap rules.
        """
        if self.is_min_heap:
            return self.heap[i] < self.heap[j]
        else:
            return self.heap[i] > self.heap[j]

    def _swap(self, i, j):
        """
        Swap elements at indices i and j.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]