"""
modify Kadane's algorithm
Update global_max only when minor_count > 0
Reset local_max to 0 only when there is at least one minor in the remaining substring.
  if local_max < 0 and there is still minor in the remaining string, we can reset it to 0 (i.e., reset both minor_count and major_count to 0).
"""


class Solution:
    def largestVariance(self, s: str) -> int:
        counter = [0] * 26
        for ch in s:
            counter[ord(ch) - ord("a")] += 1

        global_max = 0

        # i: Major
        for i in range(26):
            # j: Minor
            for j in range(26):

                # Invalid pairs
                if i == j or counter[i] == 0 or counter[j] == 0:
                    continue

                major_count = 0
                minor_count = 0

                major_char = chr(ord("a") + i)
                minor_char = chr(ord("a") + j)

                rest_minor = counter[j]

                # Kadane's algorithm
                for ch in s:
                    if ch == major_char:
                        major_count += 1

                    if ch == minor_char:
                        minor_count += 1
                        rest_minor -= 1

                    if minor_count > 0:
                        local_max = major_count - minor_count
                        global_max = max(global_max, local_max)

                    # If local max is negative and there are still minor character exist in the remaining string
                    if major_count < minor_count and rest_minor > 0:
                        major_count = 0
                        minor_count = 0

        return global_max
