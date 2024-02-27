class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        p_w = 0
        p_a = 0

        while p_w < len(word) and p_a < len(abbr):

            if abbr[p_a].isalpha():
                if abbr[p_a] != word[p_w]:
                    return False
                else:
                    p_a += 1
                    p_w += 1

            elif abbr[p_a].isdigit():

                # Invalid leading 0
                if abbr[p_a] == "0":
                    return False

                num = 0
                while p_a < len(abbr) and abbr[p_a].isdigit():
                    num = num * 10 + int(abbr[p_a])
                    p_a += 1
                # Here, p_a points at alphabet
                p_w += num
                # Here, p_w should point at the same alpha as p_a

        return p_w == len(word) and p_a == len(abbr)
