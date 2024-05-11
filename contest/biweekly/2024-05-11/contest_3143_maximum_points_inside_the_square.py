"""
Compute distance between each point and center
  max of abs x or abs y
sort distance array
iterate
  if current char in hashset,
    return ans
  save current distance as ans
  save current char in hashset
return ans
"""

from typing import List
import collections


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        distances = set()
        distance_to_chars = collections.defaultdict(list)
        for i in range(len(points)):
            d = max(abs(points[i][0]), abs(points[i][1]))
            distances.add(d)
            distance_to_chars[d].append(s[i])
        distances = list(distances)
        distances.sort()

        # print(distances)
        # print(distance_to_chars)

        ans = 0
        chars = set()
        for d in distances:

            for ch in distance_to_chars[d]:
                if ch in chars:
                    return ans
                else:
                    chars.add(ch)

            ans += len(distance_to_chars[d])

        return ans
