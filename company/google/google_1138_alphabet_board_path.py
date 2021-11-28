import pprint


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # m is dictionary with Key: character, Value: [row, col]
        m = {c: [i // 5, i % 5] for i, c in enumerate('abcdefghijklmnopqrstuvwxyz')}

        pprint.pprint(m)

        # Start position
        x0, y0 = 0, 0

        res = []

        for c in target:

            x, y = m[c]

            # print(f'c: {c}, x: {x}, y: {y}')

            if y < y0:
                res.append('L' * (y0 - y))
            if x < x0:
                res.append('U' * (x0 - x))
            if x > x0:
                res.append('D' * (x - x0))
            if y > y0:
                res.append('R' * (y - y0))

            # After finishing moving to the destination, we can add character so use "!"
            res.append('!')

            # Update current place for the next character
            x0, y0 = x, y

        return ''.join(res)


"""
From z, if you wanna go to other characters, you need to UP first, before RIGHT, otherwise out of bound
To z, you need to go LEFT first, before DOWN, otherwise out of bound

Time complexity
Let n be the length of target
O(n) because it needs to iterate in the grid

Space complexity
Temporary string list to store answer, which is the length of target, so O(n)
"""


target = 'leet'
target = 'xyz'
target = 'zyx'
target = 'zzz'
target = 'zb'
print(Solution().alphabetBoardPath(target))
