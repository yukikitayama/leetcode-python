"""
- min heap,
  - priority is the difference between node value and target
  - iterate all the nodes
- return kth minimum values in the min heap
- Time is O(nlogk) for each iteration push and pop operation
- Space is O(k) for heap
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
            # -abs() because the closer the node.val is to target, the smaller the abs() is
            # we wanna pop bigger difference when heap size is bigger than k
            # The mode negative the abs() is, the bigger the difference is
            heapq.heappush(heap, (-abs(target - node.val), node.val))
            if len(heap) > k:
                heapq.heappop(heap)
            inorder(node.right)

        heap = []
        inorder(root)
        return [x for _, x in heap]




