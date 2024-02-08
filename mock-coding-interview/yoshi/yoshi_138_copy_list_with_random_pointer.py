import collections
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

        original_to_copy = collections.defaultdict(Node)

        def get_copy_node(original_node):
            if original_node:
                if original_node in original_to_copy:
                    return original_to_copy[original_node]
                else:
                    copy_node = Node(original_node.val, None, None)
                    original_to_copy[original_node] = copy_node
                    return copy_node

        copy_head = Node(head.val, None, None)
        original_to_copy[head] = copy_head

        original_curr = head
        copy_curr = copy_head

        while original_curr:

            copy_curr.next = get_copy_node(original_curr.next)
            copy_curr.random = get_copy_node(original_curr.random)

            original_curr = original_curr.next
            copy_curr = copy_curr.next

        return copy_head