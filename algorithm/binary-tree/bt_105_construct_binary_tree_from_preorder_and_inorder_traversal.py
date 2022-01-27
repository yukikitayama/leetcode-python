from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        val_to_idx = {v: i for i, v in enumerate(inorder)}

        def recursion(left, right):

            if left > right:
                return None

            root_val = preorder.pop(0)
            root_node = TreeNode(val=root_val)

            split_index = val_to_idx[root_val]

            root_node.left = recursion(left, split_index - 1)
            root_node.right = recursion(split_index + 1, right)

            return root_node

        return recursion(0, len(inorder) - 1)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    ans = Solution().buildTree(preorder, inorder)
    print(ans.val)
    print(ans.left.val, ans.right.val)
    print(ans.right.left.val, ans.right.right.val)
