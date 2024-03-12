"""
Prefix sum
[1, 2, -3, 3, 1]
[0, 1, 3, 0, 3, 4]

[1, 2, 3, -3, 4]
[0, 1, 3, 6, 3, 7]

[1, 2, 3, -3, -2]
[0, 1, 3, 6, 3, 1]

Same prefix sum appear if zero sum happen
First iteration to the end to make prefix

When we encounter a prefix sum seen before, zero-sum consecutive sequence appears
  Hashmap saves only last occurrence of a prefix sum
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix_sum = 0
        sentinel_head = ListNode(prefix_sum)
        sentinel_head.next = head
        prefix_sum_to_node = {prefix_sum: sentinel_head}

        # Find last occurrence of each distinct prefix sum
        curr = sentinel_head.next
        while curr:
            prefix_sum += curr.val
            prefix_sum_to_node[prefix_sum] = curr
            curr = curr.next

        # Find first occurrence of prefix sum which exist in the hashmap
        prefix_sum = 0
        curr = sentinel_head
        while curr:
            prefix_sum += curr.val
            curr.next = prefix_sum_to_node[prefix_sum].next
            curr = curr.next

        return sentinel_head.next

    def removeZeroSumSublists1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix_sum = 0
        sentinel_head = ListNode(prefix_sum)
        sentinel_head.next = head
        prefix_sum_to_node = {prefix_sum: sentinel_head}

        curr = sentinel_head.next

        while curr:

            prefix_sum += curr.val

            print(f"prefix_sum: {prefix_sum}, curr.val: {curr.val}")

            if prefix_sum in prefix_sum_to_node:
                prefix_sum_to_node[prefix_sum].next = curr.next

            prefix_sum_to_node[prefix_sum] = curr

            curr = curr.next

        return sentinel_head.next

