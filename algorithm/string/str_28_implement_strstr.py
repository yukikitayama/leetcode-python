"""
- strStr()
  - Suppose we have two strings str and sub_str. We have to find the first occurrence of sub_str in the str.
    So if the string str is “helloworld”, and substring is “lo”, then the result will be 3.
- Time is O(n * m) becuase substring of haystack making a new string, so it takes O(M)
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        # len(haystack): 5, len(needle): 2, 5 - 2: 3
        # but plus 1 because string ending index is exclusive
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i
        return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    haystack = "aaaaa"
    needle = "bba"
    haystack = "aaaaa"
    needle = "bba"
    print(Solution().strStr(haystack, needle))
