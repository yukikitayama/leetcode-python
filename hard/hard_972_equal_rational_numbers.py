"""
Geometric series
"""

import fractions


class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:

        def get_fraction(num_str):

            # Integer
            if "." not in num_str:
                return fractions.Fraction(int(num_str), 1)

            i = num_str.index(".")

            # Get integer part
            ans = fractions.Fraction(int(num_str[:i]), 1)

            # Get decimal part
            num_str = num_str[i + 1:]

            # No repeating brackets
            if "(" not in num_str:

                if num_str:
                    # 10 ** len(num_str) to get bigger denominator depending on the size of int(num_str)
                    ans += fractions.Fraction(int(num_str), 10 ** len(num_str))
                    return ans
                # Otherwise, decimap part is empty, so directly return
                else:
                    return ans

            # If there is repeating bracket
            i = num_str.index("(")

            # XX.Y(ZZ)
            # Add decimal part before repeating bracket part
            if i:
                # 10 ** i moves number to right
                ans += fractions.Fraction(int(num_str[:i]), 10 ** i)

            # Repeating bracket part always appear at the end
            # :-1 because the end closing bracket should not be included
            num_str = num_str[i + 1:-1]
            j = len(num_str)
            # Why -1?
            ans += fractions.Fraction(int(num_str), 10 ** i * (10 ** j - 1))

            return ans

        return get_fraction(s) == get_fraction(t)