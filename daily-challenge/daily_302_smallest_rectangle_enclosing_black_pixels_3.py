"""
"""


from typing import List


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        # Find the first black pixel 1, so opt: True
        top = self.search_rows(image, 0, x, True)
        # Find the first while pixel 0, so opt: False
        bottom = self.search_rows(image, x + 1, len(image), False)

        left = self.search_columns(image, 0, y, top, bottom, True)

        right = self.search_columns(image, y + 1, len(image[0]), top, bottom, False)

        return (right - left) * (bottom - top)

    def search_rows(self, image, i, j, opt):
        while i != j:
            m = (i + j) // 2
            if ('1' in image[m]) == opt:
                j = m
            else:
                i = m + 1
        return i

    def search_columns(self, image, i, j, top, bottom, opt):
        while i != j:
            m = (i + j) // 2
            if any(image[k][m] == '1' for k in range(top, bottom)) == opt:
                j = m
            else:
                i = m + 1
        return i


"""
Test
bottom
i: 1, j: 2, opt: F, m: 1, 
"""


image = [
    ["0","0","1","0"],
    ["0","1","1","0"],
    ["0","1","0","0"]
]
x = 0
y = 2
print(Solution().minArea(image, x, y))







