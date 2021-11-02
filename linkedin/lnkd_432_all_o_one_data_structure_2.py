"""
"""


from typing import Optional
import collections


class Node:
    def __init__(self):
        self.key_set = set()
        self.prev = None
        self.nxt = None

    def add_key(self, key):
        self.key_set.add(key)

    def remove_key(self, key):
        self.key_set.remove(key)

    # This is used in getMaxKey() and getMinKey(), because
    # these requires to returns on of the keys with the max or min count
    # There could be multiple keys with the same count, and we don't care which
    # so this randomly returns one of the keys
    def get_any_key(self) -> Optional[str]:
        if self.key_set:
            # Set pop() method removes a random item
            result = self.key_set.pop()
            self.add_key(result)
            return result
        else:
            return None

    # Count the number of keys
    def count(self):
        return len(self.key_set)

    def is_empty(self):
        return len(self.key_set) == 0


class DoubleLinkedList:
    def __init__(self):
        self.head_node = Node()
        self.tail_node = Node()

        self.head_node.nxt = self.tail_node
        self.tail_node.prev = self.head_node

    def insert_after(self, x):
        """
        x -> node -> temp
        """
        node = Node()
        # Is x guaranteed to be an object of Node?
        temp = x.nxt

        # x.nxt, node.prev = node, x
        # Below works
        x.nxt = node
        node.prev = x

        # node.nxt, temp.prev = temp, node
        # Below works
        node.nxt = temp
        temp.prev = node

        return node

    def insert_before(self, x):
        return self.insert_after(x.prev)

    def remove(self, x):
        """
        Before remove(), prev_node -> x -> x.nxt
        After remove(), prev_node -> x.nxt.prev
        """
        prev_node = x.prev

        prev_node.nxt, x.nxt.prev = x.nxt, prev_node

        return

    def get_head(self):
        return self.head_node.nxt

    def get_tail(self):
        return self.tail_node.prev

    def get_sentinel_head(self):
        return self.head_node

    def get_sentinel_tail(self):
        return self.tail_node


class AllOne:

    def __init__(self):
        self.dll = DoubleLinkedList()
        # key_counter is a hashmap with key each key word and value the count of the key
        # We need key_counter to decide what operations are needed in doubly linked list with the key
        self.key_counter = collections.defaultdict(int)
        # node_freq is also a hashmap with key the count of keys
        # and value the reference pointing at nodes in doubly linked list
        self.node_freq = {0: self.dll.get_sentinel_head()}

    # This remove the key from the key set in the Node
    # If this key was the only key in the node,
    # this entirely removes the node from doubly linked list
    def _rmv_key_pf_node(self, pf, key):
        node = self.node_freq[pf]
        node.remove_key(key)

        if node.is_empty():
            self.dll.remove(node)
            # node_freq is Python dictionary, so pop() removes the key
            self.node_freq.pop(pf)
        return

    def inc(self, key: str) -> None:
        self.key_counter[key] += 1
        cf = self.key_counter[key]
        pf = self.key_counter[key] - 1

        # If current frequency is not in the hashmap of count to node reference,
        # we need to make a new key with cf, and the value is
        if cf not in self.node_freq:
            # self.node_freq[pf] gives us the reference to the node in doubly linked list with node.count() == pf
            # and insert a new node after the node with node.count() == pf
            # e.g. dll: 0 -> 1, insert_after(), dll: 0 -> 1 -> 2
            # and insert_after() gives us the next node
            # here it's empty node
            self.node_freq[cf] = self.dll.insert_after(self.node_freq[pf])

        # If the above if was True, newly add a key
        # If the above if was False, the node already existed, so just add the current key to the set in the node
        self.node_freq[cf].add_key(key)

        # If pf is 0, it newly makes a new node in doubly linked list
        # But if pf is more than 0, this key already existed in somewhere in doubly linked list
        # Now we wanna increment this key, so it needs to remove the key from the previous count node in DLL
        # in _rmv_key_pf_node, it either just remove a key from the set and leave the node,
        # or removes a key and remove the node entirely
        if pf > 0:
            self._rmv_key_pf_node(pf, key)

    def dec(self, key: str) -> None:
        if key in self.key_counter:
            self.key_counter[key] -= 1

            cf = self.key_counter[key]
            pf = self.key_counter[key] + 1

            # If the current count of the key after dec is 0
            if self.key_counter[key] == 0:
                self.key_counter.pop(key)

            # If the current count of the key after dec is not 0,
            # we need to update doubly linked list
            if cf != 0:
                # If current count does not exist in doubly linked list,
                # we need to make a new node
                if cf not in self.node_freq:
                    # First get the previous count node in doubly linked list
                    # then insert a new node before the previous node
                    # lastly save the reference to the new node in node_freq hashmap
                    self.node_freq[cf] = self.dll.insert_before(self.node_freq[pf])

                # If the current count exists in the hashmap key,
                # Just add the key to the decremented number node in the doubly linked list
                self.node_freq[cf].add_key(key)

            # We decremented it, so remove the key from the key set,
            # or entirely remove the node
            self._rmv_key_pf_node(pf, key)

    # Doubly linked list is ascending order
    # So getMaxKey() takes O(1) by seeing the tail of the doubly linked list
    def getMaxKey(self) -> str:
        return self.dll.get_tail().get_any_key() if self.dll.get_tail().count() else ''

    # Doubly linked list is ascending, so seeing head is the minimum
    # so getMinKey() also takes O(1)
    def getMinKey(self) -> str:
        # Why is get_tail() in if, not get_head()?
        # LeetCode console works even if replacing get_tail() with get_head()
        return self.dll.get_head().get_any_key() if self.dll.get_tail().count() else ''


obj = AllOne()
print('Made AllOne object')
print(obj.node_freq[0].key_set)
print()
obj.inc('hello')
print(f'Added hello')
print(obj.key_counter)
print(obj.node_freq)
print(obj.node_freq[0].key_set)
print(obj.node_freq[1].key_set)
print()
obj.inc('hello')
print('Added hello again')
print(obj.key_counter)
print(obj.node_freq)
print()
obj.inc('hello')
print(f'Added third hello')
print(obj.key_counter)
print(obj.node_freq)
print()
obj.inc('leet')
print(f'Added leet')
print(obj.key_counter)
print(obj.node_freq)
print()
# print(obj.getMaxKey())
# print(obj.getMinKey())
# obj.inc('leet')
# print(obj.getMaxKey())
# print(obj.getMinKey())


