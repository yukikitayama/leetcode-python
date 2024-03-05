"""
Two pointers
  while left <= right and left and right character are the same
    if same
      move left and right until different character
return right - left + 1
  if negative then 0
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:

            # This gives us the different character in each iteration
            curr_char = s[left]

            # eg. "abba", left: 3, right: 2, and terminate,
            # ans = 2 - 3 + 1 = 0
            while left <= right and s[left] == curr_char:
                left += 1

            while left < right and s[right] == curr_char:
                right -= 1

            # print(curr_char, left, right)

        return right - left + 1

    def minimumLength1(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:

                while left < right and s[left] == s[left + 1]:
                    left += 1

                while left < right and s[right] == s[right - 1]:
                    right -= 1

                # Go to next different character
                left += 1
                right -= 1

            elif s[left] != s[right]:
                break

        if right - left + 1 <= 0:
            return 0
        else:
            return right - left + 1
