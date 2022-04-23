from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            """
            dfs() returns the number of excess coins.
            Positive if it's excessive, negative if short
            """

            nonlocal ans

            # Terminate recursion
            if not node:
                return 0

            # l and r are negative, when children want coins
            l = dfs(node.left)
            r = dfs(node.right)

            # abs() because l and r could be negative
            # because we want the number of moves regardless of
            # passing from child to parent or from parent to child
            ans += abs(l) + abs(r)

            # Number of moves at the current node
            # Negative if current node wants coin
            # Positive if current node can distribute coin
            # -1 because we need to keep 1 coin at the current node
            result = node.val + l + r - 1

            print(f'node.val: {node.val}, result: {result}')

            return result

        dfs(root)

        return ans


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode()
    root.right = TreeNode()

    root = TreeNode()
    root.left = TreeNode(3)
    root.right = TreeNode()

    print(Solution().distributeCoins(root))
