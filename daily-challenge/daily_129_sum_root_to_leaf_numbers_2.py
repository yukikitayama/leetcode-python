"""
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        ans = 0

        while stack:
            node, num = stack.pop()

            if node:
                num = num * 10 + node.val

                if not node.left and not node.right:
                    ans += num

                else:
                    stack.append((node.left, num))
                    stack.append((node.right, num))

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


