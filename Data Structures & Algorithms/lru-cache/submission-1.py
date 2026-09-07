class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        # Sentinel nodes to avoid edge cases
        self.left = Node(0, 0)   # LRU (least recently used)
        self.right = Node(0, 0)  # MRU (most recently used)
        self.left.next = self.right
        self.right.prev = self.left

    # Remove node from the linked list
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Insert node at the right (MRU position)
    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move to MRU position
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # If key exists, remove old node
        if key in self.cache:
            self._remove(self.cache[key])

        # Create new node and add to cache
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        # If we exceeded capacity, evict LRU
        if len(self.cache) > self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]