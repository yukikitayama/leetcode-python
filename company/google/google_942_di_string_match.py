from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lo = 0
        hi = len(s)
        ans = []
        for ch in s:
            if ch == "I":
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1
        return ans + [lo]