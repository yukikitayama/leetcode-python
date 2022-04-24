"""
- Full binary tree, each node has 0 or 2 children
- Even number of nodes cannot be full binary tree

"""


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.memo = {
            0: [],
            1: [TreeNode(0)]
        }

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n not in self.memo:
            ans = []

            for x in range(n):

                # -1 because current node use 1
                # The rest of the stuff meaning total n minus the left distributed x and current distributed 1
                # is y
                y = n - 1 - x

                # print(f'x: {x}, y: {y}')

                # When x: [], the 2 for loops will not be performed
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):

                        # print(f'  left: {left}, right: {right}')

                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right

                        ans.append(bns)

                        # print(bns.val, bns.left, bns.right)
                        # print(f'  ans: {ans}')

            # When we find answer for the current n,
            # memoize it
            self.memo[n] = ans
            # print(f'memo: {self.memo}')

        return self.memo[n]


if __name__ == '__main__':
    n = 3
    ans = Solution().allPossibleFBT(n)
    # print(ans[0].val)
    # print(ans[0].left.val, ans[0].left.left, ans[0].left.right)
    # print(ans[0].right.val, ans[0].right.left, ans[0].right.right)

    print()

    for i in []:
        for j in [1, 2, 3]:
            print(f'i: {i}, j: {j}')

