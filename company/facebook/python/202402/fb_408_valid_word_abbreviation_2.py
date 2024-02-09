class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i = 0
        j = 0

        while i < len(word) and j < len(abbr):

            # Number
            if abbr[j].isnumeric():

                # Leading zero is not allowed
                if abbr[j] == "0":
                    return False

                num = 0

                while j < len(abbr) and abbr[j].isnumeric():
                    num = num * 10 + int(abbr[j])
                    j += 1

                i += num

            # Character
            else:

                if word[i] == abbr[j]:
                    i += 1
                    j += 1

                else:
                    return False

        return i == len(word) and j == len(abbr)


if __name__ == "__main__":
    word = "internationalization"
    abbr = "i12iz4n"
    word = "apple"
    abbr = "a2e"
    word = "a"
    abbr = "01"
    print(Solution().validWordAbbreviation(word, abbr))


