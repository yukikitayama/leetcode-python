class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.old_node_to_new_node = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None

        if head in self.old_node_to_new_node:
            return self.old_node_to_new_node[head]

        # Make a new Node. Initially next and random are set to be None
        # because they will be updated recursively
        node = Node(head.val, None, None)

        # Keep track of visited node because of loop
        self.old_node_to_new_node[head] = node

        # Depth first to the end of linked list
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
