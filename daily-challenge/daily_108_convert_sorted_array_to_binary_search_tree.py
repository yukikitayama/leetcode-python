"""
- inorder traversal
- Pick up the number in the middle of the sorted arra as a root
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def recursion(left, right):

            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = recursion(left, mid - 1)
            root.right = recursion(mid + 1, right)

            return root

        return recursion(0, len(nums) - 1)
