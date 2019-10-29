# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining
        Fill this in.
        '''
        new_node = LinkedPair(key, value)
        hm_key = self._hash_mod(key)
        head = self.storage[hm_key]
        node = head
        # if there is nothing in hash table at that key populate it with new_node
        if not head:
            self.storage[hm_key] = new_node
        else:
            # if first node has same key override value
            if head.key == key:
                new_node.next = head.next
                self.storage[hm_key] = new_node
            else:
                while node:
                    # if next node is None populate with new_node
                    if not node.next:
                        node.next = new_node
                        break
                    # if next node key is equal override with new_node
                    elif node.next.key == key:
                        new_node.next = node.next.next
                        node.next = new_node
                        break
                    else:
                        node = node.next


    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        hm_key = self._hash_mod(key)
        if self.storage[hm_key]:
            node = self.storage[hm_key]
            count = 0
            while node:
                # if the key is the first node change to pointer too look at node.next
                if count == 0:
                    count += 1
                    # print('count is 0')
                    if node.key == key:
                        self.storage[hm_key] = node.next
                        break
                # if the key is in the linked list somewhere find the matching key and make the previous node point
                # to node.next, garbage collection will take care of the node
                elif count > 0:
                    # print('count not 0')
                    if node.next:
                        if node.next.key == key:
                            node.next = node.next.next
                            break
                        else:
                            node = node.next
                    else:
                        return 'Key not found'
            return 
                                  


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        hm_key = self._hash_mod(key)
        if self.storage[hm_key]:
            node = self.storage[hm_key]
            while node:
                if node.key == key:
                    return node.value
                else:
                    node = node.next
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        self.capacity = self.capacity * 2
        new_ht = HashTable(self.capacity)
        for node in self.storage:
            while node:
                hm_key = self._hash_mod(node.key)
                new_ht.insert(node.key, node.value)
                node = node.next
        self.storage = new_ht.storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
