"""
hashmap
  k: digit
  v: list of letters

DFS(index, curr list of letter)
  terminate if index is digit length
    append current list of letter to answer list

  get current digit

  for letter in letter:

      dfs(i + 1, append current letter)

dfs(0, [])
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        digit_to_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(index, curr):
            if index == len(digits):
                ans.append("".join(curr[:]))
                return

            digit = digits[index]

            for letter in digit_to_letters[digit]:
                # Simply DFS
                # dfs(index + 1, curr[:] + [letter])

                # Backtracking
                curr.append(letter)
                dfs(index + 1, curr)
                curr.pop()

        ans = []

        dfs(0, [])

        return ans
