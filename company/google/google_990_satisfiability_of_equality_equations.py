from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        # 26 is the number of alphabet
        graph = [[] for _ in range(26)]

        for eqn in equations:

            # x==y or x!=y
            # If eqn[1] is '=', it's '=='
            # First character is always eqn[0]
            # and second character is always eqn[3]

            if eqn[1] == '=':

                # Convert character to integer
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                graph[x].append(y)
                graph[y].append(x)

        # print(f'graph: {graph}')

        # 26 for the alphabet
        # color[0]: 'a', color[1]: 'b', ...
        # If two characters are equal, they have the same integer.
        color = [None] * 26
        t = 0
        for start in range(26):

            if color[start] is None:

                # Increment for another group
                t += 1

                stack = [start]

                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if color[nei] is None:
                            color[nei] = t
                            stack.append(nei)

        # print(f'color: {color}')

        for eqn in equations:

            if eqn[1] == '!':

                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')

                # e.g. a!=a obvious wrong case
                if x == y:
                    return False

                # Contradicting case from the graph
                if color[x] is not None and color[x] == color[y]:
                    return False

        return True


if __name__ == '__main__':
    equations = ['a==b', 'b==a', 'c!=a', 'c==d']
    print(Solution().equationsPossible(equations))
