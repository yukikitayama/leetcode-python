from typing import List
import collections


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        queue = collections.deque(tokens)

        ans = 0
        curr_score = 0

        while queue and power >= queue[0]:

            # If power is at least tokens[i]
            while queue and power >= queue[0]:

                # Get token from the left of the queue because we wanna minimize losing power
                token = queue.popleft()

                # Lose power
                power -= token

                # Gain score
                curr_score += 1

            ans = max(ans, curr_score)

            # If current score is at least 1
            # if queue because we need to have a token to play
            if queue and curr_score >= 1:

                # Get token from the right of the queue to gain max power
                token = queue.pop()

                # Gain power
                power += token

                # Lose score
                curr_score -= 1

        return ans


if __name__ == '__main__':
    tokens = [100, 200, 300, 400]
    power = 200
    print(Solution().bagOfTokensScore(tokens, power))
