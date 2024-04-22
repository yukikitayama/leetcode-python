class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_set = set()
        upper_set = set()

        for i in range(len(word)):

            if word[i].islower():
                lower_set.add(word[i])
            elif word[i].isupper():
                upper_set.add(word[i].lower())

        return len(lower_set.intersection(upper_set))
