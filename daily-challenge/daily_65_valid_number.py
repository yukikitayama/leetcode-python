class Solution:
    def isNumber(self, s):
        seen_digit = False
        seen_exponent = False
        seen_dot = False

        # Iterate each character from string s
        for i, c in enumerate(s):
            # print(f'{i}: {c}')

            # Python string has a isdigit method
            if c.isdigit():
                seen_digit = True

            # Sign needs to be the first. Or you can have sign only after e/E
            # s[i - i] checks if we have e/E before sign
            elif c in ['+', '-']:
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False

            # You cannot have more than one e. And you need to have at least one digit before e/E
            # We can have digit again adter e/E, so reset seen_digit
            elif c in ['e', 'E']:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False

            # You cannot have more than one dot, and you can't also have dot aftet e/E
            elif c == '.':
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True

            # We cannot have any strings except digit, sign, e/E, and dot
            else:
                return False

        # seen_digit covers what we want
        return seen_digit


sol = Solution()
test_case = '2'
answer = sol.isNumber(test_case)
print(f'Answer: {answer}')

test_case = [
    # Valid
    '2', '0089', '-0.1', '+3.14', '4.', '-.9', '2e10', '-90E3', '3e+7', '+6e-1', '53.5e93', '-123.456e789',
    # Invalid
    'abc', '1a', '1e', 'e3', '99e2.5', '--6', '-+3', '95a54e53'
]
for s in test_case:
    answer = sol.isNumber(s)
    print(f'{s}: {answer}')
