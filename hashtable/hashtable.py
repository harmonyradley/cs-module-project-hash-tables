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

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        self.storage = [None] * capacity
        self.count = 0

    def djb2(self, key):
        hash = 5381
        for item in key:
            hash = (hash * 33) + ord(item)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """

        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.

        For a given key, store a value in the hash table"""
        # Store the value with the given key.
        index = self.hash_index(key)
        hash_entry = HashTableEntry(key, value)
        storage = self.storage[index]
        self.count += 1

        # Hash Collisions --> Linked List Chaining.
        if storage:
            self.storage[index] = hash_entry
            self.storage[index].next = storage
        else:
            self.storage[index] = hash_entry

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Remove the value stored through the key.
        if self.get(key):
            self.put(key, None)
            self.count -= 1
        else:
            print("The key twas not found")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # get the value stored with the key.
        index = self.hash_index(key)
        storage = self.storage[index]
        while storage:
            if storage.key == key:
                return storage.value
            storage = storage.next
        # key was not found.
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        load = self.get_load_factor()
        if load > 0.7:
            # Make a new array of double the size
            new_table = [None] * (new_capacity)
            old_table = self.storage
            self.storage = new_table
            self.capacity = new_capacity
            # Go through all the elements in the old hash table
            for element in old_table:
                current = element
                # we want to then put the element into the new_table
                while current is not None:
                    self.put(current.key, current.value)
                    current = current.next

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.count / self.capacity


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
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
