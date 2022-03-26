"""
- Leaf is both left and right child missing
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def dfs(node, path_str):

            if node:

                path_str += str(node.val)

                # If node is leaf, add it to answer list and end the recursion
                if not node.left and not node.right:
                    ans.append(path_str)

                else:
                    path_str += '->'
                    dfs(node.left, path_str)
                    dfs(node.right, path_str)

        ans = []
        dfs(root, '')
        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    print(Solution().binaryTreePaths(root))
