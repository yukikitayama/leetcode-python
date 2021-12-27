from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        curr_head = head
        while head.next:
            p = head.next
            head.next = p.next
            p.next = curr_head
            curr_head = p
        return curr_head
