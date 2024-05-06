"""
Stack
  if current value is bigger than stack top
    keep popping stack top
  otherwise
    append current value
Newly create linked list with the stack

T: O(N)
S: O(N)

S: O(1) by removing stack?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse_linked_list(head):
            prev = None
            curr = head

            while curr:
                next_ = curr.next
                curr.next = prev
                prev = curr
                curr = next_

            return prev

        # Reverse linked list to be ready for making increasing linked list
        head = reverse_linked_list(head)

        # Remove decreasing element
        curr = head
        max_so_far = 0
        # We need prev because we will delete current node
        prev = None

        while curr:

            if curr.val >= max_so_far:
                max_so_far = curr.val
                prev = curr
                curr = curr.next
            else:
                # [1, 2, 3] -> [1, 3]
                prev.next = curr.next
                curr = curr.next

        # Reverse again the linked list to be decreasing original order
        head = reverse_linked_list(head)

        return head

    def removeNodes1(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = []
        curr = head
        while curr:

            while stack and stack[-1] < curr.val:
                stack.pop()

            stack.append(curr.val)

            curr = curr.next

        # print(stack)

        sentinel_head = ListNode()
        curr = sentinel_head
        stack.reverse()

        while stack:
            val = stack.pop()
            node = ListNode(val)
            curr.next = node
            curr = node

        return sentinel_head.next
