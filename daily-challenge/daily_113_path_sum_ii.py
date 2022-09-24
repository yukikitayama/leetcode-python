"""
- recursion
- Carry curr list
- If leaf, get sum of curr list
- If sum == target, append the curr list to ans list
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def recursion(node, curr, remain):

            if not node:
                return

            curr.append(node.val)

            if remain == node.val and not node.left and not node.right:
                ans.append(curr[:])
            else:
                recursion(node.left, curr, remain - node.val)
                recursion(node.right, curr, remain - node.val)

            curr.pop()

        recursion(root, [], targetSum)

        return ans


if __name__ == '__main__':
    pass
