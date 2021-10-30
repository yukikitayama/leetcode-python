"""
- Time is O(klogk) because the while loop takes k and the inside has the
  O(logk) heappop and heappush.
- Space is O(k) for the heap an visited set
"""


from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        visited = set()
        heap = []
        ans = []


        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))

        # While loop takes O(k)
        while len(ans) < k and heap:

            # heappop takes O(logk) because it rearranges log(k) elements
            _, p1, p2 = heapq.heappop(heap)

            ans.append([nums1[p1], nums2[p2]])

            # If nums1 still has the next num and it has not used the pair
            if p1 + 1 < len(nums1) and (p1 + 1, p2) not in visited:
                # heappush takes O(logk)
                heapq.heappush(heap, (nums1[p1 + 1] + nums2[p2], p1 + 1, p2))
                visited.add((p1 + 1, p2))

            if p2 + 1 < len(nums2) and (p1, p2 + 1) not in visited:
                heapq.heappush(heap, (nums1[p1] + nums2[p2 + 1], p1, p2 + 1))
                visited.add((p1, p2 + 1))

        return ans


nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
# nums1 = [1,1,2]
# nums2 = [1,2,3]
# k = 2
# nums1 = [1,2]
# nums2 = [3]
# k = 3
nums1 = [1,1,2]
nums2 = [1,2,3]
k = 10
print(Solution().kSmallestPairs(nums1, nums2, k))




