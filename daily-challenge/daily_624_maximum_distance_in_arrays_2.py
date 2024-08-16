from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_num = arrays[0][0]
        max_num = arrays[0][-1]
        ans = float("-inf")
        for i in range(1, len(arrays)):
            ans = max(ans, max_num - arrays[i][0])
            ans = max(ans, arrays[i][-1] - min_num)
            min_num = min(min_num, arrays[i][0])
            max_num = max(max_num, arrays[i][-1])
        return ans

    def maxDistance2(self, arrays: List[List[int]]) -> int:
        ans = float("-inf")
        for i in range(len(arrays)):
            for j in range(len(arrays)):
                if i != j:
                    ans = max(
                        ans,
                        arrays[i][-1] - arrays[j][0]
                    )

        return ans

    def maxDistance1(self, arrays: List[List[int]]) -> int:
        min_num = float("inf")
        for i in range(len(arrays)):
            min_num = min(arrays[i][0], min_num)
        max_num = float("-inf")

        for i in range(len(arrays)):
            max_num = max(arrays[i][-1], max_num)

        return max_num - min_num