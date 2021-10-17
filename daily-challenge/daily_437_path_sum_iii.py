"""
- current node is the start of the sum
- current node is the middle of the sum
- if sum of the current node and its children is target, increment target
- return the sum of the current node and its children for its parent
"""


from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        count = 0
        k = targetSum
        h = collections.defaultdict(int)

        def preorder(node, curr_sum) -> None:
            nonlocal count

            if not node:
                return

            curr_sum += node.val

            if curr_sum == k:
                count += 1

            count += h[curr_sum - k]

            h[curr_sum] += 1

            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)

            h[curr_sum] -= 1

        preorder(root, 0)
        return count


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)
targetSum = 8
print(Solution().pathSum(root, targetSum))



