from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head

        while curr:

            # Start from the beginning in every iteration
            prev = dummy

            # Position to insert is somewhere current value is smaller than prev.next.val
            # If prev.next is None, it's end of the linked list, so without comparison, we can insert current
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # It will update curr.next, but curr.next is needed for the next iteration
            next = curr.next

            # There are 3 nodes; prev: 1, prev.next: 3, curr: 2
            # prev -> curr -> prev.next => prev.next: curr, curr.next: previous prev.next
            curr.next = prev.next
            prev.next = curr

            # next is the head of unsorted list
            curr = next

        return dummy.next

