class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        i = 0
        while i < len(word):
            count = 0
            curr = word[i]

            while i < len(word) and count < 9 and word[i] == curr:
                count += 1
                i += 1

            comp.append(str(count))
            comp.append(curr)

        return "".join(comp)