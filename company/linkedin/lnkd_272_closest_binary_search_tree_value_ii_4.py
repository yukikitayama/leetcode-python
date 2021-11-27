"""
Idea
- Inorder traversal of binary search tree is an ascending order
  - Inorder is left, root, right
- Take abs difference between each val and target
  - sort in ascending order
  - return the first kth element

Complexity
- Time is O(nlogn) to sort
- Space is O(n) for array to keep each node value
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:

        def inorder(node):
            # return inorder(node.left) + [node.val] + inorder(node.right) if node else []

            if not node:
                return

            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        # ans = inorder(root)

        ans = []
        inorder(root)
        # print(ans)

        ans.sort(key=lambda x: abs(x - target))
        return ans[:k]


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
target = 3.714286
k = 2
print(Solution().closestKValues(root, target, k))




