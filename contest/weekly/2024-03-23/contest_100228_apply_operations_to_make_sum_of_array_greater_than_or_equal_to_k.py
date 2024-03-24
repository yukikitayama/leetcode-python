"""
Operation problem

Greedy?

k: 1
  ans: 0
k: 2
  increment by 1, [2]
  ans: 1
k: 3
  - duplicate 1 and append twice, [1, 1, 1]
    - ans: 2
  - increment by 1, [2], increment by 1 or append both make >= k: 3,
    - ans: 2
k: 4
  - increment by 1, [2], duplicate and append once, [2, 2], ans: 2
  - duplicate/append, [1, 1], da, [1, 1, 1], da, [1, 1, 1, 1], ans: 3
  - duplicate/append, [1, 1], increment, [2, 1], increment or append make >= 4, ans: 3
k: 5
  - increment [2], increment [3], append [3, 3], ans: 3
  - append [1, 1], append [1, 1, 1], append [1, 1, 1, 1], append [1, 1, 1, 1, 1], ans: 4

DP?
Backtracking?

Greedy
Increment as much as you can, then append by minimum times
  k: 11, [4, 4, 4]
    11 / 4, 2 and 3,
      if remaining is 0, quotient,
      if remaining isn't 0, quotient + 1
      num1, num2 = divmod(11, 4)
        if num2 == 0, num1
        if num2 != 0, num1 + 1

"""


class Solution:
    def minOperations(self, k: int) -> int:

        def recursion(curr_num, ops):
            if curr_num >= k:
                return ops

            n1, n2 = divmod(k, curr_num)
            if n2 != 0:
                n1 += 1
            return min(recursion(curr_num + 1, ops + 1), n1)

        return recursion(1, 0)

    def minOperations1(self, k: int) -> int:

        ans = float("inf")

        def backtracking(curr_comb, curr_sum, num_ops):
            nonlocal ans
            if curr_sum >= k:
                ans = min(ans, num_ops)
                return

                # Increment
            curr_comb[0] += 1
            backtracking(curr_comb, curr_sum + 1, num_ops + 1)

            # Or Append
            curr_comb[0] -= 1
            curr_comb.append(curr_comb[0])
            backtracking(curr_comb, curr_sum + curr_comb[0], num_ops + 1)
            curr_comb.pop()

        backtracking([1], 1, 0)

        return ans