from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

        # -x[0], x[1] allows us to find BOTH attack and defense strictly greater
        # e.g. [[10, 4], [10, 3]] is not both strictly greater relationship
        # this will be sorted to [[10, 3], [10, 4]], so the second defense is greater than the first
        # which will appear in for loop

        # If attack is tie, second defense is guaranteed to be greater or equal
        # If first attack is bigger, as long as second defense is smaller, it's guaranteed that
        # both second attack and defense is smaller than the both first.
        properties.sort(key=lambda x: (-x[0], x[1]))

        # print(properties)

        ans = 0
        max_defense_so_far = 0

        for _, defense in properties:
            if defense < max_defense_so_far:
                ans += 1
                # print(f'_: {_}, defense: {defense}')
            else:
                max_defense_so_far = defense

        return ans


if __name__ == '__main__':
    properties = [[5, 5], [6, 3], [3, 6]]
    properties = [[2, 2], [3, 3]]
    properties = [[1, 5], [10, 4], [4, 3]]
    # properties = [[1, 4], [10, 4], [10, 3]]
    print(Solution().numberOfWeakCharacters(properties))
