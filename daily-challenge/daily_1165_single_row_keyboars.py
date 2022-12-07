class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        key_to_index = {k: i for i, k in enumerate(keyboard)}

        curr = 0

        ans = 0

        for ch in word:

            ans += abs(curr - key_to_index[ch])
            curr = key_to_index[ch]

        return ans


if __name__ == '__main__':
    keyboard = "abcdefghijklmnopqrstuvwxyz"
    word = "cba"
    print(Solution().calculateTime(keyboard, word))
