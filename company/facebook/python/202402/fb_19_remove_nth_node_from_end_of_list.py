"""
Iterate linked list to find n
Iterate from head again by n - k times

Case
  remove a node in the middle
    Connect prev next to curr next
  remove a node at the end
    Connect prev next to None
  remove a node at the start
    Connect dummy as prev next to curr next
    and return dummy as prev next

n is given, nth from the end
define m as length of linked list
when n == 1
  Remove the end node
when m - n > 0
  Remove middle
when m - n == 0
  Remove first node
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

    #     if not head:
    #         return head

    #     curr = head
    #     m = 0
    #     while curr:
    #         m += 1
    #         curr = curr.next

    #     print(f"m: {m}")

    #     dummy_head = ListNode()
    #     dummy_head.next = head
    #     prev = dummy_head
    #     curr = prev.next

    #     i = 0

    #     while i <= m:

    #         # Case: remove first
    #         if (m - n) == 0:
    #             if m == 1:
    #                 prev.next = None
    #             else:
    #                 prev.next = curr.next
    #             break

    #         # Case: remove middle, and remove last
    #         # prev: 3, curr: 4, i: 3, m - n: 3
    #         # Prev: 4, curr: 5, i: 4, m - n: 4
    #         elif i == (m - n):
    #             prev.next = curr.next
    #             break

    #         prev = curr
    #         curr = curr.next
    #         i += 1

    #     return dummy_head.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return head

        dummy_head = ListNode()
        dummy_head.next = head

        curr = dummy_head.next
        length = 0

        while curr:
            length += 1
            curr = curr.next

        print(f"length: {length}")

        # Remove (length - n + 1)th node
        # Find a node which is one step before the (length - n + 1)th node
        curr = dummy_head
        counter = 0
        while counter < (length - n):
            counter += 1
            curr = curr.next
        curr.next = curr.next.next

        # Why does this work for removing the last node?
        # Because it doesn't reach the last node

        return dummy_head.next
