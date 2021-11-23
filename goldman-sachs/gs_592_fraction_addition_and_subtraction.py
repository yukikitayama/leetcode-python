"""
- Least common multiple, LCM
  - Smallest value of the common multiples
    - Multiples are numbers we get by multiply it by another number
      - Multiples of 2: [2, 4, 6, ...]
  - lcm(a, b) = (a * b) / greatest common divisor of a and b
- While making denominators the LCM, need to multiply numerators also
  - denominator * x = lcm, so x = lcm / denominator
  - x is the scaling factor to multiply numerators

Algorithm
- Extract signs, numerators, and denominators from expression
- Get least common multiplier among all the denominators
"""

# Start from the solution code because already read the description


class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Collection signs only in between fractions
        # Skip the leading negative sign before the first fraction
        # Later add this leading negative sign to numerators array
        sign = []
        for i in range(1, len(expression)):
            if expression[i] in ['+', '-']:
                sign.append(expression[i])

        num = []
        den = []
        # Separate each fraction
        for sub in expression.split('+'):
            # print(f'sub: {sub}')
            # Remove negative sign from fraction
            for subsub in sub.split('-'):
                # print(f'  subsub: {subsub}')
                # Ignore empty string produced by sub.split('-')
                # and separate numerate and denominator in fraction
                if len(subsub) > 0:
                    fraction = subsub.split('/')
                    num.append(int(fraction[0]))
                    den.append(int(fraction[1]))

                    # print(f'fraction: {fraction}')

        if expression[0] == '-':
            num[0] = -num[0]

        # print(f'sign: {sign}')
        # print(f'num: {num}')
        # print(f'den: {den}')

        # Get least common multiple among all the denominators
        lcm_den = 1
        for d in den:
            lcm_den = self.lcm(lcm_den, d)

        # print(f'LCM among denominators: {lcm_den}')

        # What's res?
        # res the summation of all the numerators after scaling up numerator by least common multiplier
        # What's this formula?
        # lcm_den / den is the scaling factor to numerator
        # e.g. fraction: 1/3, lcm_den: 6, scaling factor: 6 / 3 = 2, numerator: 1 * 2 = 2
        # so 2/6
        res = lcm_den / den[0] * num[0]

        # print(f'res: {res}')

        for i in range(1, len(num)):
            # sign[i - i] because sign array one length shorter than num and den
            # because it skips the leading negative sign if exist
            if sign[i - 1] == '+':
                res += lcm_den / den[i] * num[i]
            else:
                res -= lcm_den / den[i] * num[i]

        print(f'res: {res}')

        # g is an integer to scale down numerator and denominator
        # e.g. fraction: 2/6, res: 2, lcm_den: 6, g: 2,
        # return 1/3
        g = self.gcd(abs(res), abs(lcm_den))
        return str(int(res / g)) + '/' + str(int(lcm_den / g))

    def lcm(self, a: int, b: int) -> int:
        return int((a * b) / self.gcd(a, b))

    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            t = b
            b = a % b
            a = t
        return a


# expression = "-1/2+1/2"  # 0/1
# expression = "-1/2+1/2+1/3"  # 1/3
expression = "1/3-1/2"  # -1/6
# expression = "5/3+1/3"  # 2/1
print(Solution().fractionAddition(expression))
# print(Solution().gcd(1, 6))
# print(Solution().gcd(6, 12))
# print(Solution().lcm(2, 3))



