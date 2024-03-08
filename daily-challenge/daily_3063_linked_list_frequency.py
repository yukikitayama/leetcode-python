"""
hashmap
  k: node val
  v: freq

iterate linked list
  update hashmap

sentinel head
iterate hashmap
  create current node from hashmap
  connect prev next
  current is prev
return next of sentinel head
"""

from typing import Optional
import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_to_node = collections.defaultdict(ListNode)

        sentinel_head = ListNode()

        curr = head

        while curr:

            if curr.val in num_to_node:
                node = num_to_node[curr.val]
                node.val += 1

            else:
                node = ListNode(val=1)
                num_to_node[curr.val] = node
                real_head = sentinel_head.next
                sentinel_head.next = node
                node.next = real_head

            curr = curr.next

        return sentinel_head.next

    def frequenciesOfElements1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        val_to_freq = collections.defaultdict(int)

        curr = head

        while curr:
            val_to_freq[curr.val] += 1
            curr = curr.next

        sentinel_head = ListNode()
        curr = sentinel_head
        for k, v in val_to_freq.items():
            node = ListNode(v)
            curr.next = node
            curr = curr.next

        return sentinel_head.next