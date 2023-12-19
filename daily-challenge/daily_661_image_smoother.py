from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        def compute_avg(r, c):
            sum_ = 0
            count = 0
            for i in [r - 1, r, r + 1]:
                for j in [c - 1, c, c + 1]:
                    if 0 <= i < len(img) and 0 <= j < len(img[0]):
                        sum_ += img[i][j]
                        count += 1
            return int(sum_ / count)

        ans = [[None] * len(img[0]) for _ in range(len(img))]

        for r in range(len(img)):
            for c in range(len(img[0])):

                avg = compute_avg(r, c)
                ans[r][c] = avg

        return ans


if __name__ == "__main__":
    img = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
    print(Solution().imageSmoother(img))
