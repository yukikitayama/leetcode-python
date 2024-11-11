from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:

        ans = []

        p1 = p2 = p3 = 0
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):

            if arr1[p1] == arr2[p2] == arr3[p3]:

                ans.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1

            else:

                if arr1[p1] < arr2[p2]:
                    p1 += 1
                elif arr2[p2] < arr3[p3]:
                    p2 += 1
                else:
                    p3 += 1

        return ans

    def arraysIntersection1(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        set2 = set(arr2)
        set3 = set(arr3)
        ans = []

        for num in arr1:
            if num in set2 and num in set3:
                ans.append(num)

        return ans