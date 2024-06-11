from typing import List
import heapq


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """Counting sort"""
        count = [0] * (max(arr1) + 1)
        for val in arr1:
            count[val] += 1

        ans = []
        for val in arr2:
            for _ in range(count[val]):
                ans.append(val)
                count[val] -= 1

        # Remaining
        for i in range(len(count)):
            if count[i] > 0:
                for _ in range(count[i]):
                    ans.append(i)

        return ans

    def relativeSortArray1(self, arr1: List[int], arr2: List[int]) -> List[int]:
        val_to_order = {}
        for i in range(len(arr2)):
            val_to_order[arr2[i]] = i

        min_heap = []
        not_appear = []
        for val in arr1:
            if val in val_to_order:
                heapq.heappush(min_heap, (val_to_order[val], val))
            else:
                not_appear.append(val)

        ans = []
        while min_heap:
            order, val = heapq.heappop(min_heap)
            ans.append(val)

        not_appear.sort()

        return ans + not_appear