"""
- Time is O(N) because it visits all the node
- Space is O(N) because of recursion stack
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        ans = 0

        if not root:
            return ans

        def recursion(node, depth):

            # nonlocal to update variable outside this function
            nonlocal ans

            # When it reaches a leaf, meaning found the depth,
            # so update the answer
            if not node.children:
                ans = max(ans, depth)

            if node.children:
                for child in node.children:
                    recursion(child, depth + 1)

        recursion(root, 1)

        return ans


if __name__ == '__main__':
    root = Node(1)
    root.children = [Node(3), Node(2), Node(4)]
    root.children[0].children = [Node(5), Node(6)]
    print(Solution().maxDepth(root))
