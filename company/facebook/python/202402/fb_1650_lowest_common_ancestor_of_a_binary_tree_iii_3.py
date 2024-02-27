# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

"""
Create array from node to root
Iterate 2 arrays
  the last common node is the LCA
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def recursion(node, list_):
            if node:
                list_.append(node)
                recursion(node.parent, list_)

        p_to_root = []
        recursion(p, p_to_root)
        q_to_root = []
        recursion(q, q_to_root)

        ans = None
        p_i = len(p_to_root) - 1
        q_i = len(q_to_root) - 1
        while p_i >= 0 and q_i >= 0:
            if p_to_root[p_i] != q_to_root[q_i]:
                break

            else:
                ans = p_to_root[p_i]
                p_i -= 1
                q_i -= 1

        return ans

    def lowestCommonAncestor1(self, p: 'Node', q: 'Node') -> 'Node':

        def recursion(node, list_):
            if node:
                list_.append(node)
                recursion(node.parent, list_)

        p_to_root = []
        recursion(p, p_to_root)
        q_to_root = []
        recursion(q, q_to_root)

        p_i = len(p_to_root) - 1
        q_i = len(q_to_root) - 1

        while p_i >= 0 and q_i >= 0:
            if p_to_root[p_i] != q_to_root[q_i]:
                break
            p_i -= 1
            q_i -= 1

        if p_i > q_i:
            return p_to_root[p_i + 1]
        else:
            return q_to_root[q_i + 1]
