class ArrayList:
    """
    A dynamic array-based data structure that resizes automatically.
    """

    def __init__(self):
        """Initializes an empty ArrayList with initial capacity of 4."""
        self.capacity = 4
        self.size = 0
        self.data = [None] * self.capacity
        self.load_factor = 0.75

    def _resize(self):
        """Doubles the capacity of the array when it runs out of space."""
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity

    def add(self, element):
        """Appends an element to the end of the ArrayList."""
        if self.size >= self.capacity * self.load_factor:
            self._resize()
        self.data[self.size] = element
        self.size += 1

    def insert(self, index, element):
        """Inserts an element at the specified index, shifting elements right."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        if self.size >= self.capacity * self.load_factor:
            self._resize()

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = element
        self.size += 1

    def get(self, index):
        """Retrieves an element at the specified index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def remove(self, index):
        """Removes an element at the specified index and shifts elements left."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        removed_element = self.data[index]

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.size - 1] = None
        self.size -= 1
        return removed_element

    def get_size(self):
        """Returns the number of elements in the ArrayList."""
        return self.size

    def is_empty(self):
        """Returns True if the ArrayList is empty, else False."""
        return self.size == 0

    def __str__(self):
        """Returns a string representation of the current ArrayList."""
        return "[" + ", ".join(str(self.data[i]) for i in range(self.size)) + "]"

