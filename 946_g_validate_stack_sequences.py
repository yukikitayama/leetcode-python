from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        stack = []
        for curr_push in pushed:
            # print(f'for')
            stack.append(curr_push)
            # print(f'stack: {stack}')
            # print(f'popped[i]: {popped[i]}')
            while stack and i < len(popped) and stack[-1] == popped[i]:
                # print('while')
                stack.pop()
                i += 1
                # print(f'stack: {stack}, i: {i}')

        return i == len(popped)


"""
Time complexity
Let n be the length of pushed and popped, for loop taks O(n) and while loop takes O(n),
so O(2n) = O(n)

Space complexity
Stack takes O(n)
"""


pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(Solution().validateStackSequences(pushed, popped))
