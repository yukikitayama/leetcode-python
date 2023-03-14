"""
- Recursion
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

        def recursion(node, curr):

            # print(f'curr: {curr}')

            nonlocal ans

            if node:

                curr = curr * 10 + node.val

                if not node.left and not node.right:
                    # print('here')
                    ans += curr

                recursion(node.left, curr)
                recursion(node.right, curr)

        recursion(root, 0)

        return ans


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().sumNumbers(root))
