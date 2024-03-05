"""
Hashmap
  k: position 1-based index
  val: node


Ans
  iterative approach
  change the direction as from right to left for the range to reverse
  let node before the range point to the rightmost node which has opposite direction
  let new tail node point the node at the right of the range as next node
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # Edge
        if not head:
            return None

        prev = None
        curr = head

        while left > 1:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1

        con = prev
        tail = curr

        while right:
            third = curr.next
            curr.next = prev
            prev = curr
            curr = third
            right -= 1

        if con:
            con.next = prev
        # When reverse starts from the first node
        else:
            head = prev

        tail.next = curr

        return head

    def reverseBetween1(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head:
            return head

        left_node = head
        right_node = head
        stop = False

        def recurse_and_reverse(right_node, left_counter, right_counter):
            nonlocal left_node, stop

            # Base case: Don't move right pointer further
            if right_counter == 1:
                return

            # Keep moving right pointer until right_counter is 1
            right_node = right_node.next

            if left_counter > 1:
                left_node = left_node.next

            # This recursion come back to here when right_counter becomes 1
            recurse_and_reverse(right_node, left_counter - 1, right_counter - 1)

            if left_node == right_node or right_node.next == left_node:
                stop = True

            if not stop:
                left_node.val, right_node.val = right_node.val, left_node.val

                left_node = left_node.next

        recurse_and_reverse(right_node, left, right)

        return head