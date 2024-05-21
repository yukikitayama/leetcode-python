"""
exp
[5,1,5,5,1,3,4,5,1,4]
exp: [1,1,2,3,2,3,4,5,3,5]

Stack
"""

from typing import List
import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans = []

        lis = []

        for i in range(len(obstacles)):

            # print(i, obstacles[i], lis)

            j = bisect.bisect_right(lis, obstacles[i])

            if j == len(lis):
                lis.append(obstacles[i])
            else:
                lis[j] = obstacles[i]

            ans.append(j + 1)

        return ans

    def longestObstacleCourseAtEachPosition1(self, obstacles: List[int]) -> List[int]:
        """Brute force, T: O()"""

        def find_length(index):
            curr = obstacles[index]
            res = 1

            for i in range(index - 1, -1, -1):

                if obstacles[i] <= curr:
                    res += 1
                    curr = obstacles[i]

            return res

        ans = []

        for i in range(len(obstacles)):
            l = find_length(i)

            ans.append(l)

        return ans