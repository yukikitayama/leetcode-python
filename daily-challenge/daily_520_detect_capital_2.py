class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        all_upper = True

        for i in range(len(word)):
            if not word[i].isupper():
                all_upper = False
                break

        if all_upper:
            return True

        all_lower = True

        for i in range(len(word)):
            if not word[i].islower():
                all_lower = False
                break

        if all_lower:
            return True

        first_upper = True

        for i in range(len(word)):

            if i == 0 and not word[i].isupper():
                first_upper = False
                break
            elif i > 0 and word[i].isupper():
                first_upper = False
                break

        if first_upper:
            return True

        return False


if __name__ == '__main__':
    word = 'Leetcode'
    print(Solution().detectCapitalUse(word))
