class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join([word[::-1] for word in words])


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print(Solution().reverseWords(s))
