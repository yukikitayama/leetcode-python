class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n + 1)
        G[0] = 1
        G[1] = 1

        # i is n
        for i in range(2, n + 1):

            # j is i
            for j in range(1, i + 1):

                G[i] += G[j - 1] * G[i - j]

        return G[n]


print(Solution().numTrees(3))
