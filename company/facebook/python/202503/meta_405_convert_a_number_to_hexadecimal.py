class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return "0"

        # -1 should be        11111111111111111111111111111111
        # bin(1 << 32):      100000000000000000000000000000000
        # bin((1 << 32) - 1): 11111111111111111111111111111111
        # 32 because constraints is 2^31
        if num < 0:
            num = (1 << 32) + num

        hexs = "0123456789abcdef"
        ans = []
        while num > 0:
            i = num % 16
            ans.append(hexs[i])
            num //= 16

        return "".join(ans[::-1])