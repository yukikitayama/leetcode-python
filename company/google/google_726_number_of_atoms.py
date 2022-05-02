"""
- Start from the most inner and go outside to count
"""


import collections


class Solution:
    def countOfAtoms(self, formula: str) -> str:

        i = 0
        n = len(formula)

        def parse():
            nonlocal i

            count = collections.Counter()

            # formula[i] == ')' terminates recursion
            while i < n and formula[i] != ')':

                # When encountering '(', initiate recursion
                if formula[i] == '(':
                    i += 1
                    for name, v in parse().items():

                        # Here, i is already incremented after the (something) and the digit after )

                        # Append the result of recursion to the current count
                        count[name] += v
                        # print(f'    count: {count}, i: {i}')

                else:
                    i_start = i
                    i += 1
                    # e.g. Mg
                    # When formula[i] is not lower, this terminates
                    while i < n and formula[i].islower():
                        i += 1
                    # i end slicer is exclusive
                    name = formula[i_start:i]

                    i_start = i

                    while i < n and formula[i].isdigit():
                        i += 1

                    # When name isn't followed by digit, meaning count 1
                    # i is not incremented, so formula[i:i] returns '' 0 length string
                    # '' is falsy when used as ('' or 1), so when formula[i:i] returns ''
                    # count is 1
                    count[name] += int(formula[i_start:i] or 1)

                    # print(f'count: {count}')

            # Checking the digit after ')' to multiply
            i += 1
            i_start = i

            while i < n and formula[i].isdigit():
                i += 1

            # print(f'i: {i}, n: {n}, i_start: {i_start}')

            # if i_start < i, then we found a digit after ')'
            if i_start < i:

                # We need to multiply each item between '(' and ')' by the
                # number we found after ')'
                multiplicity = int(formula[i_start:i])
                for name in count:
                    count[name] *= multiplicity

                    # print(f'  count: {count}')

            # Return the result to the recursion stack
            return count

        count = parse()

        # print(f'count: {count}')

        ans = []

        for name in sorted(count):
            ans.append(name)

            # Append digit only the count is more than 1
            multiplicity = count[name]
            if multiplicity > 1:
                ans.append(str(multiplicity))

        return ''.join(ans)


if __name__ == '__main__':
    formula = "H2O"
    formula = 'H2O2'
    formula = "Mg(OH)2"
    # count: {'H': 2, 'Mg': 1, 'O': 2}, ans: "H2MgO2"
    print(Solution().countOfAtoms(formula))
