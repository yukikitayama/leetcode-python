"""
- Greedy
- Priority queue
"""


from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))

        max_defense_so_far = 0
        ans = 0

        for i in range(len(properties) - 1, -1, -1):

            # print(f'i: {i}')

            if properties[i][1] < max_defense_so_far:
                ans += 1
                # print('increment ans')

            max_defense_so_far = max(max_defense_so_far, properties[i][1])

        return ans


if __name__ == '__main__':
    properties = [[5, 5], [6, 3], [3, 6]]
    properties = [(1, 2), (3, 4), (3, 6), (3, 7)]
    print(Solution().numberOfWeakCharacters(properties))
