"""
Preorder: root, left, right
Postorder: left, right, root

Ans
the first node in the preorder traversal is always the root of the tree.
Our goal, then, is to correctly determine which parts of the preorder and postorder arrays correspond to the left and right subtrees
the second element in the preorder array is the root of the left subtree
In thepostorderarray, all nodes visited beforeleftRootbelong to the left subtree. Conversely, the nodes visited afterleftRootin thepostorderarray belong to the right subtree.
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        index_in_post_order = [0] * (len(preorder) + 1)
        for i in range(len(postorder)):
            index_in_post_order[postorder[i]] = i

        def recursion(pre_start, pre_end, post_start):
            if pre_start > pre_end:
                return None

            if pre_start == pre_end:
                return TreeNode(preorder[pre_start])

            left_root = preorder[pre_start + 1]

            # +1 to include left root
            num_of_nodes_in_left = index_in_post_order[left_root] - post_start + 1

            root = TreeNode(preorder[pre_start])

            root.left = recursion(
                pre_start + 1,
                pre_start + num_of_nodes_in_left,
                post_start
            )

            root.right = recursion(
                pre_start + num_of_nodes_in_left + 1,
                pre_end,
                # After left nodes
                post_start + num_of_nodes_in_left
            )

            return root

        return recursion(0, len(preorder) - 1, 0)

