class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"HashTableEntry: ({self.key}, Value : {self.value}) Next -> {self.next} "


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
Min_LF = .2
Max_LF = .7


class HashTable:

    def __init__(self, capacity):
        self.hash_list = [None] * capacity
        self.capacity = 8
        self.occupied_slots = 0

    # def __str__(self):
    #     return(f"HashTable: ({self.hash_list}, {self.occupied_slots}, {self.capacity})")

    def get_num_slots(self):
        # Return length of data-structure
        #
        return self.capacity

    def get_load_factor(self):
        # return load factor
        return self.occupied_slots / self.capacity

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
        curr_node = self.hash_list[self.hash_index(key)]
        # print("LOAD FACTOR: ", loadFactor)

        #  Check Load factor first
        if loadFactor >= Max_LF:
            self.resize(self.capacity * 2)

            index = self.hash_index(key)
            curr_node = self.get_node(key)
        if curr_node is None and self.hash_list[index] is not None:
            new_node = HashTableEntry(key, value)
            new_node.next = self.hash_list[index]
            self.add_node(new_node, index)

        else:
            self.add_node(HashTableEntry(key, value), index)

    def add_node(self, node, index):
        self.hash_list[index] = node
        self.occupied_slots += 1

    def delete(self, key):
        index = self.hash_index(key)
        node_head = self.hash_list[index]

        if node_head is None:
            print("key not found")

        else:
            node_head = self.del_node(key, node_head)
            self.hash_list[index] = node_head

    def del_node(self, key, node_head):
        if node_head == None:
            print("Not found")
            return None

        if key == node_head.key:
            next_node = node_head.next
            node_head = None
            self.occupied_slots -= 1
            return next_node

        node_head.next = self.del_node(key, node_head.next)
        return node_head

    def get(self, key):

        curr_node = self.get_node(key)
        return curr_node.value if curr_node is not None else None

    def get_node(self, key):
        index = self.hash_index(key)
        current_node = self.hash_list[index]

        while current_node is not None:
            if current_node.key == key:
                return current_node
            else:
                current_node = current_node.next

        return current_node

    def resize(self, new_capacity):
        # Create a blank new array with double the size of the old array
        old_capacity = self.hash_list
        self.__init__(new_capacity)
        self.capacity = new_capacity

        for node in old_capacity:
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
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.get("line_2")
    ht.get("line_1")
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    # ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
