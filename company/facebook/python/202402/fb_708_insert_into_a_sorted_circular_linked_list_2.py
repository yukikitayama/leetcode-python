"""
curr from head
while loop
    if insertVale is between curr and curr next,
      insert
if curr is head, one circuled
  Circuled back, but hasn't inserted
    [1, 2, 3]
      <- 4, prev next is 4, 4 next is head
    [2, 3, 4]
      <- 1, prev next is 1, 1 next is head
    treatment is the same

Ans
  Case 1: min < insertVal < max
    new node inserted in the middle
  Case 2: insertVal < min or max < insertVal
    new node inserted after the tail
      tail is when prev > curr. Tail (prev) has max
      When prev is tail
        when insertVal < min, insertVal <= curr
        when insertVal > max, insertVal >= prev
  Case 3: Uniform values
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        if not head:
            node = Node(val=insertVal)
            node.next = node
            return node

        prev = head
        curr = head.next
        to_insert = False

        while True:

            # Case 1
            if prev.val <= insertVal <= curr.val:
                prev.next = Node(insertVal, curr)
                return head

            # When prev is tail
            elif prev.val > curr.val:
                # If case 2
                if prev.val <= insertVal or insertVal <= curr.val:
                    prev.next = Node(insertVal, curr)
                    return head

            prev = curr
            curr = curr.next

            # One circule finished
            # Preparation for case 3
            if prev == head:
                break

        # Case 3
        node = Node(val=insertVal)
        prev.next = node
        node.next = curr

        return head
