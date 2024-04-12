"""
Preorder is root, left, right
Stack?
If we see an element greater than previous
  min so far
"""

from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        min_limit = float("-inf")
        stack = []

        for i in range(len(preorder)):

            # print(i, preorder[i], min_limit, stack)

            if not stack:
                stack.append(preorder[i])

            elif stack and stack[-1] > preorder[i]:
                if preorder[i] < min_limit:
                    return False
                else:
                    stack.append(preorder[i])

            else:
                while stack and stack[-1] < preorder[i]:
                    prev_num = stack.pop()
                    min_limit = max(min_limit, prev_num)
                stack.append(preorder[i])

        return True
