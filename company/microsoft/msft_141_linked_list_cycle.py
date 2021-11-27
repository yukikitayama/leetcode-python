"""
- Add current node to a set, and follow next
- if the current node is in a set, there's cycle
- If it reaches next is None, there's no cycle
- Time O(n), space O(n)
"""


from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False

        slow = head
        fast = head.next

        while fast != slow:

            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True

