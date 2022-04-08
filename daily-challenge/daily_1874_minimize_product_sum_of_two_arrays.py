from typing import List
import heapq


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        counter1 = [0] * 101
        counter2 = [0] * 101

        for num1 in nums1:
            counter1[num1] += 1
        for num2 in nums2:
            counter2[num2] += 1

        p1 = 1
        p2 = 100
        ans = 0

        while p1 <= 100 and p2 >= 1:

            while p1 <= 100 and counter1[p1] == 0:
                p1 += 1

            while p2 >= 1 and counter2[p2] == 0:
                p2 -= 1

            if p1 == 101 or p2 == 0:
                break

            # min() because at least
            occ = min(counter1[p1], counter2[p2])
            ans += p1 * p2 * occ
            counter1[p1] -= occ
            counter2[p2] -= occ

        return ans


class Solution2:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()

        heap = []
        for num2 in nums2:
            # - to make it max heap
            heapq.heappush(heap, -num2)

        ans = 0

        for i in range(len(nums1)):
            num2 = heapq.heappop(heap)
            ans += nums1[i] * -num2

        return ans

class Solution1:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)

        ans = 0

        for i in range(len(nums1)):
            ans += nums1[i] * nums2[i]

        return ans


if __name__ == '__main__':
    nums1 = [5,3,4,2]
    nums2 = [4,2,2,5]
    print(Solution().minProductSum(nums1, nums2))
