import collections


class Node:
    def __init__(self, val: int=0, left: 'Node'=None, right: 'Node'=None, next: 'Node'=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        queue = collections.deque([root])

        while queue:

            # Number of nodes at the current level
            size = len(queue)

            for i in range(size):

                node = queue.popleft()

                # queue always contains the nodes at the current level and the next level
                # so the nodes that we need to make next is the nodes only at the current level
                # and except the last one
                if i < size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root



