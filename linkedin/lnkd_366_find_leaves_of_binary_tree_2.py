"""
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = []

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.get_height(root)

        return self.ans

    def get_height(self, node):
        # Return -1 because leaf height will be 0 by -1 + 1
        if not node:
            return -1

        # Postorder by left, right and root at the return statement
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        curr_height = 1 + max(left_height, right_height)

        # It only appends a new list when it first reaches here
        # e.g. 2nd time, curr_height: 0, self.ans: [[X]], len(self.ans): 1
        # curr_height: 1 (first time), self.ans: [[x1, x2, ...]], len(self.ans): 1
        #   By appending, self.ans: [[x1, x2, ...], []]
        if len(self.ans) == curr_height:
            self.ans.append([])

        self.ans[curr_height].append(node.val)

        return curr_height


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(Solution().findLeaves(root))

