"""
Linked list to store key value in LRU order
  prev
  next
    can remove and connect
Get
  remove key from the list
  append key to the tail of the list
Put
  remove key from the list
  append key to the tail of the list
Hashmap
  k: key
  v: Node
"""


class ListNode:
    def __init__(self, key=-1, val=-1, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.sentinel_head = ListNode()
        self.sentinel_tail = ListNode()
        self.sentinel_head.next = self.sentinel_tail
        self.sentinel_tail.prev = self.sentinel_head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def append(self, node):
        real_tail = self.sentinel_tail.prev

        # Real tail
        real_tail.next = node
        node.prev = real_tail

        # Sentinel tail
        node.next = self.sentinel_tail
        self.sentinel_tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]

        # Remove
        self.remove(node)

        # Append
        self.append(node)

        # No need to update hashmap because the same node only changed in linked list position
        # but nothing change in hashmap

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            old_node = self.key_to_node[key]
            self.remove(old_node)

        new_node = ListNode(key=key, val=value)
        self.append(new_node)
        # Need to update hashmap because put needs to work for both new and existing
        self.key_to_node[key] = new_node

        # Remove oldest
        if len(self.key_to_node) > self.capacity:
            real_head = self.sentinel_head.next
            self.remove(real_head)
            # In other place, we don't delete a key from hashmap when self.remove
            # becuase it was actually not removing it but it was changing order
            # But here we are actually removing the head from the linked list
            # So removing from linked list is removing from hashmap too
            del self.key_to_node[real_head.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)