"""
sentinel head
curr_sum
while current node is not none
  if current node value isn't zero
    increment curr sum by current node value
  if current node value is 0
    if curr sum isn't 0
      create new node
      append to answer linked list
      reset curr sum to 0
  update current node with next node
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """S: O(1)"""
        modified_node = head.next
        summing_node = modified_node

        while summing_node:

            curr_sum = 0

            while summing_node.val != 0:
                curr_sum += summing_node.val
                summing_node = summing_node.next

            modified_node.val = curr_sum

            summing_node = summing_node.next
            modified_node.next = summing_node
            modified_node = modified_node.next

        return head.next

    def mergeNodes1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """S: O(N)"""
        sentinel_head = ListNode()
        curr_sum = 0
        curr_node = head
        curr_ans = sentinel_head
        while curr_node:

            if curr_node.val != 0:
                curr_sum += curr_node.val

            elif curr_node.val == 0:
                if curr_sum != 0:
                    node = ListNode(curr_sum)
                    curr_ans.next = node
                    curr_ans = curr_ans.next
                    curr_sum = 0

            curr_node = curr_node.next

        return sentinel_head.next
