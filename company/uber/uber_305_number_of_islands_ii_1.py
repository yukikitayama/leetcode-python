"""
- Initialize ans to 0 array with length same as positions
- Iterate row
  - Iterate col
    - If current position is 1 island
      - Update current position to 1
      - if the current island not connected to previous island
        - Increment count of islands, and insert it to ans
      - if the current island connected,
        - Insert current count to ans

- How to check if the current island is connected to previous islands

Complexity
- Time is O(nm)
- Space is O(1)
"""


from typing import List
import collections


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ans = []
        land_to_id = collections.defaultdict(int)
        num_islands = 0
        island_id = 0

        for position in positions:
            r, c = position
            overlap = set()

            # Find connected islands previously found
            if r - 1 >= 0 and (r - 1) * n + c in land_to_id:
                overlap.add(land_to_id[(r - 1) * n + c])
            if r + 1 < m and (r + 1) * n + c in land_to_id:
                overlap.add(land_to_id[(r + 1) * n + c])
            if c - 1 >= 0 and r * n + (c - 1) in land_to_id:
                overlap.add(land_to_id[r * n + (c - 1)])
            if c + 1 < n and r * n + (c + 1) in land_to_id:
                overlap.add(land_to_id[r * n + (c + 1)])
            # Positions could have duplicates
            if r * n + c in land_to_id:
                overlap.add(land_to_id[r * n + c])

            # print(f'overlap: {overlap}')

            if not overlap:
                num_islands += 1
                land_to_id[r * n + c] = island_id
                island_id += 1

            elif len(overlap) == 1:
                # New island belongs to an existing island and
                # island ID remains unchanged
                land_to_id[r * n + c] = next(iter(overlap))

            # If overlap is multiple, current new land connects separate existing islands
            # into one island
            else:
                # Consolidate separate islands into one by overwriting island ID
                # with one root id
                root_id = next(iter(overlap))
                for k, id in land_to_id.items():
                    if id in overlap:
                        land_to_id[k] = root_id

                land_to_id[r * n + c] = root_id
                num_islands -= (len(overlap) - 1)

            ans.append(num_islands)

        return ans


"""
- Key of land_to_id is calculated by current row * n + current col

Complexity
- Time is O(l) by letting l the length of positions
- Space is O(l) for hashmap
"""


m = 3
n = 3
positions = [[0,0],[0,1],[1,2],[2,1]]
# Output: [1,1,2,3]
m = 1
n = 1
positions = [[0,0]]
# Output: [1]
m = 3
n = 3
positions = [[0,0],[0,1],[1,2],[1,2]]
# Output: [1,1,2,2]
"""
positions could not be unique
0   *   *
1           *
2
    0   1   2
"""
print(Solution().numIslands2(m, n, positions))
