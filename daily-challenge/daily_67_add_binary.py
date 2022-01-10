class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)

        # Add until no more carry
        while y:
            # Add without carry
            # Adding carry will be successful when x does not have 1 at the same position as y carry
            ans = x ^ y
            # Get carry
            carry = (x & y) << 1
            x = ans
            y = carry

        # [2:] removes the leading '0b'
        return bin(x)[2:]



class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        # zfill() adds zeroes at the beginning of the string until reach the specified length
        a = a.zfill(n)
        b = b.zfill(n)
        carry = 0
        ans = []

        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry % 2 == 1:
                ans.append('1')
            else:
                ans.append('0')

            # If carry is 1 or 0, carry to be 0
            # If carry is 2, carry to be 1
            carry //= 2

        if carry == 1:
            ans.append('1')
        ans.reverse()
        return ''.join(ans)


if __name__ == '__main__':
    a = '11'
    b = '1'
    print(Solution().addBinary(a, b))
