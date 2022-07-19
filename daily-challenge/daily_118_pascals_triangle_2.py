from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for i in range(numRows):

            if i == 0:
                ans.append([1])

            else:
                curr = []
                for j in range(i + 1):
                    if j == 0:
                        curr.append(1)

                    elif j == i:
                        curr.append(1)

                    else:
                        sum_ = ans[-1][j - 1] + ans[-1][j]
                        curr.append(sum_)
                ans.append(curr)

            # print(f'i: {i}')
            # [print(row) for row in ans]
            # print()

        return ans


if __name__ == '__main__':
    numRows = 3
    numRows = 5
    print(Solution().generate(numRows))

