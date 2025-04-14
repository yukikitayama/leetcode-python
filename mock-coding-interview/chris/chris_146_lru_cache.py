"""
[(1, 1), (2, 2)]
put(1, 3)
[(1, 3), (2, 2)]
[(2, 2), (1, 3)]
put affects "used"

Naive
  queue
    recency
    front: least recent, back: most recent
    store key
  hashmap
    k: key, v: value
  update_order
    search the key in queue, and if exist, pop it and move it to back of the queue
  put
  get
T: O(capacity) for get and put
S: O(capacity)

Linked list
  prev
  next
"""


class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.sentinel_head = ListNode(-1, -1)
        self.sentinel_tail = ListNode(-1, -1)
        self.sentinel_head.next = self.sentinel_tail
        self.sentinel_tail.prev = self.sentinel_head
        self.key_to_node = {}

    def get(self, key: int) -> int:

        if key in self.key_to_node:
            val = self.key_to_node[key].val

            # Update order
            self.update_order(key)

            return val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.key_to_node[key].val = value
            # Update order
            self.update_order(key)
        else:
            node = ListNode(key, value)
            self.key_to_node[key] = node
            # Add to Linked List
            real_tail = self.sentinel_tail.prev
            real_tail.next = node
            node.prev = real_tail
            node.next = self.sentinel_tail
            self.sentinel_tail.prev = node

        if len(self.key_to_node) > self.capacity:
            # Evict oldest
            old_node = self.sentinel_head.next
            self.sentinel_head.next = old_node.next
            old_node.next.prev = self.sentinel_head
            del self.key_to_node[old_node.key]

    def update_order(self, key):
        node = self.key_to_node[key]

        # Remove
        node.prev.next, node.next.prev = node.next, node.prev

        # Append to right
        real_tail = self.sentinel_tail.prev
        real_tail.next = node
        node.prev = real_tail
        node.next = self.sentinel_tail
        self.sentinel_tail.prev = node
        # Connections going to right
        """
            real_end    <--->    dummy_tail
            real_end  -->  node  --> dummy_tail
        """
        # Connections going to left

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)