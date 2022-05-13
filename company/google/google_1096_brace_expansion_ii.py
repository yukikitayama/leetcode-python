from typing import List


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = []
        res = []
        cur = []

        for i in range(len(expression)):

            v = expression[i]

            # print(f'i: {i}, v: {v}')

            if v.isalpha():
                cur = [c + v for c in cur or ['']]

            elif v == '{':
                stack.append(res)
                stack.append(cur)
                res = []
                cur = []

            elif v == '}':
                pre_cur = stack.pop()
                pre_res = stack.pop()

                cur = [p + c for c in res + cur for p in pre_cur or ['']]

                # print(f'    pre_cur: {pre_cur}, pre_res: {pre_res}')

                res = pre_res

            elif v == ',':
                res += cur
                cur = []

            # print(f'  cur: {cur}')
            # print(f'  stack: {stack}')
            # print(f'  res: {res}')

        return sorted(set(res + cur))


if __name__ == '__main__':
    expression = "{a,b}{c,{d,e}}"
    # ["ac","ad","ae","bc","bd","be"]
    print(Solution().braceExpansionII(expression))
