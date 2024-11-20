class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = [0] * 3
        for c in s:
            count[ord(c) - ord("a")] += 1

        # Edge
        for i in range(3):
            if count[i] < k:
                return -1

        count_in_window = [0] * 3
        left = 0
        max_window_size = 0
        for right in range(len(s)):

            count_in_window[ord(s[right]) - ord("a")] += 1

            while left <= right and (
                    count[0] - count_in_window[0] < k
                    or count[1] - count_in_window[1] < k
                    or count[2] - count_in_window[2] < k
            ):
                count_in_window[ord(s[left]) - ord("a")] -= 1
                left += 1

            max_window_size = max(
                max_window_size,
                right - left + 1
            )

        return len(s) - max_window_size