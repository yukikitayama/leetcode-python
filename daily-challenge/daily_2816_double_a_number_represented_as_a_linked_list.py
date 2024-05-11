"""
10000
integer overflow

Collect values into list
iterate the list from back to front
  double current number, add carry
  compute carry
  append current result to another array
Iterate the second array from left to right to make linked list
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse_linked_list(node):
            prev = None
            curr = node
            while curr:
                curr_next = curr.next
                curr.next = prev
                prev, curr = curr, curr_next

            return prev

        # Reverse given list to get least significant bit
        head = reverse_linked_list(head)
        curr = head
        # curr will be eventually none, but if carry, we need to connect carry to final prev
        prev = None
        carry = 0
        while curr:
            new_val = curr.val * 2 + carry
            carry, new_val = divmod(new_val, 10)
            curr.val = new_val
            prev = curr
            curr = curr.next
        if carry:
            prev.next = ListNode(carry)

        return reverse_linked_list(head)

    def doubleIt1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        # print(vals)

        carry = 0
        double = []
        for i in range(len(vals) - 1, -1, -1):
            d = vals[i] * 2 + carry
            carry, curr_digit = divmod(d, 10)
            double.append(curr_digit)
        if carry:
            double.append(carry)

        # print(double)

        sentinel_head = ListNode()
        curr = sentinel_head
        for i in range(len(double) - 1, -1, -1):
            node = ListNode(double[i])
            curr.next = node
            curr = curr.next

        return sentinel_head.next