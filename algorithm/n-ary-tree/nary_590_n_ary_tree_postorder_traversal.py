"""
- Time is O(N) because it visits all the node
- Space is O(N) because of the recursion stack
"""


from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        ans = []

        # Recursion function throws error when root is None
        # because None doesn't have children attribute
        if not root:
            return ans

        def recursion(node):

            # End of recursion when the current node is a leaf
            if not node.children:
                ans.append(node.val)
                return

            if node.children:
                # Traverse children from left to right for postorder
                for child in node.children:
                    recursion(child)

            # When all the children of the current node finishes,
            # root can be added because of postorder
            ans.append(node.val)
            return

        recursion(root)

        return ans


if __name__ == '__main__':
    root = Node(1)
    root.children = [Node(3), Node(2), Node(4)]
    root.children[0].children = [Node(5), Node(6)]
    print(Solution().postorder(root))
