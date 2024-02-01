"""
- greedy

- Binary search
  - Each binary search needs the for loop in ribbons to count
  - Time is O(NlogN), N for the for loop and logN for the binary search
"""


from typing import List


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # Initial min length of ribbon
        start = 1
        # Initial max length of ribbon
        end = max(ribbons)

        while start <= end:

            mid = start + (end - start) // 2
            curr_k = 0
            for ribbon in ribbons:
                curr_k += ribbon // mid

            # print(f'mid: {mid}, curr_k: {curr_k}, start: {start}, end: {end}')

            # If we get too many ribbons, it means we cut it too short
            # so increase start to get longer ribbon
            if curr_k >= k:
                start = mid + 1

            # If we get smaller number of ribbon than required ribbons
            # We need to decrease end to get shorter ribbon to get more number of ribbons
            else:
                end = mid - 1

        # print(f'mid: {mid}, curr_k: {curr_k}, start: {start}, end: {end}')

        return end


if __name__ == '__main__':
    ribbons = [9, 7, 5]
    k = 3
    print(Solution().maxLength(ribbons, k))
