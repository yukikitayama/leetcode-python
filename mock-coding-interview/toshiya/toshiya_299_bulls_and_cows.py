import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counter_secret = collections.Counter(secret)
        counter_guess = collections.Counter(guess)

        # Bull operation
        bulls = 0
        for i in range(len(secret)):

            if secret[i] == guess[i]:
                bulls += 1

                counter_secret[secret[i]] -= 1
                if counter_secret[secret[i]] == 0:
                    del counter_secret[secret[i]]
                counter_guess[secret[i]] -= 1
                if counter_guess[secret[i]] == 0:
                    del counter_guess[secret[i]]

        # Cow operation
        cows = 0
        for k, v in counter_guess.items():

            if k in counter_secret:
                cows += min(counter_secret[k], counter_guess[k])

        return str(bulls) + "A" + str(cows) + "B"


