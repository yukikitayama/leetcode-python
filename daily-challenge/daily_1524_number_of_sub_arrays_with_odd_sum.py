"""
[0, 1, 4, 9]

ans
o + o = e
o + e = o
e + o = o
e + e = e
instead of keeping track of all possible subarray sums, we only need to count how many subarrays up to a given index have even sums and how many have odd sums.
if the current element is odd, it flips the parity
If the element is even, it preserves the parity

If two prefix sums have the same parity (both even or both odd), their difference will be even, meaning the subarray sum is even.
If two prefix sums have different parity (one is even, the other is odd), their difference will be odd, meaning the subarray sum is odd.
"""

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 1e9 + 7
        prefix_sum = 0
        # +1 by 0
        even_count = 1
        odd_count = 0
        ans = 0

        for num in arr:
            prefix_sum += num

            # If even
            if prefix_sum % 2 == 0:
                ans += odd_count
                ans %= MOD
                even_count += 1

            # If odd
            else:
                ans += even_count
                ans %= MOD
                odd_count += 1

        return int(ans)

    def numOfSubarrays1(self, arr: List[int]) -> int:
        MOD = 1e9 + 7

        # Conver to binary
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                arr[i] = 0
            else:
                arr[i] = 1

        dp_even = [0] * len(arr)
        dp_odd = [0] * len(arr)

        # Base
        if arr[len(arr) - 1] == 0:
            dp_even[len(arr) - 1] = 1
        else:
            dp_odd[len(arr) - 1] = 1

        # Transition
        for i in range(len(arr) - 2, -1, -1):

            # If current is odd
            if arr[i] == 1:
                dp_odd[i] = (1 + dp_even[i + 1]) % MOD
                dp_even[i] = dp_odd[i + 1]

            # If current is even
            else:
                dp_even[i] = (1 + dp_even[i + 1]) % MOD
                dp_odd[i] = dp_odd[i + 1]

        count = 0
        for odd_count in dp_odd:
            count += odd_count
            count %= MOD

        return int(count)