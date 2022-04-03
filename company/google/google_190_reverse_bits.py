class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        power = 31

        while n:
            # n & 1 gets the rightmost bit
            # << power because we need to reverse,
            # rightmost needs to be pushed to left
            ans += (n & 1) << power
            # next leftmost
            power -= 1
            # next rightmost
            n = n >> 1

        return ans


if __name__ == '__main__':
    n = 43261596
    # 964176192
    print(Solution().reverseBits(n))
