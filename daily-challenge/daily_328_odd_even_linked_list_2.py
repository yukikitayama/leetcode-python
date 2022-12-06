from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        odd_tail = head
        even_head = head.next
        even_tail = head.next

        while even_tail and even_tail.next:

            # Connect next odd to current odd tail
            odd_tail.next = even_tail.next

            # Iterate to the next odd
            odd_tail = odd_tail.next

            # Get next even and connect it to the even tail
            even_tail.next = odd_tail.next

            # Iterate to the next even
            even_tail = even_tail.next

        # Connect odd tail to even head
        odd_tail.next = even_head

        return head


