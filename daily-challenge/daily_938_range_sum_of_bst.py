"""
Result
- Start: 7:14
- End: 7:21
- Solved: 1
- Optimized: 0
- saw solution: 0
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        ans = 0

        def recursion(node):

            nonlocal ans

            if not node:
                return

            if low <= node.val <= high:
                ans += node.val

            # If current value is bigger than low
            # then left child also could be in range
            if low < node.val:
                recursion(node.left)

            # If current value is smaller than low
            # then left child is smaller than current value
            # so it's not in range

            # If current value is smaller than high
            # then right child also could be in range
            if node.val < high:
                recursion(node.right)

            # If current value is bigger than high
            # then right child also bigger than high
            # so it's not in range

        recursion(root)

        return ans


"""
- Time O(n)
- Space O(n) for recursion stack
"""


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
low = 7
high = 15
print(Solution().rangeSumBST(root, low, high))
