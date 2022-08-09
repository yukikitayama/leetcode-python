from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        val_to_index = {x: i for i, x in enumerate(arr)}
        dp = [1] * len(arr)

        for i, x in enumerate(arr):

            for j in range(i):

                # Suppose arr[j] is left child
                if x % arr[j] == 0:

                    right = x / arr[j]

                    if right in val_to_index:

                        dp[i] += dp[j] * dp[val_to_index[right]]
                        dp[i] %= (10**9 + 7)

        # print(dp)

        return sum(dp) % (10**9 + 7)


if __name__ == '__main__':
    arr = [2, 4]
    print(Solution().numFactoredBinaryTrees(arr))
