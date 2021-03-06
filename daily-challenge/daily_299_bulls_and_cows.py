from collections import Counter
import pprint


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Count a number of each character in string
        h = Counter(secret)
        # pprint.pprint(h)

        bulls = 0
        cows = 0
        for idx, ch in enumerate(guess):
            if ch in h:
                if ch == secret[idx]:
                    bulls += 1
                    # if h[ch] <= 0, before bull we used cow too many times, so decrease number of cows
                    # int(True): 1, int(False): 0
                    cows -= int(h[ch] <= 0)

                else:
                    # if ch exists in ch, counte up cows
                    cows += int(h[ch] > 0)
                # Because counted current ch, so update h
                h[ch] -= 1

        return f'{str(bulls)}A{str(cows)}B'


"""
Time complexity
One pass for making dictionary, another pass for for-loop, so O(2n) = O(n)

Space complexity
O(1) because we keep dictionary and keys are from 0 to 9, at most 10 elements, so O(10) = O(1)
"""


secret = "1807"
guess = "7810"
# secret = "1123"
# guess = "0111"
print(Solution().getHint(secret, guess))
