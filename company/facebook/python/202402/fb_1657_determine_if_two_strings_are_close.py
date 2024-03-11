"""
word1: "abbzzca"
qord2: "babzzcz"
exp: F
"""

import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        counter1 = collections.Counter(word1)
        cc1 = collections.Counter(counter1.values())

        counter2 = collections.Counter(word2)
        cc2 = collections.Counter(counter2.values())

        if counter1.keys() == counter2.keys():
            if cc1 == cc2:
                return True
            else:
                return False
        else:
            return False

    def closeStrings2(self, word1: str, word2: str) -> bool:

        counter1 = collections.Counter(word1)
        cc1 = collections.Counter(counter1.values())

        counter2 = collections.Counter(word2)
        cc2 = collections.Counter(counter2.values())

        if counter1.keys() == counter2.keys():
            cc1.subtract(cc2)
            if len(set(cc1.values())) == 1 and list(cc1.values())[0] == 0:
                return True
            else:
                return False
        else:
            return False

    def closeStrings1(self, word1: str, word2: str) -> bool:

        # Edge
        if len(word1) != len(word2):
            return False

        counter1 = collections.Counter(word1)
        cc1 = collections.Counter(counter1.values())

        counter2 = collections.Counter(word2)
        cc2 = collections.Counter(counter2.values())

        print(counter1)
        print(cc1)
        print(counter2)
        print(cc2)

        if counter1.keys() != counter2.keys():
            return False
        else:
            if len(cc1.keys()) > len(cc2.keys()):
                for k, v in cc1.items():
                    if k not in cc2:
                        return False
                    elif cc1[k] != cc2[k]:
                        return False
                return True
            else:
                for k, v in cc2.items():
                    if k not in cc1:
                        return False
                    elif cc2[k] != cc1[k]:
                        return False
                return True
