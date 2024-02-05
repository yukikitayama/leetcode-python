"""
two pass
counter from s
iterate s
  return first character whose hashmap value is 1
t: O(n), s: O(n)

one pass
Iterate from end
  curr index as ans if not seen
  if seen reset ans to -1
  add curr char to hashset seen
"""

import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)

        for i in range(len(s)):

            if counter[s[i]] == 1:
                return i

        return -1
