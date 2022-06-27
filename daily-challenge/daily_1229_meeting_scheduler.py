from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        p1 = p2 = 0

        while p1 < len(slots1) and p2 < len(slots2):

            if min(slots1[p1][1], slots2[p2][1]) - max(slots1[p1][0], slots2[p2][0]) >= duration:

                return [max(slots1[p1][0], slots2[p2][0]), max(slots1[p1][0], slots2[p2][0]) + duration]

            if slots1[p1][1] < slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1

        return []


if __name__ == '__main__':
    slots1 = [[10, 50], [60, 120], [140, 210]]
    slots2 = [[0, 15], [60, 70]]
    duration = 8
    print(Solution().minAvailableDuration(slots1, slots2, duration))
