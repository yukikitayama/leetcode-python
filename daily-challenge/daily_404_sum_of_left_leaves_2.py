"""
- Morris tree traversal preorder
  - By modifying the input tree, improve recursion/iteration space O(n) to O(1)

"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        curr = root

        while curr:

            if not curr.left:
                curr = curr.right

            else:
                prev = curr.left

                if not prev.left and not prev.right:
                    ans += prev.val

                while prev.right and prev.right is not curr:
                    prev = prev.right

                if not prev.right:
                    prev.right = curr
                    curr = curr.left

                else:
                    prev.right = None
                    curr = curr.right
        return ans


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# root = TreeNode(1)

print(Solution().sumOfLeftLeaves(root))
