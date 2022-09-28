"""
- Iterate to the end to know the length
- In next iteration, iterate by times of total length - given n
"""



from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head
        first = sentinel
        second = sentinel

        for i in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return sentinel.next


class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head
        length = 0

        curr = head

        while curr:
            length += 1
            curr = curr.next

        length -= n
        curr = sentinel
        while length > 0:
            length -= 1
            curr = curr.next

        curr.next = curr.next.next

        return sentinel.next


if __name__ == '__main__':
    pass
