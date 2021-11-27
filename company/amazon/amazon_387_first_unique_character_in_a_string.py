"""
Algorithm
- Counter
- Iterate each index and character,
  - When it finds a character with value 1, return the index
- If not found,
  - return -1

Complexity
- Time is O(n) to make a counter and O(n) to find the index
"""


import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)

        for i in range(len(s)):

            if count[s[i]] == 1:
                return i

        return -1


"""
- Time is O(n) to make an object of collections.Counter,
  and O(n) to find the index
- Space is O(n) to make the Counter object
"""


s = "leetcode"
s = "loveleetcode"
s = "aabb"
print(Solution().firstUniqChar(s))
