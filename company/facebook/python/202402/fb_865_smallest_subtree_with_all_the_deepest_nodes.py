"""
eg1
  deepest nodes: 7 and 4, so 7 and 4 itself is not a node which contains ALL the deepest nodes
eg2
  root: 0
    left: 1
      right: 2
    right 3
  Deepest node is 2 only. Because 1 doesn't have left child, 2 itself contains all the deepest nodes (here only 2)

Algo
  Assign depth to each node by DFS
  Get max depth


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        # Assign depth to each node
        depth = {None: -1}

        def dfs1(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs1(node.left, node)
                dfs1(node.right, node)

        dfs1(root)

        max_depth = max(depth.values())

        # Find the answer node
        def dfs2(node):

            # If leaf
            if not node:
                return None

            # If deepest node
            if depth[node] == max_depth:
                return node

            left_result = dfs2(node.left)
            right_result = dfs2(node.right)

            # If current node contains all the deepest nodes, current node (parent of deepest nodes) is answer
            if left_result and right_result:
                return node
            # If left result is not None, left result contains a deepest node and it's answer
            elif left_result:
                return left_result
            # If left result is None, and there is deepest node at right, return right node as answer
            elif right_result:
                return right_result
            # eg. leaf which is not deepest returns None
            else:
                return None

        return dfs2(root)