class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # abs() to think sign separately
        n, remainder = divmod(abs(numerator), abs(denominator))

        # Either numerator or denominator is negative, sign is negative
        sign = '-' if numerator * denominator < 0 else ''

        result = [sign + str(n), '.']

        stack = []
        # If the current remainder is already in stack,
        # it's repeating
        while remainder not in stack:
            # Append the current remainder as long as it does not repeat
            # it checks if it repeats by checking the stack
            stack.append(remainder)
            # remainder * 10 because in division, when keep dividing the remainder,
            # first append 0 to the right of remainder, and divide again with the original denominator
            n, remainder = divmod(remainder * 10, abs(denominator))

            result.append(str(n))

        idx = stack.index(remainder)
        # Quotients are in result list
        # Remainders are in stack list
        # +2 to avoid number before . and .
        # The number could be 2 digits like 10 or 15, but it's one element in the list
        # so + 2 can successfully avoid whatever number before . and .
        # And repeat start position depends on idx, which can be found by remainder index in stack
        result.insert(idx + 2, '(')
        # safe to append ) at the end, because result does not contain repeating
        result.append(')')

        # The above while loop also stops when repeating 0
        # but e.g. 0.5(0), this (0) is not necessary so remove
        # rstrip('.') because otherwise 2 / 1 will be 2.
        # rstrip() removes any trailing characters
        result = ''.join(result).replace('(0)', '').rstrip('.')

        return result


numerator = 1
denominator = 2
# "0.5"
# numerator = 4
# denominator = 333
# '0.(012)'
numerator = 2
denominator = 1
# '2'
# numerator = 2
# denominator = 3
# numerator = 1
# denominator = 5
print(Solution().fractionToDecimal(numerator, denominator))

