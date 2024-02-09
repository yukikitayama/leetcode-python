from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        min_so_far = float("inf")

        ans = 0

        for i in range(len(citations) - 1, -1, -1):

            citation = citations[i]
            min_so_far = min(min_so_far, citation)

            array_length = len(citations) - i

            if min_so_far >= array_length:
                ans = array_length

            else:
                break

        return ans

