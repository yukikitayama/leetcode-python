"""
- We can always solve the problem with at most 2 steps
  - Remove all a, and remove all b
- Steps: {0, 1, 2}
"""


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0

        elif s == s[::-1]:
            return 1

        else:
            return 2


if __name__ == '__main__':
    s = "ababa"
    s = "abb"
    s = "baabb"
    print(Solution().removePalindromeSub(s))
