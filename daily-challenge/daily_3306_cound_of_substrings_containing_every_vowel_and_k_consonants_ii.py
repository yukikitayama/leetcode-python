class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def is_vowel(c):
            return c in "aeiou"

        next_consonant = [0] * len(word)
        next_consonant_index = len(word)
        for i in range(len(word) - 1, -1, -1):
            next_consonant[i] = next_consonant_index
            if not is_vowel(word[i]):
                next_consonant_index = i

        # print(next_consonant)

        ans = 0
        start = end = 0
        vowel_count = {}
        consonant_count = 0

        while end < len(word):

            new_letter = word[end]

            if is_vowel(new_letter):
                vowel_count[new_letter] = vowel_count.get(new_letter, 0) + 1
            else:
                consonant_count += 1

            # Need to shrink
            while consonant_count > k:
                start_letter = word[start]
                if is_vowel(start_letter):
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1
                start += 1

            # Count substring
            while start < len(word) and len(vowel_count) == 5 and consonant_count == k:

                # Increment answer by additional vowels
                ans += next_consonant[end] - end

                start_letter = word[start]

                if is_vowel(start_letter):

                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]

                else:
                    consonant_count -= 1

                start += 1

            end += 1

        return ans