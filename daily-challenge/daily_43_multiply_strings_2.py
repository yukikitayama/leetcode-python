class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # This length is the max length of integer str made by multiplication
        res = [0] * (len(num1) + len(num2))
        # print(res)
        # e.g. len(num1) = 3, range(start: 2, stop: -1, step -1), [2, 1, 0] because stop is exclusive
        for i in range(len(num1) - 1, -1, -1):
            # print(i)
            # Carry is a number going to the next higher digit which occurs by multiplication
            carry = 0
            for j in range(len(num2) - 1, -1, -1):
                # By subtracting by ord('0'), get an integer
                tmp = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0')) + carry
                # i + j + 1 because it will come back when j starts from the end
                # When i: 2, j: 2, i + j + 1: 5, len(res): 6, 5 is the last index
                carry = (res[i + j + 1] + tmp) // 10
                # % 10 gives us the current digit only
                res[i + j + 1] = (res[i + j + 1] + tmp) % 10

                # print(f'i: {i}, j: {j}, Tmp: {tmp}, carry: {carry}, res: {res}')

            # We could have left over 1
            res[i] += carry

        # A list of chars to one string
        # map(func, iter), so map(str, res) converts list of integers to list of chars,
        # and then join
        res = ''.join(map(str, res))
        # print(f'before return res: {res}')

        # We could have leading 0 but we need to remove it
        # lstrip removes spaces at the left
        # If res is '000', res.lstrip('0') returns ''
        # '' is False
        return '0' if res.lstrip('0') == '' else res.lstrip('0')




num1 = "123"
num2 = "456"
print(Solution().multiply(num1, num2))
