from typing import List
import collections


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        n = len(parent)
        children = collections.defaultdict(list)

        for i in range(n):

            p = parent[i]
            children[p].append(i)

        # print(children)

        def dfs(node):

            nonlocal ans

            if node not in children:
                return 1

            first_longest = second_longest = 0

            for child in children[node]:

                child_longest = dfs(child)

                if s[node] == s[child]:
                    continue

                if child_longest > first_longest:
                    second_longest = first_longest
                    first_longest = child_longest
                elif child_longest > second_longest:
                    second_longest = child_longest

            # print(f'max: {ans}, {first_longest}, {second_longest}')

            ans = max(ans, first_longest + second_longest + 1)

            return first_longest + 1

        ans = 1

        dfs(0)

        return ans


if __name__ == '__main__':
    parent = [-1, 0, 0, 1, 1, 2]
    s = "abacbe"
    parent = [-1, 0, 1]
    s = 'aab'
    print(Solution().longestPath(parent, s))
