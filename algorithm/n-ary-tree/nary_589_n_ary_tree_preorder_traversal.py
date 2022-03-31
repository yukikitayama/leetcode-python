"""
- Time is O(N) because visiting all the nodes
- Space is O(N) because of recursion stack
"""


from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        ans = []

        def recursion(node):

            # End condition of recursion
            if not node:
                return

            ans.append(node.val)

            # Add if statement to check whether node has children
            # to avoid error when accessing node.children in the for loop
            if node.children:
                for child in node.children:
                    recursion(child)

        recursion(root)

        return ans


if __name__ == '__main__':
    root = Node(1)
    root.children = [Node(3), Node(2), Node(4)]
    root.children[0].children = [Node(5), Node(6)]
    print(Solution().preorder(root))
