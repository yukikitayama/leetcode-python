"""
s len: 4
after len: 2
(4 - 2) // 2 = 2 // 2 = 1
"""


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def remove(chars, pattern, score):
            res = 0
            write = 0

            for read in range(len(chars)):

                chars[write] = chars[read]

                if write > 0 and chars[write - 1] == pattern[0] and chars[write] == pattern[1]:
                    write -= 2
                    res += score

                write += 1

            del chars[write:]

            return res

        ans = 0
        s = list(s)

        if x > y:
            ans += remove(s, "ab", x)
            ans += remove(s, "ba", y)
        else:
            ans += remove(s, "ba", y)
            ans += remove(s, "ab", x)

        return ans

    def maximumGain1(self, s: str, x: int, y: int) -> int:
        if x > y:
            high_pair = "ab"
            low_pair = "ba"
            high_score = x
            low_score = y
        else:
            high_pair = "ba"
            low_pair = "ab"
            high_score = y
            low_score = x

        def remove(str_, pair):
            stack = []

            for ch in str_:

                if stack and stack[-1] == pair[0] and ch == pair[1]:
                    stack.pop()

                else:
                    stack.append(ch)

            return "".join(stack)

        ans = 0

        first_remove = remove(s, high_pair)

        ans += ((len(s) - len(first_remove)) // 2) * high_score

        second_remove = remove(first_remove, low_pair)

        ans += ((len(first_remove) - len(second_remove)) // 2) * low_score

        return ans
