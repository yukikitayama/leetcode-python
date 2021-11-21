"""
- Inorder
  - left, root, right
- Postorder
  - left, right, root
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def helper(left, right):
            if left > right:
                # Return None because we wanna connect None to child
                return None

            # postorder is left, right, root. So the end of list contains root
            post_val = postorder.pop()
            root = TreeNode(post_val)
            index = inorder_val_to_index[post_val]

            # Recursion returns root node, so the nodes are connected to right and left child
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)
            return root

        inorder_val_to_index = {val: i for i, val in enumerate(inorder)}

        return helper(0, len(inorder) - 1)


"""
- Time is O(n) because recursion visit all the nodes
"""




