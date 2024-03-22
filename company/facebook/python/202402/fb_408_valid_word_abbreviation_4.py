class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p_w = p_a = 0

        while p_w < len(word) and p_a < len(abbr):

            if abbr[p_a].isdigit():

                # Leading 0 not allowed
                if abbr[p_a] == "0":
                    return False

                num = 0
                while p_a < len(abbr) and abbr[p_a].isdigit():
                    num = num * 10 + int(abbr[p_a])
                    p_a += 1
                # Here p_a points at nondigit

                p_w += num

            elif word[p_w] != abbr[p_a]:
                return False

            else:
                p_w += 1
                p_a += 1

        if p_w == len(word) and p_a == len(abbr):
            return True
        else:
            return False