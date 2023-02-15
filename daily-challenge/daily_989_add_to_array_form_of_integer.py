from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        num[-1] += k

        for i in range(len(num) - 1, -1, -1):

            # Make it one digit
            carry, num[i] = divmod(num[i], 10)

            # print(f'i: {i}, carry: {carry}')

            if i:
                # Next left digit
                num[i - 1] += carry

        # e.g. num: [9, 9], k: i, [1, 0, 0]
        # i: 0, carry: 1, num[0]: 0
        if carry:
            num = [int(i) for i in str(carry)] + num

        return num


if __name__ == "__main__":
    num = [1, 2, 0, 0]
    k = 34

    num = [2, 1, 5]
    k = 806
    # 1021

    num = [0]
    k = 10000
    # [1, 0, 0, 0, 0]
    print(Solution().addToArrayForm(num, k))


