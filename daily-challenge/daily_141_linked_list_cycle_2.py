"""
Collect node while iterating
Iterate terminates when current node is None and return False

S: O(1)
  two pointers
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast = head.next
        slow = head

        while fast:

            if fast == slow:
                return True

            if fast.next:
                fast = fast.next.next
            else:
                return False

            slow = slow.next

        return False

    def hasCycle1(self, head: Optional[ListNode]) -> bool:

        nodes = set()

        curr = head

        while curr:
            if curr in nodes:
                return True

            nodes.add(curr)

            curr = curr.next

        return False