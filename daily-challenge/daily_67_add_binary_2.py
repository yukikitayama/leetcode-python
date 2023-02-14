class Solution:
    def addBinary(self, a: str, b: str) -> str:

        x = int(a, 2)
        y = int(b, 2)

        # print(f'x: {x}, y: {y}')

        while y:
            # Get 1 bit until carry won't appear
            without_carry = x ^ y
            # Move carry until carry won't appear
            carry = (x & y) << 1
            x = without_carry
            y = carry

        # print(f'x: {x}, bin(x): {bin(x)}')

        # bin(x): "0bBINARY"

        return bin(x)[2:]


if __name__ == "__main__":
    a = "11"
    b = "1"
    print(Solution().addBinary(a, b))
