"""
Linked list to store data
  key
  val
  prev
  next

Initialization
  set capacity
  set head
  set tail
  set hashmap
    k: key
    v: list node

Get
  if not in the hashmap, -1
  get current node
  remove current node from the linked list
  append it to tail

Put
  if key exist in hashmap
    remove the existing node

  create new node
  update hashmap
  append it to tail

  if key length of hashmap exceed capacity
    remove head
    remove the node from hashmap

Append
  get tail
  insert between prev and next

Remove
  connect
    node.prev.next and node.next.prev
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

    def append(self, node):
        real_tail = self.sentinel_tail.prev

        real_tail.next = node
        node.prev = real_tail

        node.next = self.sentinel_tail
        self.sentinel_tail.prev = node

    def remove(self, node):
        # prev_node = node.prev
        # next_node = node.next
        # prev_node.next = next_node
        # next_node.prev = prev_node

        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return - 1

        node = self.key_to_node[key]

        self.remove(node)
        self.append(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.remove(self.key_to_node[key])

        node = ListNode(key=key, val=value)
        self.key_to_node[key] = node
        self.append(node)

        if len(self.key_to_node.keys()) > self.capacity:
            real_head = self.sentinel_head.next
            self.remove(real_head)
            del self.key_to_node[real_head.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)