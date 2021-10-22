class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        # zfill() adds zeros at the beginning of the string until it reaches the argument length
        a = a.zfill(n)
        b = b.zfill(n)

        # print(f'a: {a}')
        # print(f'b: {b}')

        carry = 0
        # It needs reverse answer, beaucse its appends to the end
        # so the firstly appended element is the head of the list
        # but it iterates from the last
        answer = []

        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            # If carry is 1
            if carry % 2 == 1:
                answer.append('1')

            # If carry is 0 or 2
            else:
                answer.append('0')

            # 0 // 2: 0, 1 // 2: 0, 2 // 2: 1
            # If carry is 2, we need carry 1 to the next digit, so 2 // 2: 1
            # If the current carry is 0 or 1, it does not affect the next digit,
            # so 0 by 0 // 2 or 1 // 2
            carry //= 2

        # If 1 carry is left, append it
        if carry == 1:
            answer.append('1')

        answer.reverse()
        return ''.join(answer)


a = "11"
b = "1"
a = "1010"
b = "1011"
print(Solution().addBinary(a, b))

