"""
- fast, slow, slow prev pointers
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next:
            return None

        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head


class Solution1:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next:
            return None

        n = 1
        curr = head

        while curr.next:
            curr = curr.next
            n += 1

        mid = n // 2

        # print(f'n: {n}, mid: {mid}')

        curr = head

        for _ in range(mid - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head


if __name__ == '__main__':
    head = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(Solution().deleteMiddle(head))
