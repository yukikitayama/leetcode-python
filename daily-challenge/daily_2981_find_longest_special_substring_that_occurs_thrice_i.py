import collections


class Solution:
    def maximumLength(self, s: str) -> int:
        char_len_to_count = collections.Counter()

        for start in range(len(s)):

            curr_char = s[start]
            curr_len = 0

            for end in range(start, len(s)):

                if curr_char == s[end]:
                    curr_len += 1
                    char_len_to_count[(curr_char, curr_len)] += 1

                else:
                    break

        # print(char_len_to_count)

        ans = -1
        for k, v in char_len_to_count.items():
            curr_char = k[0]
            curr_len = k[1]
            if v >= 3 and curr_len > ans:
                ans = curr_len
        return ans