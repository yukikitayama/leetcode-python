class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Extract falling dominoes
        symbols = [[i, d] for i, d in enumerate(dominoes) if d != '.']
        # Add sentinel
        symbols = [[-1, 'L']] + symbols + [[len(dominoes), 'R']]

        # print(symbols)

        ans = list(dominoes)

        for (i, x), (j, y) in zip(symbols, symbols[1:]):

            # Same direction
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x

            # Fall to the middle
            elif x == "R" and y == "L":
                for k in range(i + 1, j):
                    # i: 0, j: 3, k: 1, k - i: 1, j - k: 2
                    # i: 0, j: 4, k: 2, k - i: 2, j - k: 2
                    if k - i < j - k:
                        ans[k] = "R"
                    elif k - i == j - k:
                        ans[k] = "."
                    elif k - i > j - k:
                        ans[k] = "L"

            # L...R no effect

        return "".join(ans)

