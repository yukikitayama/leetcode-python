"""
backtracking
  generate all the substring partitions
    for each substring, check if it's palindrome
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        dp = [[False] * len(s) for _ in range(len(s))]

        # Base case
        # for i in range(len(dp)):
        #     dp[i][i] = True
        # for row in dp:
        #     print(row)

        ans = []

        def backtracking(start, curr_comb):

            if start == len(s):
                ans.append(curr_comb[:])
                return

            for end in range(start, len(s)):

                # If current string is found to be palindrome from dp
                # end - start <= 2, end: 2, start: 0, you only have one character between start and end
                # end: 1, start: 0, even length palindrome
                # end: 0, start: 0, one length palindrome
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    curr_comb.append(s[start:end + 1])

                    backtracking(end + 1, curr_comb)

                    curr_comb.pop()

        backtracking(0, [])

        return ans

    def partition3(self, s: str) -> List[List[str]]:
        def is_palindrome(word):
            return word == word[::-1]

        ans = []

        def backtracking(index, curr_comb):

            if index == len(s):
                ans.append(curr_comb[:])
                return

            for end in range(index + 1, len(s) + 1):
                curr_str = s[index:end]
                if is_palindrome(curr_str):
                    curr_comb.append(curr_str)

                    backtracking(end, curr_comb)

                    # Backtrack
                    curr_comb.pop()

        backtracking(0, [])

        return ans

    def partition2(self, s: str) -> List[List[str]]:

        def is_palindrome(word):
            return word == word[::-1]

        ans = []

        def backtracking(curr_str, curr_comb):

            if not curr_str:
                ans.append(curr_comb[:])
                return

            for i in range(1, len(curr_str) + 1):

                if is_palindrome(curr_str[:i]):
                    backtracking(curr_str[i:], curr_comb + [curr_str[:i]])

        backtracking(s, [])

        return ans

    def partition1(self, s: str) -> List[List[str]]:

        ans = []

        def backtracking(index, curr_comb):

            if index == len(s):
                ans.append(curr_comb[:])
                return

            curr_char = s[index]

            if not curr_comb:
                curr_comb.append(curr_char)
                backtracking(index + 1, curr_comb)

            # curr_comb: ["a"], curr_char: "a"
            # ["aa"] or ["a", "a"]

            else:

                # Concatenate current ch to last ch
                last_str = curr_comb.pop()
                new_str = last_str + curr_char
                curr_comb.append(new_str)
                backtracking(index + 1, curr_comb)

                # Backtracking
                curr_comb.pop()
                curr_comb.append(last_str)

                # Or newly append current ch to combination
                curr_comb.append(curr_char)
                backtracking(index + 1, curr_comb)

        backtracking(0, [])

        return ans
