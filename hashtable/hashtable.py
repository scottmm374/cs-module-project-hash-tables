class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
Min_LF = .2
Max_LF = .7


class HashTable:

    def __init__(self, capacity):
        self.hash_arr = [None] * capacity
        self.capacity = capacity
        self.occupied_slots = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        encoded_str = key.encode()
        hash = 5381
        for x in encoded_str:
            hash = ((hash << 5) + hash) + x
            print(hash)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """

        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % len(self.capacity)

    def put(self, key, value):
        # Array version
        self.capacity[self.hash_index(key)] = value

        """
        # Search the linked list for a Node with the same KEY as the one we are inserting
                # If it exists:
                    # change the value of the node
                    # return
            # if it doesnt exist do the following steps
​
            # the first item in the hash_array is the HEAD of the linked list
            # Create a new hashTableEntry and add it to the HEAD of the linked list
            # Make the new entry the new HEAD
        """

    def delete(self, key):

        # Array version
        if self.capacity[self.hash_index(key)] is None:
            print("key not found")
        else:
            self.capacity[self.hash_index(key)] = None

        """
        # Search through the linked list until we find the node to delete 
        # Delete the node if found

        """

    def get(self, key):
        # Array version
        return self.capacity[self.hash_index(key)]

        """
        # Search / Loop through the linked list at the hashed index
        # Compare the key to search to the keys in the nodes
        # if you find it, return the value
        # if not, return None
        """

    def resize(self, new_capacity):
        """
       # Create a blank new array with double the size of the old array
        # We have to rehash every single item because the hash function has changed
            # go through each slot in the array
                # go through each item in each linked list in the array
                    # rehash the key in each item and store in new array
​
        # make new array the new storage

        """


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")

    # string = HashTableEntry.HashTable.djb2("apple", )
    # print(string)
