"""
- Make both of two pointer travel the same distance
  - By letting them experience both linked list
"""


from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p_a = headA
        p_b = headB

        while p_a != p_b:
            p_a = headB if not p_a else p_a.next
            p_b = headA if not p_b else p_b.next

        # Return a ListNode object or None
        return p_a
