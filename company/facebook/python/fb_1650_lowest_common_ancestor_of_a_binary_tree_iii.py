class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        def node_to_root(node, path):
            path.append(node)
            if node.parent:
                node_to_root(node.parent, path)

        p_path = []
        node_to_root(p, p_path)
        q_path = []
        node_to_root(q, q_path)

        # Right side of the arrays start with the highest common node
        # Lowest common is the common leftmost node in the arrays
        i = len(p_path) - 1
        j = len(q_path) - 1
        while i >= 0 and j >= 0:
            if p_path[i].val == q_path[j].val:
                i -= 1
                j -= 1
            else:
                break

        # +1 because the above while loop exceeds by one so to come back
        return p_path[i + 1]

