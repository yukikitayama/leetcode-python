"""
if curr next is target
  curr.next = curr.next.next

  curr = curr.next

If two pointers
  prev, curr
    if curr is target
      prev.next = curr.next
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel_head = ListNode(-1)
        sentinel_head.next = head

        curr = sentinel_head

        while curr:

            while curr.next and curr.next.val == val:
                curr.next = curr.next.next

            curr = curr.next

        return sentinel_head.next
