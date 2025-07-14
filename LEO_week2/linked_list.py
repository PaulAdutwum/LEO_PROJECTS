class Node:
    def __init__(self, data=None):
    #Initialize a Node with data and a reference to the next node.
        self.data = data 
        self.next = None
        

class LinkedList:
    def __init__(self):
    #Initialize the LinkedList with a head node.
        
        self.head = None
        self._size = 0

    def add(self, element):
    #Add an element to the end of the LinkedList.
        
        new_node = Node(element)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1  

    def insert(self, index, element):
    #Insert an element at the specified index.
        
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self._size +=1 

    def get(self, index):
    #Retrieve the element at the specified index.
        
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def remove(self, index):
    #Remove the element at the specified index.
        
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self._size -= 1

    def size(self):
    #Return the current number of elements in the LinkedList.
        return self._size

    def is_empty(self):
        #Check if the LinkedList is empty.
        return self.head is None
    
    def has_cycle(self):
    # Check if there is a cycle in the linkedlist
        fast = self.head 
        slow = self.head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast:
                return True 
        return False 
                

