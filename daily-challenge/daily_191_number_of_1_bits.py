class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:

            ans += 1
            # Make the least significant 1 bit to 0 bit
            n = n & (n - 1)

        return ans


class Solution1:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        mask = 1

        for i in range(32):

            result = n & mask

            # print(f'result: {result}')

            if result != 0:
                ans += 1
                # print(f'  ans: {ans}')

            mask <<= 1

        return ans


if __name__ == '__main__':
    # print(int('01011', 2))
    n = int('01011', 2)
    print(Solution().hammingWeight(n))
