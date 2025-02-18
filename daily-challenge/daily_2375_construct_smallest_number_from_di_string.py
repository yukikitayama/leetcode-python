"""
used boolean array
combination integer array
backtracking(index, comb)
  if index == pattern length
    update answer
    terminate
  Transition
    if "I"
      each digit from which is bigger than prev to largest
        use unused digit
        recursion
      backtrack

"""

import itertools


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        stack = []

        for i in range(len(pattern) + 1):

            stack.append(i + 1)

            if i == len(pattern) or pattern[i] == "I":
                while stack:
                    ans.append(str(stack.pop()))

        return "".join(ans)

    def smallestNumber2(self, pattern: str) -> str:

        numbers = "".join(str(num) for num in range(1, len(pattern) + 2))

        def check(permutation_str):
            for i in range(len(pattern)):
                if pattern[i] == "I" and permutation_str[i] > permutation_str[i + 1]:
                    return False
                elif pattern[i] == "D" and permutation_str[i] < permutation_str[i + 1]:
                    return False
            return True

        for permutation in itertools.permutations(numbers, r=len(numbers)):
            permutation_str = "".join(permutation)
            if check(permutation_str):
                return permutation_str

    def smallestNumber1(self, pattern: str) -> str:
        ans = "9" * (len(pattern) + 1)

        used = [False] * 9

        def backtracking(index, comb):
            nonlocal ans

            if index == len(pattern):
                ans = min(
                    ans,
                    "".join([str(num) for num in comb])
                )
                return

            if index == 0:
                for digit in range(1, 9 + 1):
                    used[digit - 1] = True
                    comb.append(digit)
                    backtracking(index + 1, comb)
                    comb.pop()
                    used[digit - 1] = False

            if pattern[index] == "I":
                for digit in range(min(comb[-1] + 1, 9), 9 + 1):
                    if not used[digit - 1]:
                        used[digit - 1] = True
                        comb.append(digit)
                        backtracking(index + 1, comb)
                        comb.pop()
                        used[digit - 1] = False

            elif pattern[index] == "D":
                for digit in range(max(comb[-1] - 1, 1), 0, -1):
                    if not used[digit - 1]:
                        used[digit - 1] = True
                        comb.append(digit)
                        backtracking(index + 1, comb)
                        comb.pop()
                        used[digit - 1] = False

        backtracking(0, [])

        return ans