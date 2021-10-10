"""
- Pick a cell as the value to which all other cells will change
- A cell % x needs to be 0 to be possible
  - Once it finds a cell which % x is not zero, return -1
- Initialize ans to float('inf')
- Initialize current counter to 0
- Pick a standard value
- Iterate each row
  - Iterate each col
    - If current value is bigger than the standard value
      - subtract x until it will be equal to the standard
        - Increment counter every time
    - If current value is smakker than the standard value
      - Add x until it will be equal to the standard
        - Increment counter every time
"""


from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        # Edge case [[something]], because it's single value in the grid
        # no need to do operations
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        ans = float('inf')

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                standard = grid[row][col]

                # if standard % x != 0:
                #     return -1

                counter = 0

                for row2 in range(len(grid)):
                    for col2 in range(len(grid[0])):

                        if row2 == row and col2 == col:
                            continue

                        current_value = grid[row2][col2]

                        if current_value > standard:
                            while current_value > standard:
                                current_value -= x
                                counter += 1

                            # print(f'current_value: {current_value}, standard: {standard}')

                            if current_value != standard:
                                return -1

                        elif current_value < standard:
                            while current_value < standard:
                                current_value += x
                                counter += 1

                            if current_value != standard:
                                return -1

                ans = min(ans, counter)

        return ans


grid = [[2, 4], [6, 8]]
x = 2
grid = [[1,5],[2,3]]
x = 1
grid = [[1,2],[3,4]]
x = 2
grid = [[146]]
x = 86
# Expected: 0
grid = [[931,128],[639,712]]
x = 73
# Expected: 12
print(Solution().minOperations(grid, x))

