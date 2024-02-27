"""
get
  update LRU priority
put
  puuted key has highest priority
  pop the lowest priority key from hashmap

Naive
  hashmap to store k and v
  queue to store recency
    heap
  get updates queue as well as return val
  put updates hashmap and pop hashmap and pop queue if exceeding size

Ans
  Linked list can remove from any positions in constant time
  Hashmap
    k: key
    v: pointer to ListNode object
      value is stored in the ListNode object
"""

import collections


class ListNode:
    def __init__(self, key=-1, val=-1, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.key_to_node = collections.defaultdict(ListNode)
        self.capacity = capacity

        self.sentinel_head = ListNode()
        self.sentinel_tail = ListNode()
        self.sentinel_head.next = self.sentinel_tail
        self.sentinel_tail.prev = self.sentinel_head

    def append(self, node):
        real_tail = self.sentinel_tail.prev

        real_tail.next = node
        node.prev = real_tail

        node.next = self.sentinel_tail
        self.sentinel_tail.prev = node

    def remove(self, node):
        prev = node.prev
        next_ = node.next
        prev.next = next_
        next_.prev = prev

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        else:
            node = self.key_to_node[key]
            # Update linked list
            self.remove(node)
            self.append(node)
            val = node.val
            return val

    def put(self, key: int, value: int) -> None:
        # Need to update linked list, so first remove it
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.remove(node)

        # Add to hashmap
        node = ListNode(key=key, val=value)
        self.key_to_node[key] = node

        # Add to linked list
        self.append(node)

        # If exceeding capacity, remove oldest
        if len(self.key_to_node) > self.capacity:
            real_head = self.sentinel_head.next
            self.remove(real_head)
            real_head_key = real_head.key
            del self.key_to_node[real_head_key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)