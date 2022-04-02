from typing import List
import collections


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)

        count_set = set(count.values())

        # print(count)
        # print(count_set)

        return len(count) == len(count_set)


if __name__ == '__main__':
    arr = [1,2,2,1,1,3]
    arr = [1, 2]
    print(Solution().uniqueOccurrences(arr))
