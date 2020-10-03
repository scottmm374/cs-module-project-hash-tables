class HashTableEntry:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None


class HashTable:

    def __init__(self, capacity):
        self.hash_array = [None] * capacity
        self.capacity = capacity
        self.number_of_items = 0

    # A hash function needs to take a string and return a single number
    # It must be deterministic (i.e the same result every time given the same input)
    def hash_fn(self, s):
        # convert the string to a UTF-8 (Unicode) representation
        encoded_string = s.encode()  # O(1)
        result = 0
        # every character is now a number based off UTF-8 rules
        for byte_char in encoded_string:
            # simply add the numbers up to get one single new number
            result += byte_char

        return result

    def hash_index(self, key):
        hash_value = self.hash_fn(key)
        index = hash_value % len(self.hash_array)
        return index

    # To insert a key and value to this hash_table
    # - hash the key to convert it to a number
    # - take that number and MOD it by the size of hash_table
    # - insert the VALUE into the index given by the MOD operation

    def put(self, key, value):
        index = self.hash_index(key)
        if self.hash_array[index] is not None:
            # Search the linked list for a Node with the same KEY as the one we are inserting
            # If it exists:
            # change the value of the node
            # return
            # if it doesnt exist do the following steps

            # the first item in the hash_array is the HEAD of the linked list
            # Create a new hashTableEntry and add it to the HEAD of the linked list
            # Make the new entry the new HEAD

            pass
        self.hash_array[index] = HashTableEntry(key, value)

    # To retrieve a value given a specific key from a hash_table
    # - hash the key to convert it to a number
    # - use MOD (%) to find the index within the underlying array
    # - use this new index to find the value in the array

    def get(self, key):
        index = self.hash_index(key)

        # Search / Loop through the linked list at the hashed index
        # Compare the key to search to the keys in the nodes
        # if you find it, return the value
        # if not, return None

        return self.hash_array[index].value

    def delete(self, key):
        index = self.hash_index(key)
        # Search through the linked list until we find the node to delete
        # Delete the node if found

        pass

    def resize(self):
        # Create a blank new array with double the size of the old array
        # We have to rehash every single item because the hash function has changed
        # go through each slot in the array
        # go through each item in each linked list in the array
        # rehash the key in each item and store in new array

        # make new array the new storage
        pass


table = HashTable(4)
table.put('banana', "banana is yellow")
table.put('apple', "apple is green")
table.put('pickle', "pickle is green")
table.put('tomato', "tomato is red")
print(table.get('pickle'))


# Node Class
class LinkedList:

    def __init__(self):
        self.head = None

    def find(self, key):
        current_node = self.head

        while current_node is not None:
            # Compare the current node with what we are looking for
            if current_node.key == key:
                return current_node
            current_node = current_node.next

        return None

    def insert_at_head(self, node):
        # Link the node to the current HEAD
        node.next = self.head
        # Set head pointer to new node
        self.head = node

    def delete(self, key):
        # Handle the case where the node to delete is the HEAD
        if key == self.head.key:
            self.head = self.head.next
            return self.head

        prev = None
        curr = self.head

        while curr is not None:
            # loop until we find the right key
            if curr.key == key:
                # found it!
                prev.next = curr.next
                return curr

            # move the pointers over
            prev = curr
            curr = curr.next
        return None
