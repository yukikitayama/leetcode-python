import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        counter = collections.Counter(t)
        required = len(counter)

        left = 0
        right = 0
        window = collections.defaultdict(int)
        formed = 0
        ans = [float("inf"), None, None]

        while right < len(s):

            curr_char = s[right]

            window[curr_char] += 1

            if curr_char in counter and window[curr_char] == counter[curr_char]:
                formed += 1

            # Contract
            while left <= right and formed == required:

                left_char = s[left]

                if right - left + 1 < ans[0]:
                    ans = [right - left + 1, left, right]

                # Update window information before contracting
                window[left_char] -= 1
                if left_char in counter and window[left_char] < counter[left_char]:
                    formed -= 1
                left += 1

            # Expand
            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]