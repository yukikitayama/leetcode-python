"""
- Sort by descending units, (descending boxes)
- Priority queue
"""


from typing import List
import heapq


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        max_heap = []

        # O(n) to push all to max heap
        for i in range(len(boxTypes)):
            heapq.heappush(max_heap, (-boxTypes[i][1], boxTypes[i][0]))

        # print(f'heap: {max_heap}')

        ans = 0
        while len(max_heap) > 0 and truckSize > 0:
            unit, boxes = heapq.heappop(max_heap)
            curr = min(truckSize, boxes)
            ans += curr * -unit
            truckSize -= curr

            # print(f'curr: {curr}, truckSize: {truckSize}, ans: {ans}')

        return ans


class Solution1:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])

        # print(f'boxTypes: {boxTypes}')

        ans = 0
        # count = 0
        for i in range(len(boxTypes)):

            # while count < truckSize and boxTypes[i][0] > 0:
            #     boxTypes[i][0] -= 1
            #     count += 1
            #     ans += boxTypes[i][1]

            curr = min(truckSize, boxTypes[i][0])
            ans += curr * boxTypes[i][1]
            truckSize -= curr

            # if count >= truckSize:
            if truckSize == 0:
                break

        return ans


if __name__ == '__main__':
    boxTypes = [[1, 3], [2, 2], [3, 1]]
    truckSize = 4
    # 8
    boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
    truckSize = 10
    # 91
    boxTypes = [[1, 3], [5, 5], [2, 5], [4, 2], [4, 1], [3, 1], [2, 2], [1, 3], [2, 5], [3, 2]]
    truckSize = 35
    print(Solution().maximumUnits(boxTypes, truckSize))
