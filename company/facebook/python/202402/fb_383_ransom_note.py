import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = collections.Counter(magazine)

        # print(counter)

        for ch in ransomNote:

            if ch not in counter:
                return False

            else:
                counter[ch] -= 1
                if counter[ch] == 0:
                    del counter[ch]

        return True
