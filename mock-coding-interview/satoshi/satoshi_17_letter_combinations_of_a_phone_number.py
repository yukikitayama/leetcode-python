"""
Backtracking
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        digit_to_chars = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        ans = []

        def backtracking(index, curr_comb):

            # Terminate
            if len(curr_comb) == len(digits):
                ans.append("".join(curr_comb[:]))
                return

            for i in range(index, len(digits)):

                digit = digits[i]
                candidates = digit_to_chars[digit]

                for candidate in candidates:
                    curr_comb.append(candidate)

                    backtracking(i + 1, curr_comb)

                    # Backtrack
                    curr_comb.pop()

        backtracking(0, [])

        return ans
