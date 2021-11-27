"""
- level order traversal
- Once it finds the val bigger than root, return it
- If iterates all the node and still not found, return -1

  2
 / \
2   2
   / \
  2   4

- Time O(n), space: O(n)

  1
 / \
3   1
   / \
  1  2

- failed
"""


from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.min_value = None

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        self.min_value = root.val

        queue = collections.deque([root])

        while queue:
            curr = queue.popleft()

            if curr.val > self.min_value:
                return curr.val
            else:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return -1


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)

print(Solution().findSecondMinimumValue(root))







