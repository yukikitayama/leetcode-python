"""
- binary search to make time O(logn)
"""


from typing import List
import bisect


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = bisect.bisect_right(letters, target)
        return letters[idx % len(letters)]


letters = ["c","f","j"]
target = "a"
letters = ["c","f","j"]
target = "c"
letters = ["c","f","j"]
target = "d"
letters = ["c","f","j"]
target = "g"
letters = ["c","f","j"]
target = "j"
print(Solution().nextGreatestLetter(letters, target))

