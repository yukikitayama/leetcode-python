import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        c_m = collections.Counter(magazine)

        for r in ransomNote:

            if c_m[r] <= 0:
                return False

            c_m[r] -= 1

        return True


class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        c_m = collections.Counter(magazine)
        c_r = collections.Counter(ransomNote)

        for r in c_r:

            if r not in c_m or c_r[r] > c_m[r]:
                return False

        return True


if __name__ == '__main__':
    ransomNote = "a"
    magazine = "b"
    ransomNote = "aa"
    magazine = "ab"
    ransomNote = "aa"
    magazine = "aab"
    print(Solution().canConstruct(ransomNote, magazine))
