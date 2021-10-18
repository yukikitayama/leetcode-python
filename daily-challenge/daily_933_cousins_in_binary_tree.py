from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.recorded_depth = None
        self.is_cousin = False

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.dfs(root, 0, x, y)
        return self.is_cousin

    def dfs(self, node, depth, x, y):
        # To stop recursion at the leaf
        # The returned value is okay to be False, because
        # either x or y is found, so no depth information is made
        if node is None:
            return False

        if self.recorded_depth and depth > self.recorded_depth:
            return False

        # If either node is found, record the depth,
        # and the other node depth will need to be identical
        if node.val == x or node.val == y:
            if self.recorded_depth is None:
                self.recorded_depth = depth

            # For the first node found (either x or y), it always returns T
            # But for the second node found, check if it's in the same depth to know the second is
            # the cousin of the first found
            return self.recorded_depth == depth

        # Left and right will be True as long as either x or y is found in the child and
        # they are at the recorded_depth
        left = self.dfs(node.left, depth + 1, x, y)
        right = self.dfs(node.right, depth + 1, x, y)

        # To update is_cousin to True, both left and right needs to found x or y
        # and they are at the same depth
        # recorded_depth != depth + 1 will be true if x and y are found at the one level below of the
        # current node. For example, recorded_depth: 1, depth: 0,
        #   1
        #  / \
        # 2   3
        # But it will be false if, for example, recorded_depth: 2, depth: 0,
        #   1
        #  / \
        # 2   3
        #  \   \
        #   4   5
        # so the below if statement will run when the current node is 1 to set is_cousin to True
        if left and right and self.recorded_depth != depth + 1:
            self.is_cousin = True

        # Return True if either x or y is found at children and depth is recorded_depth
        return left or right


"""
Test
root = [1,2,3,null,4,null,5], x = 5, y = 4
  1
 / \
2   3
 \   \
  4   5
recorded_depth: None
is_cousin: F,
dfs(root: 1, 0, 5, 4)
node: root:1, depth: 0, x: 5, y: 4, if1: F, if2: F, if3: F, dfs(1.left, 1, 5, 4)
node: 2, depth: 1, if1: F, if2: F, if3: F, dfs(2.left, 2, 5, 4)
node: None, depth: 2, if1: F, return F, 
2.left: F, dfs(2.right, 2, 5, 4)
node: 4, depth: 2, if1: F, if2: F, node.val: 4, node.val == y: T, if3: T, if4: T, recorded_depth: 2, recorded_depth == depth: T, return T
2.right: T, if5: F because left is F, left or right: T, return T
1.left: T, dfs(1.right, 1, 5, 4)
node: 3, depth: 1, if1: F, if2: F, if3: F, dfs(3.left, 2, 5, 4)
node: None, if1: F, return F
3.left: F, dfs(3.right, 2, 5, 4)
node: 5, depth: 2, if1: F, if2: F, node.val: 5, node.val == x: T, if3: T, if4: F, recorded_depth == depth: T, return T,
3.right: F, if5: F because left is F, left or right: T, return T
1.right: T, left: T, right: T, depth: 0, recorded_depth:2 != (depth + 1): 1: T, self.is_cousin: T, left or right: T, return T
return is_cousin: T,


root = [1,2,3,null,4], x = 2, y = 3
  1
 / \
2   3
 \
  4
dfs(root: 1, 0, 2, 3)
node: 1, depth: 0, if1: F, if2: F, if3: F, dfs(1.left, 1, 2, 3)
node: 2, depth: 1, if1: F, if2: F, if3: T, recorded_depth: 1, return T
1.left: T, dfs(1.right, 1, 2, 3)
node: 3, depth: 1, if1: F, if2: F, if3: T, return T
1.right: T, left: T, right: T, recorded_depth != depth + 1: 1 != 1, F, 
"""
