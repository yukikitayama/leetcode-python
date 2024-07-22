from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_and_index = [[h, i] for i, h in enumerate(heights)]
        height_and_index.sort(reverse=True)
        ans = []
        for _, i in height_and_index:
            ans.append(names[i])
        return ans