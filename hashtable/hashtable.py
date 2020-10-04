class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"HTEntry: ({self.key}, {self.value}) -> {self.next}"

    def __str__(self):
        return f"HTEntry: ({self.key}, {self.value}) -> {self.next}"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
Min_LF = .2
Max_LF = .7


class HashTable:

    def __init__(self, capacity):
        self.hash_list = [None] * capacity
        # update capacity when resizing, then we can just re use hash_list I think.
        self.capacity = 8
        self.occupied_slots = 0
        # self.head = None

    def __str__(self):
        print(f"HashTable: ({self.hash_list}, {self.occupied_slots})")

    def get_num_slots(self):
        # Return length of data-structure
        return len(self.hash_list)

    def get_load_factor(self):
        return round(self.occupied_slots / self.capacity, 1)

    def djb2(self, key):

        encoded_str = key.encode()
        hash = 5381
        for x in encoded_str:
            hash = ((hash << 5) + hash) + x
        # hashed_key = hash & 0xFFFFFFFF
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        return self.djb2(key) % len(self.hash_list)

    def put(self, key, value):
        loadFactor = self.get_load_factor()
        index = self.hash_index(key)
        curr_node = self.hash_list[index]

        # Check load Factor first
        print("LOAD FACTOR: ", loadFactor)
        if loadFactor < Max_LF:
            if curr_node is None:
                new_node = self.hash_list[self.hash_index(key)] = value
                self.occupied_slots += 1
                print("NEW NODE:\n", new_node, "Index: ", index)
                return new_node
            if curr_node is not None:
                new_node = HashTableEntry(key, value)
                new_node.next = curr_node
                new_node = self.hash_list[self.hash_index(key)] = value
                self.occupied_slots += 1
                print("NEW NODE:\n", new_node, "index: ", index)
                return new_node
        print("Load factor > .7", loadFactor)
        return self.resize()

    def delete(self, key):

        if self.hash_list[self.hash_index(key)] is None:
            print("key not found")

            # if Index occupied, BUT Key doesnt match:    CAN PROB DO ALL THIS IN FIND()
            #     Iterate using next, to find key
            #         if not found:
            #             return not found
            #         if Found :
            #             value = none (delete)
            #             subtract 1 from occupied slots.
            # Check load factor, for being too small, if it is too small resize, smaller but min 8 slots.

        else:
            self.hash_list[self.hash_index(key)] = None

        """
        # Search through the linked list until we find the node to delete
        # Delete the node if found

        # Search the linked list for a Node with the same KEY as the one we are inserting
                # If it exists:
                    # change the value of the node
                    # return
            # if it doesnt exist do the following steps
​
            # the first item in the hash_list is the HEAD of the linked list
            # Create a new hashTableEntry and add it to the HEAD of the linked list
            # Make the new entry the new HEAD
     """

    def get(self, key):

        Curr_key_index = self.hash_index(key)
        arr_index = self.hash_list[Curr_key_index]
        hash_key = self.djb2(key)

        if Curr_key_index == arr_index:
            # check to see if it matches key_hash.
            # if index == key[index]:
            print(self.hash_list[self.hash_index(key)], "Found key")
            return self.hash_list[self.hash_index(key)]
            #  If is doesnt match, then findNode method for LL
        else:
            print(
                f" Not Found, see below: \n hashKey: {hash_key}, index: {Curr_key_index}, key: {key}")
            # return self.findNode(key, index)
            # return self.findNode(key)
        # print("Key not found")
        # return None

    # def findNode(self, key, index):
    #     # key = self.djb2(key)
    #     current_node = self.head
    #     # hash_key = self.djb2(key)
    #     print("CURRENT NODE in FINDNODE:\n", current_node)
    #     print("KEY IN FINDNODE:\n", key)

    #     while current_node is not None:
    #         if current_node == key:
    #             print(current_node, "if equal key")
    #             return current_node
    #         current_node = current_node.next
    #     return None

        # Search / Loop through the linked list at the hashed index
        # Compare the key to search to the keys in the nodes
        # if you find it, return the value
        # if not, return None

    def resize(self):
        # Create a blank new array with double the size of the old array
        self.new_capacity = (self.capacity * 2)
        new_arr = [None] * self.new_capacity
        self.capacity = self.new_capacity
        self.hash_list = new_arr

        for node in self.hash_list:
            curr_node = node
            while curr_node is not None:
                self.put(node.key, node.value)
                curr_node = curr_node.next

        # We have to rehash every single item because the hash function has changed
        # go through each slot in the array
        # go through each item in each linked list in the array
        # rehash the key in each item and store in new array
        # make new array the new storage


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.get("line_2")
    # ht.get("line_1")
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
