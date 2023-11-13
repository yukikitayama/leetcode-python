class Solution:
    def sortVowels(self, s: str) -> str:
        ans = [None] * len(s)

        v = []
        for i in range(len(s)):

            if s[i].lower() in ["a", "e", "i", "o", "u"]:
                v.append((ord(s[i]), s[i]))

            else:
                ans[i] = s[i]

        v.sort(reverse=True)

        for i in range(len(ans)):

            if not ans[i]:
                num, ch = v.pop()
                ans[i] = ch

        return "".join(ans)


class SolutionCountingSort:
    def sortVowels(self, s: str) -> str:

        def is_vowel(ch):
            return ch.lower() in ["a", "e", "i", "o", "u"]

        counts = [0] * 200

        for i in range(len(s)):
            if is_vowel(s[i]):
                counts[ord(s[i]) - ord("A")] += 1

        ans = [None] * len(s)
        sorted_vowels = "AEIOUaeiou"
        j = 0

        for i in range(len(s)):

            if not is_vowel(s[i]):
                ans[i] = s[i]

            else:
                while counts[ord(sorted_vowels[j]) - ord("A")] == 0:
                    j += 1

                ans[i] = sorted_vowels[j]
                counts[ord(sorted_vowels[j]) - ord("A")] -= 1

        return "".join(ans)


if __name__ == "__main__":
    s = "lEetcOde"
    print(Solution().sortVowels(s))
    print(SolutionCountingSort().sortVowels(s))