"""
- Doubly linked list
- Each node contains a set
  - The set contains keys with the same count
- Node 0 is the node for dummy keys with 0 count
- Node 1 is the node for keys with 1 count
  - getMinKey() get a random key from Node 1
  - getMaxKey() get a random key from the max Node
"""


from typing import Optional
import collections


class Node:
    def __init__(self):
        self.key_set = set()
        self.prev = None
        self.next = None

    def add_key(self, key):
        self.key_set.add(key)

    def remove_key(self, key):
        self.key_set.remove(key)

    def get_any_key(self):
        if self.key_set:
            result = self.key_set.pop()
            self.key_set.add(result)
            return result
        else:
            return None

    def count(self):
        return len(self.key_set)

    def is_empty(self):
        return len(self.key_set) == 0


class DoublyLinkedList:
    def __init__(self):
        self.sentinel_head = Node()
        self.sentinel_tail = Node()
        self.sentinel_head.next = self.sentinel_tail
        self.sentinel_tail.prev = self.sentinel_head

    def insert_after(self, x):
        """
        x -> temp, but insert something after x, so
        x -> node -> temp
        """
        node = Node()
        temp = x.next
        x.next = node
        node.prev = x
        node.next = temp
        temp.prev = node
        return node

    def insert_before(self, x):
        """
        Insert something before x
        y -> x, so x.prev points at y, so inserting after y can insert before x
        y -> node -> x
        """
        return self.insert_after(x.prev)

    def remove(self, x):
        prev_node = x.prev
        prev_node.next, x.next.prev = x.next, prev_node

    def get_head(self):
        return self.sentinel_head.next

    def get_tail(self):
        return self.sentinel_tail.prev

    def get_sentinel_head(self):
        return self.sentinel_head

    def get_sentinel_tail(self):
        return self.sentinel_tail


class AllOne:
    def __init__(self):
        self.dll = DoublyLinkedList()
        self.key_counter = collections.defaultdict(int)
        self.node_freq = {0: self.dll.get_sentinel_head()}

    def remove_key_previous_freq_node(self, pf, key):
        node = self.node_freq[pf]
        node.remove_key(key)
        if node.is_empty():
            self.dll.remove(node)
            self.node_freq.pop(pf)

    def inc(self, key: str) -> None:
        self.key_counter[key] += 1
        cf = self.key_counter[key]
        pf = self.key_counter[key] - 1

        if cf not in self.node_freq:
            # Insert cf node after pf node. # It's not getting data from pf node
            self.node_freq[cf] = self.dll.insert_after(self.node_freq[pf])
        self.node_freq[cf].add_key(key)
        # If pf is more than 0, this key already existed in DLL, so it needs to remove it
        if pf > 0:
            self.remove_key_previous_freq_node(pf, key)

    def dec(self, key: str) -> None:
        if key in self.key_counter:
            self.key_counter[key] -= 1
            cf = self.key_counter[key]
            pf = self.key_counter[key] + 1

            if self.key_counter[key] == 0:
                self.key_counter.pop(key)

            if cf != 0:
                if cf not in self.node_freq:
                    self.node_freq[cf] = self.dll.insert_before(self.node_freq[pf])
                self.node_freq[cf].add_key(key)

            self.remove_key_previous_freq_node(pf, key)

    def getMaxKey(self) -> str:
        return self.dll.get_tail().get_any_key() if self.dll.get_tail().count() else ''

    def getMinKey(self) -> str:
        return self.dll.get_head().get_any_key() if self.dll.get_head().count() else ''



