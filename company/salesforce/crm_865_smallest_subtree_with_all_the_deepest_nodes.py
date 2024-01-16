class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        depth = {None: -1}

        def dfs1(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs1(node.left, node)
                dfs1(node.right, node)

        dfs1(root)

        max_depth = max(depth.values())

        # import pprint
        # pprint.pprint(depth)
        # print(f"max_depth: {max_depth}")

        def dfs2(node):

            if not node or depth.get(node, None) == max_depth:
                return node

            left = dfs2(node.left)
            right = dfs2(node.right)

            if left and right:
                return node
            elif left:
                return left
            elif right:
                return right

        return dfs2(root)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    print(Solution().subtreeWithAllDeepest(root))

