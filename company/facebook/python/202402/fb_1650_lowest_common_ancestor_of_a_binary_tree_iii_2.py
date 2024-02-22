"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

"""
If root is given
postorder traversal dfs
  teminate if leaf and return 0
  return the number of node of p or q
  if left and right sum is 2, return this node
  if curr and left or right sum is 2, return this node
  otherwise return max of left or right

from each p and q iterate to root
  save the path to array

two pointers to two arrays
  last common node is the LCA
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        def node_to_root(node, path):
            while node:
                path.append(node)
                node = node.parent

        p_path = []
        node_to_root(p, p_path)
        q_path = []
        node_to_root(q, q_path)

        p_pointer = len(p_path) - 1
        q_pointer = len(q_path) - 1

        ans = None

        while p_pointer >= 0 and q_pointer >= 0:

            # If current is different, last node was LCA
            if p_path[p_pointer] != q_path[q_pointer]:
                break

            ans = p_path[p_pointer]

            p_pointer -= 1
            q_pointer -= 1

        return ans