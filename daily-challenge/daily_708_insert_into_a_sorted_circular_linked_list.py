class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        if head is None:
            new_node = Node(insertVal, None)
            # To make a cycle
            new_node.next = new_node
            return new_node

        prev = head
        curr = head.next
        # Flag to indicate we can insert a value right away and end the below while loop
        # before the 1 cycle iteration
        to_insert = False

        while True:

            # Between min and max, easiest case
            if prev.val <= insertVal <= curr.val:
                to_insert = True

            # Locate tail
            elif prev.val > curr.val:
                # Append after max value or append before min value
                if insertVal >= prev.val or insertVal <= curr.val:
                    to_insert = True

            if to_insert:
                # In any of the above case, we can insert between curr and prev
                # prev.next was originally curr, but update prev.next to insert inbetween
                prev.next = Node(insertVal, curr)
                return head

            prev, curr = curr, curr.next

            # If iterated one cycle
            if prev == head:
                break

        # When the linked list contains all uniform values
        prev.next = Node(insertVal, curr)
        return head


