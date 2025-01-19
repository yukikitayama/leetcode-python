from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_to_rank = {}
        sorted_arr = sorted(arr)
        rank = 1
        for num in sorted_arr:
            if num not in num_to_rank:
                num_to_rank[num] = rank
                rank += 1
        for i in range(len(arr)):
            arr[i] = num_to_rank[arr[i]]
        return arr
