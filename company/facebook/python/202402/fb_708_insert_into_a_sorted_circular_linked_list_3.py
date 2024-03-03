# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

"""
Track prev and curr

Insert
  temp = prev.next
  prev.next = insert node
  insert node.next = temp

Insert location
  middle
    prev < insert < curr
  tail
    if insert node is smaller than min of given linked list
      prev is tail, curr is head, prev > insert, curr > insert
    if insert node is bigger than max of given linked list
      prev is tail, curr is head, prev < insert, curr < insert
  if still cannot find location
    linked list filled with unique values, and insert is the same number,
    after one cycle, prev == curr, insert at tail
      eg. [1, 1, 1] -> [1, 1, 1, 2]

Ans
  min <= insertVal <= max
    insert during iteration
  insertVal < min or max < insertVal
    insert when prev > curr
    insert after prev and before curr
  both can might happen during iteration
  Edge
    uniform values
    Insert after one cycle
"""

from typing import Optional


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # Edge
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        prev = head
        curr = prev.next

        while True:

            if prev.val <= insertVal <= curr.val:
                prev.next = Node(insertVal, curr)
                return head

            if prev.val > curr.val:
                if prev.val <= insertVal or insertVal <= curr.val:
                    prev.next = Node(insertVal, curr)
                    return head

            prev = curr
            curr = curr.next

            if prev == head:
                break

        prev.next = Node(insertVal, curr)
        return head

    def insert1(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # Edge
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        prev = head
        curr = prev.next
        insert_node = Node(val=insertVal)

        while prev:

            if prev.val <= insert_node.val <= curr.val:
                temp = prev.next
                prev.next = insert_node
                insert_node.next = temp
                break

            # Before one cycle, gap occurs
            if curr.val < prev.val:
                if insertVal < curr.val or prev.val < insertVal:
                    temp = prev.next
                    prev.next = insert_node
                    insert_node.next = temp
                    break

            if curr == head:
                print(f"curr: {curr.val}, prev: {prev.val}")
                temp = prev.next
                prev.next = insert_node
                insert_node.next = temp
                break

            prev = curr
            curr = curr.next

        return head
