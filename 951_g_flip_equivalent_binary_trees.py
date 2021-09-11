from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#         # Check if both are None
#         # If at below leaf
#         if root1 is root2:
#             return True
#
#         # not root1 is True if root1 is None
#         # The below is True if there's at least one True
#         # True if it's leaf and value is different
#         # if not root1 or not r


"""
If statements having multiple and/or conditions and return statement having multiple and/or expression are evaluated
from the left. Once the conditions are met, the rest of the conditions/expressions won't run
"""


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # True if both are None, meaning both does not have values, so no need to consider flipped or not, just return
        # True
        if root1 is root2:
            return True

        # The above check both are None, so the below checks either is None, so not equivalent
        # or if values are different, the are not equivalent, so return false
        if not root1 or not root2 or root1.val != root2.val:
            # print(f'root1: {root1}, root2: {root2}')
            # print(f'root1.val: {root1.val}, root2.val: {root2.val}')
            return False

        # The first and second returns True if with no flips, they are the same
        # The third and forth returns True if with flips, they are the same
        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))


def test(root2):
    # return True and True or True and root2.val
    return False and False or True and True


print(f'test(1): {test(1)}')


# root1 = TreeNode(1, TreeNode(2), TreeNode(3))
# root2 = TreeNode(1, TreeNode(2))
# print(Solution().flipEquiv(root1, root2))

# root1 = TreeNode(1, TreeNode(2), TreeNode(3))
# root2 = TreeNode(1, TreeNode(3), TreeNode(2))
root1 = TreeNode(1)
# root1 = TreeNode(2)
# root2 = TreeNode(1)
# root2 = TreeNode(3)
root2 = None
# print(f'not root1: {not root1}')
# print(f'not root2: {not root2}')
# root1 = root1.left
# root2 = root2.left
# print(f'{not root1}')

# if root1.val != root2.val:
#     print('if')
# else:
#     print('else')
if not root2 or root1.val != root2.val:
    print('if')
else:
    print('else')

# print('not root1 or not root2 or root1.val != root2.val')
if not root1 or not root2 or root1.val != root2.val:
    print('if')
    # print(f'if, not root1: {not root1}, not root2: {not root2}, root1.val != root2.val: {root1.val != root2.val}')
else:
    print('else')
# if root1 is root2:
#     print('if')
# else:
#     print('else')
# if None is None:
#     print('if')
# else:
#     print('else')
#
# if True or False:
#     print('if')
# else:
#     print('else')
# if True and False:
#     print('if')
# else:
#     print('else')
# print('False and False')
# if False and False:
#     print('if')
# else:
#     print('else')
