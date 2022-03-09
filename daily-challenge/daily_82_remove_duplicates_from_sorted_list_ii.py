"""
- If current val is the same as the previous val,
  2 previous node.next is current node.next
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        sentinel = ListNode(0, head)

        predecessor = sentinel

        while head:

            # If duplicate
            if head.next and head.val == head.next.val:

                # Move current node until it finds non-duplicate
                # At the end of while loop, curr is the last node of all duplicates
                while head.next and head.val == head.next.val:
                    head = head.next

                # Skip all the duplicates by connecting predecessor next
                # to non-duplicate
                predecessor.next = head.next

            else:
                predecessor = predecessor.next

            # Move current
            head = head.next

        return sentinel.next
