"""

"""


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, curr=[]):
            # if the combination is done
            if len(curr) == k:

                print(f'  append: {curr[:]} to output')

                # Takes O(k) to copy each element to output
                output.append(curr[:])

            # Takes nCk to make combinations
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)

                print(f'    before backtrack curr: {curr}')

                # use next integers to complete the combination
                backtrack(i + 1, curr)

                print(f'    after backtrack curr: {curr}')

                # backtrack
                curr.pop()

        output = []
        backtrack()
        return output


"""
n: 4
k: 2
output: []
first: 1, curr: [], i: 1, curr: [1], backtrack(2, [1])
first: 2, curr: [1], i: 2, curr: [1, 2], backtrack(3, [1, 2])
if: T, output: [[1, 2]], i: 3, 
"""


n = 4
k = 2
print(Solution().combine(n, k))

