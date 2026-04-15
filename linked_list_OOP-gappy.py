class Node:
    """
    A Node class that represents each element of the linked list.
    It holds the data and a reference to the next node.
    The __init__ procedure in Python is where you write a constructor which
    sets initial values of a newly created object.
    """
    def __init__(self, theData):
        self.data = theData  # Store the data for this node
        self.next = None  # The reference to the next node is initially None


class LinkedList:
    """
    A LinkedList class to implement the linked list operations.
    Just a wrapper for a Node really, initially pointing at None (null)
    """
    def __init__(self):
        self.head = None  # Initially, the linked list is empty

    def append(self, theData):
        """
        Add a node with the given data to the end of the linked list.
        """
        new_node = Node(theData)  # Create a new node
        if self.head == ???????  # If the list is empty
            self.head = ???????
        else:
            current = self.head
            while current.next != ???????:  # Traverse until current is the last node...
                current = ???????
            current.next = ???????  # Make the last node point to the new node.

    def insert_at_beginning(self, data):
        """
        Insert a node with the given data at the beginning of the linked list.
        """
        new_node = Node(???????)  # Create a new node
        new_node.next = self.???????  # Point new node to ???????:
        self.head = ???????  # Move the head to the new node

    def delete(self, key):
        """
        Delete the first node containing the specified data (key).
        """
        current = self.head

        # If the list is empty..
        if current == ???????:
            print("The list is empty.")
            return

        # If the node to be deleted is the head
        if current.data == key:
            self.head = ???????  # Move head to ???????
            current = None  # Delete the old head
            return

        # Search for the node to be deleted
        prev = None
        while current != None and current.data != key:
            prev = current
            current = ???????

        # If the key is not found
        if current == None:
            print(f"Node with data {key} not found.")
            return

        # Remove the node from the list
        prev.next = ???????
        current = None  # Delete the node

    def traverse(self):
        """
        Print all the elements in the linked list.
        """
        current = self.head
        if current == None:
            print("The list is empty.")
            return
        while current != None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of list


# Main section to demonstrate the linked list operations

# Create a new linked list by calling its constructor...
my_list = LinkedList()

# Append elements to the linked list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Linked List after appending elements:")
my_list.traverse()

# Insert an element at the beginning
my_list.insert_at_beginning(5)
print("\nLinked List after inserting 5 at the beginning:")
my_list.traverse()

# Delete an element from the linked list
my_list.delete(20)
print("\nLinked List after deleting node with data 20:")
my_list.traverse()

# Try deleting a non-existing element
my_list.delete(100)

# Final state of the list
print("\nFinal state of the Linked List:")
my_list.traverse()