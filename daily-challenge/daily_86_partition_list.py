from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        sentinel_before = ListNode()
        sentinel_after = ListNode()

        curr_before = sentinel_before
        curr_after = sentinel_after

        while head:

            if head.val < x:
                curr_before.next = head
                curr_before = curr_before.next

            else:
                curr_after.next = head
                curr_after = curr_after.next

            head = head.next

        curr_before.next = sentinel_after.next

        # End of after could have next pointer, but the answer needs to be None
        curr_after.next = None

        return sentinel_before.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    x = 3
    ans = Solution().partition(head, x)
    while ans:
        print(ans.val)
        ans = ans.next

