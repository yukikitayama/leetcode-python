"""
Algorithm
- left pointer moves by one
- right pointer moves by two
- when right pointer is None, return left pointer node
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # fast is None when linked list is even length
        # fast.next is None when linked list is odd length
        while fast and fast.next:

            # print(f'slow.val: {slow.val}, fast.val: {fast.val}')

            slow = slow.next
            fast = fast.next.next

        return slow


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
print(Solution().middleNode(head))

