from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num_to_order = {arr2[i]: i for i in range(len(arr2))}
        # +1000 because of constraints
        arr1.sort(key=lambda x: num_to_order[x] if x in num_to_order else x + 1000)

        return arr1