"""
Inorder traversal of BST is ascending order -> sorted

linked list conversion
Node(2).left: Node(1)
Node(2).right: Node(3)
This is already correct

Node(4).left: Node(2)
needs to
Node(4).left: Node(3)

recursion(node, parent)
  right needs parent node

  body
    left

    root

    right

Save every node to array by inorder traversal
After traversal
for loop
  curr node left = left index node
    if i = 0, right most index
  curr node right = right index node
    if i = len() - 1, left most index

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    # def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

    #     if not root:
    #         return root

    #     inorder_nodes = []

    #     def inorder(node):

    #         # Terminal recursion
    #         if not node:
    #             return

    #         inorder(node.left)
    #         inorder_nodes.append(node)
    #         inorder(node.right)

    #     inorder(root)

    #     for i in range(len(inorder_nodes)):

    #         node = inorder_nodes[i]

    #         if i == 0:
    #             node.left = inorder_nodes[-1]
    #         else:
    #             node.left = inorder_nodes[i - 1]

    #         if i == len(inorder_nodes) - 1:
    #             node.right = inorder_nodes[0]
    #         else:
    #             node.right = inorder_nodes[i + 1]

    #     return inorder_nodes[0]

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        first = None
        last = None

        def inorder(node):
            nonlocal first, last

            if not node:
                return

            inorder(node.left)

            # Except first node
            if last:
                last.right = node
                node.left = last
            # First node
            else:
                first = node

            # Update curr node to be the last node
            last = node

            inorder(node.right)

        inorder(root)

        # The above inorder didn't set first left, and last right
        first.left = last
        last.right = first

        return first