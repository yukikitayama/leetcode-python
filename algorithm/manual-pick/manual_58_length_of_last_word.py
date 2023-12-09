class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


if __name__ == "__main__":
    s = "Hello World"
    s = "   fly me   to   the moon  "
    print(Solution().lengthOfLastWord(s))
