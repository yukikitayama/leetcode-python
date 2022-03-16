"""
- Make an empty stack and push an element from pushed
- Make an index for popped to keep track of current pop item
- At the end of pushed iteration, if the index is at the end of popped list, return True
"""


from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []
        i = 0

        for j in range(len(pushed)):

            curr = pushed[j]

            stack.append(curr)

            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        # Here i should be index out of bound because of break of while loop if successful
        return i == len(popped)


if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    # True
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    # False
    print(Solution().validateStackSequences(pushed, popped))
