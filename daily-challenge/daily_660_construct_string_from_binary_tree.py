"""
- Recursion function returns string
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def recursion(node):

            if not node:
                return ''

            left_str = recursion(node.left)
            right_str = recursion(node.right)

            if left_str and right_str:
                return f'{node.val}({left_str})({right_str})'
            elif left_str and not right_str:
                return f'{node.val}({left_str})'
            elif not left_str and right_str:
                return f'{node.val}()({right_str})'
            else:
                return f'{node.val}'

        return recursion(root)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)

    ans = Solution().tree2str(root)
    print(ans)
