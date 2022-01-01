from typing import Optional


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        if not head:
            node = Node(val=insertVal)
            node.next = node
            return node

        prev = head
        curr = head.next

        while True:

            if prev.val <= insertVal <= curr.val:
                node = Node(insertVal, curr)
                prev.next = node
                return head

            # Before tail, prev is smaller than curr because ascending order
            # But after tail, it could be reverse
            # In that case, prev is tail and curr is head
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    node = Node(insertVal, curr)
                    prev.next = node
                    return head

            # Iterate
            prev, curr = curr, curr.next

            # After one cycle
            if prev == head:
                break

        # It reaches here if it finished one cycle and only unique values in cycle
        node = Node(insertVal, curr)
        prev.next = node
        return head


