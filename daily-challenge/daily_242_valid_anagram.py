import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)
        return counter_s == counter_t


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    s = "rat"
    t = "car"
    print(Solution().isAnagram(s, t))
