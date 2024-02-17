"""
Data structure is list of list
  length of each list
    list[0]: 2**0
    list[1]: 2**1
    list[2]: 2**2
Insert
  Check last list
    If the length is less than the 2 power length, append
      append newly created treenode object
      Connect current node with parent
        parent is in prev array
        if current position is 0 or 1, parent is 0, current_position // 2
        if current position is 2 or 3, parent is 1
    If not
      append new list to the data structure
get_root
  Return the first element of the first list
"""

from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

        # Queue always stores node which have missing child
        self.queue = collections.deque()

        # Initilize to populate node to the above queue
        buffer = collections.deque()
        buffer.append(root)

        while buffer:
            node = buffer.popleft()
            # If either child is missing
            if not node.left or not node.right:
                self.queue.append(node)

            # To have complete structure, append from left
            if node.left:
                buffer.append(node.left)
            if node.right:
                buffer.append(node.right)

        for node in self.queue:
            print(node.val)

    def insert(self, val: int) -> int:

        # leftmost of queue has the first parent node which needs child
        node = self.queue[0]

        self.queue.append(TreeNode(val))

        # To have complete structure, fill from the missing left
        if not node.left:
            node.left = self.queue[-1]
        # Queue only contains node which has missing left or right child
        # so if the above left is not missing, right is always missing
        else:
            node.right = self.queue[-1]

            # Remove a node which has both left and right child from the queue
            self.queue.popleft()

        return node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()