from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel_head = ListNode()
        carry = 0
        curr = sentinel_head

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sum_ = num1 + num2 + carry
            carry, curr_digit = divmod(sum_, 10)

            node = ListNode(curr_digit)
            curr.next = node
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return sentinel_head.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def get_num(node):
            curr = node
            multiplier = 1
            ans = 0

            while curr:
                ans += curr.val * multiplier
                multiplier *= 10
                curr = curr.next

            return ans

        sum_ = get_num(l1) + get_num(l2)
        str_sum = str(sum_)

        sentinel_head = ListNode()
        curr = sentinel_head

        for i in range(len(str_sum) - 1, -1, -1):
            node = ListNode(int(str_sum[i]))
            curr.next = node
            curr = curr.next

        return sentinel_head.next