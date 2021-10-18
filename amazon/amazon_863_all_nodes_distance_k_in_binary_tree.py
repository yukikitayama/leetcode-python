"""
- Do DFS to add parent TreeNode to each TreeNode in binary tree
  - It allows the traverse in tree to visit parent of the current TreeNode as well as its children
- Do BFS from the target to all the TreeNodes in distance k
"""


from typing import List
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        # Add the parent TreeNode to each TreeNode in the original binary tree
        # Make a new attribute self.par and it contains an object of TreeNode
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        # print(f'root.val: {root.val}, root.left.val: {root.left.val}, '
        #       f'root.right.val: {root.right.val}, root.par: {root.par}')
        # root_left = root.left
        # print(f'root_left.val: {root_left.val}, root_left.left.val: {root_left.left.val}, '
        #       f'root_left.right.val: {root_left.right.val}, root_left.par.val: {root_left.par.val}')
        # root_right = root.right
        # print(f'root_right.val: {root_right.val}, root_right.left.val: {root_right.left.val}, '
        #       f'root_right.right.val: {root_right.right.val}, root_right.par.val: {root_right.par.val}')

        # BFS
        # Queue: (TreeNode, distance)
        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:

            # If the first element in the queue has distance k
            if queue[0][1] == k:
                # BFS allows travers to be level by level
                # So when queue[0][1] is k, all the TreeNodes having k distance from target are currently in the queue
                # because they are added by the below for loop.
                # So it can list comprehension for all the TreeNode currently in the queue, append their val to list
                # and return it
                return [node.val for node, d in queue]

            node, d = queue.popleft()

            for neighbor in (node.left, node.right, node.par):
                if neighbor is not None and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, d + 1))

        # If the distance and k are not met in the while loop,
        # it couldn't find the TreeNodes, so return empty list
        return []


"""
- Time is O(n) to visit all the TreeNodes
- Space is O(n) for queue and parents
"""



# root = [3,5,1,6,2,0,8,null,null,7,4]
k = 2
root = TreeNode(3)
target = TreeNode(5)
root.left = target
root.right = TreeNode(1)
target.left = TreeNode(6)
target.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
target.right.left = TreeNode(7)
target.right.right = TreeNode(4)
print(Solution().distanceK(root, target, k))






