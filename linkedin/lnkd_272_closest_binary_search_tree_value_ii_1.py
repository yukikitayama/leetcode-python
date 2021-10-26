"""
- Iterate all the nodes
- Keep the list size k and append and pop the k closest values to target
- compare current node value to target,
  - if target is smaller, go to left
  - If target is larger, go to right

- Inorder traversal in binary search tree gives us the non-decreasing order
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:

        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        # nums is non-decreasing order because of inorder traversal in binary search tree
        # O(n) to make an array
        nums = inorder(root)

        print(f'nums: {nums}')

        # O(nlogn) to sort
        nums.sort(key=lambda x: abs(x - target))

        print(f'nums: {nums}')

        return nums[:k]


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
target = 3.714286
k = 2
print(Solution().closestKValues(root, target, k))


