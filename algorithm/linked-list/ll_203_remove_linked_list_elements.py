from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            # 1 -> 2 -> 3, when val: 2
            # prev: 1, curr: 2, curr.next: 3
            # -> prev: 1, prev.next: 3, curr: 3
            # so -> 1 -> 3, where prev: 1, curr: 3
            if curr.val == val:
                prev.next = curr.next
            # 1 -> 2 -> 3, when val: 3
            # prev: 1, curr: 2, curr.next: 3
            # -> prev: 2, curr: 3
            else:
                prev = curr
            curr = curr.next

        return dummy.next



