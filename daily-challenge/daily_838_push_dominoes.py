class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        # print(f'symbols: {symbols}')

        # Split string into a list of characters
        ans = list(dominoes)

        # print(f'ans: {ans}')

        # Window by symbols
        # The last element won't be iterated in symbols, but you see the last from symbols[1:]
        for (i, x), (j, y) in zip(symbols, symbols[1:]):

            # print(f'i: {i}, x: {x}, j: {j}, y: {y}')

            # If L == L or R == R
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x

            # R ... L, the middle dominoes needs to be updated
            elif x == 'R' and y == 'L':

                length = j - i - 1
                mid = (j + i) // 2
                # print(f'length: {length}, mid: {mid}')

                for k in range(i + 1, j):

                    if length % 2 == 0:
                        if k <= mid:
                            ans[k] = 'R'
                        else:
                            ans[k] = 'L'
                    elif length % 2 != 0:
                        if k < mid:
                            ans[k] = 'R'
                        elif k > mid:
                            ans[k] = 'L'

        return ''.join(ans)


if __name__ == '__main__':
    dominoes = "RR.L"
    # dominoes = ".L.R...LR..L.."
    print(Solution().pushDominoes(dominoes))
