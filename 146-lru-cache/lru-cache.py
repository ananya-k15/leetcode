class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # hashmap to store all key-value pairs
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        l, r = node.prev, node.next
        l.next = r
        r.prev = l

    def insert(self, node: Node) -> None:
        # use the right pointer to insert b/w most recently used and right pointer
        l, r = self.right.prev, self.right
        l.next = r.prev = node
        node.prev = l
        node.next = r

    def get(self, key: int) -> int:
        if key in self.cache:
            # Update doubly linked list since this is now the most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            # remove the LRU, i.e., node next to the left pointer
            LRU = self.left.next
            del self.cache[LRU.key]
            self.remove(LRU)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)