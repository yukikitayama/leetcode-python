"""
- Two counters
- ransom counter value <= magazine counter
- Time n, space n
"""


import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        counter = collections.Counter(magazine)

        for char in ransomNote:

            if char not in counter:
                return False

            if counter[char] <= 0:
                return False

            counter[char] -= 1

        return True


if __name__ == '__main__':
    ransomNote = "a"
    magazine = "b"
    ransomNote = "aa"
    magazine = "aab"
    print(Solution().canConstruct(ransomNote, magazine))
