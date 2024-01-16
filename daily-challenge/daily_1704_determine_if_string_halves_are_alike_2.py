"""
for loop from 0 to len(s) / 2 exclusive
  a counter is i
  b counter is i + len(s) / 2
compare 2 counters at the end
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vowels = {
            "a", "e", "i", "o", "u",
            "A", "E", "I", "O", "U"
        }

        counter_a = 0
        counter_b = 0

        for i in range(len(s) // 2):

            if s[i] in vowels:
                counter_a += 1
            if s[i + len(s) // 2] in vowels:
                counter_b += 1

        return counter_a == counter_b


if __name__ == "__main__":
    s = "book"
    s = "textbook"
    print(Solution().halvesAreAlike(s))





