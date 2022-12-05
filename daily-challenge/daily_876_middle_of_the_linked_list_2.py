from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head
        slow = head

        # print(f'fast.val: {fast.val}, slow.val: {slow.val}')

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # print(f'fast.val: {fast.val if fast else None}, slow.val: {slow.val}')

        return slow


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    print(Solution().middleNode(head).val)
