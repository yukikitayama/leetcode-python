from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)

        ans = 0

        # Because we only need to get maximum distance,
        # both i and j need not to reach end
        # When either reach the end, we already have the max distance
        while i < n and j < m:

            # In each iteration, we increment either i or j

            # If it's not valid because nums1 is bigger
            # increment index for nums1 to find smaller number
            # Fix j and move i
            if nums1[i] > nums2[j]:
                i += 1

            # Fix i and move j
            else:
                ans = max(ans, j - i)
                # Move ahead j because we wanna see a longer distance from fixed i to ahead j
                j += 1

        return ans


if __name__ == '__main__':
    nums1 = [55, 30, 5, 4, 2]
    nums2 = [100, 20, 10, 10, 5]
    # 2
    print(Solution().maxDistance(nums1, nums2))
