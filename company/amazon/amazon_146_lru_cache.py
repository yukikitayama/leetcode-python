"""
Using linked list is better to remove from arbitrary positions than array

Hashmap, k: key, v: ListNode object, for O(1)

Sentinel nodes for convenience and for empty case
"""


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        prev_end = self.tail.prev

        prev_end.next = node
        node.prev = prev_end

        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)
        node = ListNode(key=key, val=value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            delete_node = self.head.next
            self.remove(delete_node)
            del self.dic[delete_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)