import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(t, s))
