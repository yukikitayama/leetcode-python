class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for curr_s, curr_t in zip(s, t):
            # print(f'curr_s: {curr_s}, s_to_t: {s_to_t}, s_to_t.get(curr_s): {s_to_t.get(curr_s)}, '
            #       f'curr_t: {curr_t}, t_to_s: {t_to_s}, t_to_s.get(curr_t): {t_to_s.get(curr_t)}')
            if curr_s not in s_to_t and curr_t not in t_to_s:
                s_to_t[curr_s] = curr_t
                t_to_s[curr_t] = curr_s

            elif s_to_t.get(curr_s) != curr_t or t_to_s.get(curr_t) != curr_s:
                return False

        return True


# s = "egg"
# t = "add"
# s = "foo"
# t = "bar"
# s = "paper"
# t = "title"
s = "badc"
t = "baba"
print(Solution().isIsomorphic(s, t))
