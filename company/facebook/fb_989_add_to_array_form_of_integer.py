from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num[-1] += k

        for i in range(len(num) - 1, -1, -1):
            carry, num[i] = divmod(num[i], 10)

            if i:
                num[i - 1] += carry

            # print(f'carry: {carry}, curr: {curr}')

        # We could have carry more than 10, so
        # we cannot [carry] + num
        # We need to carry: 100 -> [1, 0, 0]
        # which can be done by map(int, str(carry))
        # carry: 100 -> '100' -> ['1', '0', '0'] -> [1, 0, 0]
        if carry:
            num = list(map(int, str(carry))) + num

        return num


if __name__ == '__main__':
    num = [1, 2, 0, 0]
    k = 34
    num = [2, 1, 5]
    k = 806
    print(Solution().addToArrayForm(num, k))
