"""
Algorithm
- Initialize start index to 0 and end index to 0
- Iterate index for s from 0 to length of s exclusive
  - For each index, use it as the center of the substring, and expand outwards as long as it's palindrome
  - We track the length of the substring
  - If the length is longer the max length so far, we update the start and end index
    - Initially start and end both are 0, so end - start = 0
      - e.g. Index is 0,
        - when length is 1, start and end should stay 0
        - length: 2, start: 0, end: 1, because s[0:1+1] = s[0:2] = ab if s is abc
          current index is the center around the palindromic substring
          so start is half minus and end is hald plus
          start = i - (length - 1) // 2, end = i + length // 2
          length: 2, i: 3, start: 3 - (2 - 1) // 2 = 3 - 0 = 3, end: 3 + 2 // 2 = 4
          s[3:4+1] = s[3:5], if s is abcdef, s[3:5] = de
          length: 3, i: 2, start: 2 - (3 - 1) // 2 = 2 - 1 = 1, end: 2 + 2 // 2 = 3,
          s[1:3+1] = s[1:4], if s is abcdef, s[1:4] = bcd
  - How to expand around the center?
    - Center could be one character or 2 characters, so center is left and right argument
      if center is one character left == right
    - Center can expand as long as left and right are in boundary and s[left] == s[right]
      - Use while loop
      - Decrement left and increment right because we need to expand outwards
    - Length of the substring is right - left - 1
      - -1 because when we break out of while loop it's invalid, so we need to subtract
      - right: 3, left: 1, length: 3 - 1 - 1 = 1
- Use the updated start and end index, substring the given s, and return the substring.

Complexity
- Let n be the length of s
- Time is O(n^2) because O(n) to find the center index, and O(n) to expand around each center
- Space is O(1) because it only use pointers
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0

        # Iterate each character in s as the candidate center character for palindrome
        for i in range(len(s)):

            # Center is one character case
            length_one = self.expand_around_center(s, i, i)

            # Center is two characters case
            length_two = self.expand_around_center(s, i, i + 1)

            # Max because we wanna have the longest
            current_length = max(length_one, length_two)

            # Update start and end indices to eventually return substring of s
            if current_length > end - start:
                # The current index of i is the center index,
                # So left is minus half and right is plus half
                start = i - (current_length - 1) // 2
                end = i + current_length // 2

        # What we return is substring
        return s[start:end + 1]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        # Avoid modifying input indices
        l = left
        r = right

        # As long as it won't be out of boundary and it's palindrome, expand outwards
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return r - l - 1



"""
Test
expand_around_center
When palindrome length is 1,
l:2, r:2, s[l] == s[r]: T, l: 1, r: 3, 
s[l] == s[r]: F
r - l - 1: 3 - 1 - 1 = 1
"""


s = "babad"
s = "cbbd"
s = "a"
s = "ac"
print(Solution().longestPalindrome(s))
