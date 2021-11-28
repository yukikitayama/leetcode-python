from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # If an explicit value of None is allowed
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodes = set()
        return self.can_get_target(root, k, nodes)

    def can_get_target(self, root: TreeNode, target: int, nodes: set) -> bool:
        # If there's no child, root is None
        if root is None:
            return False

        # x1 + x2 = target
        # target - x1 = x2
        if target - root.val in nodes:
            return True

        nodes.add(root.val)

        # Using "or" allows us to find at least one True
        return (self.can_get_target(root.left, target, nodes)
                or self.can_get_target(root.right, target, nodes))


# Test root = [5,3,6,2,4,null,7], k = 9
root = TreeNode(
    val=5,
    left=TreeNode(
        val=3,
        left=TreeNode(
            val=2,
            left=None,
            right=None
        ),
        right=TreeNode(
            val=4,
            left=None,
            right=None
        )
    ),
    right=TreeNode(
        val=6,
        left=None,
        right=TreeNode(
            val=7,
            left=None,
            right=None
        )
    )
)

print(Solution().findTarget(root=root, k=9))
print(Solution().findTarget(root=root, k=28))
