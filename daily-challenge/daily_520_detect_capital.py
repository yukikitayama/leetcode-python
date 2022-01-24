class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        n = len(word)

        all_capital = True
        all_not_capital = True
        first_capital = True

        # Check all capital
        for i in range(n):
            if not word[i].isupper():
                all_capital = False
                break

        if all_capital:
            return True

        # Check all not capital
        for i in range(n):
            if word[i].isupper():
                all_not_capital = False
                break

        if all_not_capital:
            return True

        # Check only first capital
        if not word[0].isupper():
            first_capital = False

        if first_capital:
            for i in range(1, n):
                if word[i].isupper():
                    first_capital = False

        if first_capital:
            return True

        return False


if __name__ == '__main__':
    word = "USA"
    word = "FlaG"
    print(Solution().detectCapitalUse(word))
