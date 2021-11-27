"""
"""


from typing import Optional, List
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            # -1 to abs because it needs to heappop after this
            # without -1, it will pop the smallest element, which is not what we want
            # With negative absolute difference, the smallest difference will be deeper in the priority queue
            heapq.heappush(heap, (-abs(node.val - target), node.val))
            if len(heap) > k:
                heapq.heappop(heap)
            inorder(node.right)

        heap = []
        inorder(root)
        # First element is abs diff between node and target
        # Second element is the actual node value which we want to return
        return [x for _, x in heap]


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
target = 3.714286
k = 2
print(Solution().closestKValues(root, target, k))


