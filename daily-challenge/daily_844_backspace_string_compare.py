class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1

        # Used for sequence of '#'s
        skip_s = 0
        skip_t = 0

        while i >= 0 or j >= 0:

            # print(f's[i]: {s[i]}, t[j]: {t[j]}')

            while i >= 0:
                if s[i] == '#':
                    i -= 1
                    skip_s += 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break

            while j >= 0:
                if t[j] == '#':
                    j -= 1
                    skip_t += 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

            # print(f'  s[i]: {s[i]}, t[j]: {t[j]}')

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            # print(f'    i: {i}, j: {j}')

            # If comparing nothing with char
            if (i >= 0) != (j >= 0):
                return False

            i -= 1
            j -= 1

            # print(f'    i: {i}, j: {j}')

        # print(f'i: {i}, j: {j}')

        return True


class Solution1:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def build(string):
            stack = []
            for i in range(len(string)):

                if string[i] != '#':
                    stack.append(string[i])

                elif stack and string[i] == '#':
                    stack.pop()

            return ''.join(stack)

        return build(s) == build(t)


if __name__ == '__main__':
    s = "ab#c"
    t = "ad#c"
    # s = "ab##"
    # t = "c#d#"
    s = "a#c"
    t = "b"
    s ="bbbextm"
    t = "bbb#extm"
    # False
    # s = "nzp#o#g"
    # t = "b#nzp#o#g"
    # True
    s = "aaa###a"
    t = "aaaa###a"
    # False
    print(Solution().backspaceCompare(s, t))
