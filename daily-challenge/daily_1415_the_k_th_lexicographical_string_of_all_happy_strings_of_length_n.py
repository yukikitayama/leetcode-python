"""
backtracking
  save all patterns to array
  backtracking(index, comb)
    if index is n,
      append comb to array
return kth from array
  if k is bigger than array, return ""
"""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        buffer = []
        ans = ""
        counter = 0

        def backtracking(index, comb):
            nonlocal ans, counter

            if index == n:
                counter += 1
                if counter == k:
                    ans = "".join(comb)
                return

            for ch in ["a", "b", "c"]:

                if comb and comb[-1] == ch:
                    continue

                comb.append(ch)
                backtracking(index + 1, comb)

                if ans:
                    return

                comb.pop()

        backtracking(0, [])

        return ans

    def getHappyString1(self, n: int, k: int) -> str:

        buffer = []

        def backtracking(index, comb):

            if index == n:
                buffer.append("".join(comb))
                return

            for ch in ["a", "b", "c"]:

                if comb and comb[-1] == ch:
                    continue

                comb.append(ch)
                backtracking(index + 1, comb)
                comb.pop()

        backtracking(0, [])

        return buffer[k - 1] if k <= len(buffer) else ""
