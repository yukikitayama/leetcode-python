"""
Hashmap
  k: pointer to original node
  v: pointer to copied node

Get copied node by original node
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        original_to_copy = {}
        copy_head = Node(head.val)
        original_to_copy[head] = copy_head

        def get_copy_node(original_node):
            """original_node could be None"""
            if original_node:
                if original_node in original_to_copy:
                    return original_to_copy[original_node]
                else:
                    copy_node = Node(original_node.val)
                    original_to_copy[original_node] = copy_node
                    return copy_node
            else:
                return None

        curr = head

        while curr:
            copy_next = get_copy_node(curr.next)
            copy_random = get_copy_node(curr.random)

            original_to_copy[curr].next = copy_next
            original_to_copy[curr].random = copy_random

            curr = curr.next

        return copy_head

    def copyRandomList1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        original_to_copy = {}

        copy_head = Node(head.val)

        original_to_copy[head] = copy_head

        curr = head

        while curr:
            next_node = curr.next

            if next_node:
                if next_node in original_to_copy:
                    original_to_copy[curr].next = original_to_copy[next_node]
                else:
                    copy_next_node = Node(next_node.val)
                    original_to_copy[next_node] = copy_next_node
                    original_to_copy[curr].next = copy_next_node

            random_node = curr.random

            if random_node:
                if random_node in original_to_copy:
                    original_to_copy[curr].random = original_to_copy[random_node]
                else:
                    copy_random_node = Node(random_node.val)
                    original_to_copy[random_node] = copy_random_node
                    original_to_copy[curr].random = copy_random_node

            curr = curr.next

        return copy_head
