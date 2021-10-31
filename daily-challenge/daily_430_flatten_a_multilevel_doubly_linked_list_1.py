"""
- recursion
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        pseudo_head = Node(None, None, head, None)

        self.flatten_dfs(pseudo_head, head)

        # flatten_dfs() connects head prev to pseudo but the answer doesn't need it
        pseudo_head.next.prev = None
        return pseudo_head.next

    # Preorder by root -> left -> right
    def flatten_dfs(self, prev, curr):

        # This will be returned at the end of child
        # and at the end of original linked list
        if not curr:
            return prev

        # Take care of current state first because it's preorder
        curr.prev = prev
        prev.next = curr

        # When curr does not have child, the below flatten_dfs just return the curr
        # so tail: curr, temp_next: curr.next
        # so at the end return, flatten_dfs(curr, curr.next)
        temp_next = curr.next
        tail = self.flatten_dfs(curr, curr.child)

        # children are connecting by prev and next
        # so the answer does not need any node in child
        curr.child = None

        return self.flatten_dfs(tail, temp_next)