"""
Question
- What should I do with the leading zero

Idea
- dfs
- When a child is None, increment ans by the number
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, number):

            nonlocal ans

            # if not node:
            #     ans += number
            #     return

            if node:

                number = number * 10 + node.val

                if not node.left and not node.right:
                    ans += number

                dfs(node.left, number)
                dfs(node.right, number)

        dfs(root, 0)

        return ans


# 25
root = TreeNode(1, TreeNode(2), TreeNode(3))

# 1026
root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

"""
  4
 / \
9   0
 \
  1

Expected: 531
"""
# root = TreeNode(4)
# root.left = TreeNode(9)
# root.right = TreeNode(0)
# root.left.right = TreeNode(1)

print(Solution().sumNumbers(root))


