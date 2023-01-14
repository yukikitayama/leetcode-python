"""
- Make graph
- Find smallest character in each connected component
"""


from typing import List


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        # Make equivalence mapping between s1 and s2
        graph = [[0] * 26 for _ in range(26)]
        for i in range(len(s1)):
            s1_i = ord(s1[i]) - ord('a')
            s2_i = ord(s2[i]) - ord('a')
            graph[s1_i][s2_i] = 1
            graph[s2_i][s1_i] = 1

        # [print(row) for row in graph]

        def dfs(src, component: List[int]):

            nonlocal min_char

            visited[src] = 1

            component.append(src)

            min_char = min(min_char, src)

            for i in range(26):
                # If there's edge and not yet visited
                if graph[src][i] and not visited[i]:
                    dfs(i, component)

        visited = [0] * 26
        # For each character, store the equivalent minimum index
        mapping_char = [i for i in range(26)]

        for i in range(26):
            if not visited[i]:

                # Connected component
                component = []

                # Variable to keep track the minimum character index so far in each component
                min_char = 27

                # Traverse connected component
                # and compute minimum character index in the component
                dfs(i, component)

                for v in component:

                    mapping_char[v] = min_char

        # print(mapping_char)

        ans = []
        for ch in baseStr:
            # i is difference between this character and 'a'
            i = mapping_char[ord(ch) - ord('a')]

            # Convert the difference to actual character
            # +ord('a') because base is 'a'
            ans.append(chr(i + ord('a')))

        return ''.join(ans)


if __name__ == '__main__':
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    print(Solution().smallestEquivalentString(s1, s2, baseStr))
