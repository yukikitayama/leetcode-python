from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def backtracking(start, curr):

            if start >= len(s):
                ans.append(curr[:])

            for end in range(start, len(s)):

                if is_palindrome(start, end):
                    curr.append(s[start:end + 1])
                    backtracking(end + 1, curr)
                    curr.pop()

        def is_palindrome(low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True

        ans = []

        backtracking(0, [])

        return ans


if __name__ == '__main__':
    s = "aab"
    print(Solution().partition(s))
