from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sentinel = ListNode()
        carry = 0
        curr_node = sentinel

        while l1 or l2:

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum_ = l1_val + l2_val + carry
            carry = sum_ // 10
            curr_digit = sum_ % 10
            # print(f'l1_val: {l1_val}, l2_val: {l2_val}, sum_: {sum_}, carry: {carry}, curr_digit: {curr_digit}')
            curr_node.next = ListNode(val=curr_digit)
            curr_node = curr_node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            curr_node.next = ListNode(carry)

        return sentinel.next


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    ans = Solution().addTwoNumbers(l1, l2)
    while ans:
        print(ans.val)
        ans = ans.next
