from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:

        # seen contains masks
        # Each mask is binary representation of character presence of each word
        seen = set()
        for word in startWords:
            # Initialize mask
            m = 0

            for ch in word:

                # ord('a'): 97
                m ^= 1 << ord(ch) - 97

                # print(f'bin(m): {bin(m)}, ch: {ch}')

            seen.add(m)

        # [print(bin(s)) for s in seen]

        ans = 0
        for word in targetWords:
            # Initialize mask
            m = 0
            for ch in word:
                m ^= 1 << ord(ch) - 97

            # print(f'bin(m): {bin(m)}')

            # We can rearrange letters so we don't care order of characters in word
            # Just check the presence
            # Remove one character from targetString to check the one-character-remove-word in seen
            for ch in word:
                if m ^ (1 << ord(ch) - 97) in seen:
                    # print(f'ord: {ord(ch) - 97}')
                    # print(f'ans m^(1<<ord(ch-97)): {bin(m ^ (1 << ord(ch) - 97))}')
                    ans += 1
                    break

        return ans


if __name__ == '__main__':
    startWords = ["ant", "act", "tack"]
    targetWords = ["tack", "act", "acti"]
    startWords = ['abc']
    targetWords = ['abcd']
    print(Solution().wordCount(startWords, targetWords))
