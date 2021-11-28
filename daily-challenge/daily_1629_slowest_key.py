from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        # Key: Key, value: duration pressed
        key_to_duration = {}
        # First item no need to get time by taking difference, so directly put into
        key_to_duration[keysPressed[0]] = releaseTimes[0]

        for i in range(1, len(releaseTimes)):
            # Get pressed duration time
            curr_duration = releaseTimes[i] - releaseTimes[i - 1]
            curr_key = keysPressed[i]
            # We can have the same key multiple times. Need to update with the longest duration
            key_to_duration[curr_key] = max(key_to_duration.get(curr_key, 0), curr_duration)

        # Initialize for making answer
        answer = ''
        longest = 0

        # Key: pressed key, value: duration pressed
        for key, value in key_to_duration.items():
            if value > longest:
                longest = value
                answer = key
            # we can have multiple same length durations, but we need to return lexicographically bigger
            # below if key: 'b', answer: 'a', it's True
            elif value == longest and key > answer:
                answer = key

        return answer


releaseTimes = [9,29,49,50]
keysPressed = "cbcd"
releaseTimes = [12,23,36,46,62]
keysPressed = "spuda"
print(Solution().slowestKey(releaseTimes, keysPressed))
