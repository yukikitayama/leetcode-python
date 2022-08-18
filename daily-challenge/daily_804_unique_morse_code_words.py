from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        seen = set()

        for word in words:
            curr = ''
            for ch in word:
                i = ord(ch) - ord('a')
                curr += morse[i]
            seen.add(curr)

        return len(seen)


if __name__ == '__main__':
    words = ["gin", "zen", "gig", "msg"]
    print(Solution().uniqueMorseRepresentations(words))
