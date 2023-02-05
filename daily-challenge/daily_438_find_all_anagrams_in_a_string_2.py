"""
- Sliding window
- Hashmap
"""


from typing import List
import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        ns = len(s)
        np = len(p)

        if ns < np:
            return []

        p_count = collections.Counter(p)

        s_count = collections.Counter()

        ans = []

        for i in range(ns):

            # Add right letter
            s_count[s[i]] += 1

            # Remove left letter
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1

            if s_count == p_count:
                # When a counter is complete, index is at the end of the substring
                # so go back by the amount of p
                ans.append(i - np + 1)

        return ans


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    # [0, 6]
    print(Solution().findAnagrams(s, p))
