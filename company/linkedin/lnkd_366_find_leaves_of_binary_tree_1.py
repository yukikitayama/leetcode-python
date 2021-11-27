"""
- Define height as the number of edges from a node to the deepest leaf
  - The height is going to be the index to the answer list in appending
  - Leaf has a height 0
  - height(node) = 1 + max(height(node.left), height(node.right))
- left, right, root order traversal (<- post order traversal)
  - because height depends on children, so need to visit left and right before root
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pairs = []

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.get_height(root)

        # Takes O(nlogn) time
        self.pairs.sort()

        n = len(self.pairs)
        i = 0
        height = 0
        ans = []

        while i < n:
            nums = []
            while i < n and self.pairs[i][0] == height:
                nums.append(self.pairs[i][1])
                i += 1
            ans.append(nums)
            height += 1
        return ans

    def get_height(self, node):
        # Return -1 because leaf height will be 0 by -1 + 1
        if not node:
            return -1

        # Postorder by left, right and root at the return statement
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        curr_height = 1 + max(left_height, right_height)

        self.pairs.append((curr_height, node.val))

        return curr_height


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(Solution().findLeaves(root))

