class Solution:
    def climbStairs(self, n: int) -> int:

        def climb_stairs(i, n, memo):
            # print(f'i: {i}, memo: {memo}')

            if i > n:
                return 0

            if i == n:
                return 1

            # memo array is initialized with 0, so
            # if a number is bigger than 0, it's updated and it's the answer
            if memo[i] > 0:
                # print(f'answer if, i: {i}, memo[i]: {memo[i]}')
                return memo[i]

            # Only when memo[i] does not have an answer, we call climb_stairs recursively
            memo[i] = climb_stairs(i + 1, n, memo) + climb_stairs(i + 2, n, memo)

            # print(f'Before final return with i: {i}, memo: {memo}')
            return memo[i]

        # * (n + 1) because we wanna have an extra space to contain the data for n
        # otherwise, out of bound index
        # memo[0]: steps for n, memo[1]: steps for n - 1, ... memo[-1]: steps for 0
        memo = [0] * (n + 1)
        return climb_stairs(0, n, memo)


"""
Store the result at each step in memo array,
and return the result from the array if the function called again
"""


print(Solution().climbStairs(3))
