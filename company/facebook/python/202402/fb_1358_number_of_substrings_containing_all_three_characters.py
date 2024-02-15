"""
Two pointers
  right pointer move by one
    every time left pointer scan left of right ponter
T: O(N^2)

DP
  dp(i)
    Number of occurrence up to i at s from beginning
      abc: 1, abca: 1 + 1 + 1 =

Ans
  Sliding window
  Move right pointer to have a valid counter
    Use math to compute additional valid count to the right
  Move left pointer as long as valid
    With a new left base, compute the number of valid substrings
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        # ans = 0

        # # Right is exclusive
        # for right in range(3, len(s) + 1):
        #     # Left os inclusive
        #     for left in range(0, right - 1):

        #         char_set = set(s[left:right])
        #         if len(char_set) == 3:
        #             ans += 1

        # return ans

        counter = {
            "a": 0,
            "b": 0,
            "c": 0
        }
        left = 0
        right = 0
        n = len(s)
        curr_count = 0
        ans = 0

        while right < n:

            counter[s[right]] += 1

            # Expand until valid
            if counter["a"] == 0 or counter["b"] == 0 or counter["c"] == 0:
                right += 1
                continue

            while counter["a"] > 0 and counter["b"] > 0 and counter["c"] > 0:
                curr_count += 1

                right_count = n - right - 1
                curr_count += right_count

                counter[s[left]] -= 1
                left += 1

            ans += curr_count
            right += 1
            curr_count = 0

        return ans