from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        # 26 English lowercase letter
        root = list(range(26))

        def find(x):
            # Path compression
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            root[x] = y

        # Merge connected components
        for equation in equations:
            if equation[1] == '=':
                # From letter to index
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')

                union(x, y)

        for equation in equations:
            if equation[1] == '!':

                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')
                # If the roots are the same, they are connected,
                # but the equation says they are not connected
                if find(x) == find(y):
                    return False

        return True


if __name__ == '__main__':
    equations = ["a==b", "b!=a"]
    equations = ["b==a", "a==b"]
    print(Solution().equationsPossible(equations))
