from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Edge
        if not head:
            return head

        original_to_copy = {}
        copy_node = Node(head.val)
        original_to_copy[head] = copy_node
        curr = head

        while curr:

            # Next
            if curr.next and curr.next not in original_to_copy:
                copy_next = Node(curr.next.val)
                original_to_copy[curr.next] = copy_next
                copy_node.next = copy_next
            elif curr.next and curr.next in original_to_copy:
                copy_node.next = original_to_copy[curr.next]

            # Random
            if curr.random and curr.random not in original_to_copy:
                copy_random = Node(curr.random.val)
                original_to_copy[curr.random] = copy_random
                copy_node.random = copy_random
            elif curr.random and curr.random in original_to_copy:
                copy_node.random = original_to_copy[curr.random]

            curr = curr.next
            copy_node = copy_node.next

        return original_to_copy[head]

    def copyRandomList1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_copy = {}

        prev = None
        curr = head
        copy_head = None

        while curr:

            # Copy
            copy_node = Node(x=curr.val)

            if not copy_head:
                copy_head = copy_node

            # Save copy
            original_to_copy[curr] = copy_node

            # Connect next
            if prev:
                original_to_copy[prev].next = copy_node

            # Connect random
            if curr.random in original_to_copy:
                copy_node.random = original_to_copy[curr.random]
            else:
                original_random = curr.random
                if original_random:
                    copy_random = Node(x=original_random.val)
                    original_to_copy[original_random] = copy_random
                    copy_node.random = copy_random

            # Iterate to next
            prev = curr
            curr = curr.next

        return copy_head
