from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(val=0)
        tenth = 0
        answer_head = answer

        while l1 is not None or l2 is not None:

            l1_value = l1.val if l1 is not None else 0
            l2_value = l2.val if l2 is not None else 0
            summed = l1_value + l2_value + tenth
            tenth = summed // 10
            first = summed % 10
            answer.next = ListNode(val=first)
            answer = answer.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if tenth > 0:
            answer.next = ListNode(tenth)

        return answer_head.next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
answer = Solution().addTwoNumbers(l1, l2)
print(answer.val)
print(answer.next.val)
print(answer.next.next.val)

