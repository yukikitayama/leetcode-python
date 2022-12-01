class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        count_a = count_b = 0
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        for i in range(len(s) // 2):

            if s[i] in vowels:
                count_a += 1

            if s[-(i + 1)] in vowels:
                count_b += 1

        return count_a == count_b


if __name__ == '__main__':
    s = 'book'
    s = 'textbook'
    print(Solution().halvesAreAlike(s))
