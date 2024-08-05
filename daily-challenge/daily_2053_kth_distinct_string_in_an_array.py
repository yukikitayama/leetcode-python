from typing import List
import collections


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = collections.Counter(arr)

        encounter = 0

        for str_ in arr:

            if counter[str_] == 1:

                encounter += 1

                if encounter == k:
                    return str_

        return ""