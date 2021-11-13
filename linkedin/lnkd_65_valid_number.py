class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_exponent = False
        seen_dot = False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ['+', '-']:
                # If not the first position or no e or E in front of it, False
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
            elif c in ['e', 'E']:
                # Cannot have two exponents, and need to have digits before exponent
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif c == '.':
                # Not allowed to have 2 dots and after exponent only have integers, not decimals with dot
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            # If other characters, they are not allowed
            else:
                return False

        # Because this tracks seen digit after exponent
        return seen_digit

