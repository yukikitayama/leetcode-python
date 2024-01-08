"""
2 passes
"""

from typing import Optional
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr_num = 0

        curr_node = head

        while curr_node:

            curr_num = curr_num * 10 + curr_node.val
            curr_node = curr_node.next

        curr_num *= 2

        digits = collections.deque()
        # Edge case
        if curr_num == 0:
            digits.append(curr_num)
        else:
            while curr_num:
                digits.appendleft(curr_num % 10)
                curr_num //= 10

        # print(curr_num, digits)

        dummy_head = ListNode()
        curr_dummy_node = dummy_head

        for num in digits:

            curr_dummy_node.next = ListNode(num)
            curr_dummy_node = curr_dummy_node.next

        return dummy_head.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(8)
    head.next.next = ListNode(9)
    # 378

    head = ListNode(9)
    head.next = ListNode(9)
    head.next.next = ListNode(9)
    # 1988

    head = ListNode(0)

    ans = Solution().doubleIt(head)
    while ans:
        print(ans.val)
        ans = ans.next
