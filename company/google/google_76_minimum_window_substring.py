from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = Counter(t)
        # print(f'dict_t: {dict_t}')

        num_unique_t = len(dict_t)
        # print(f'num_unique_t: {num_unique_t}')

        l, r = 0, 0

        # Track the number of unique character from t in current window
        num_unique_s_for_t = 0

        # Tracks count of all the unique characters
        window_counts = {}

        # ans is tuple
        ans = float('inf'), None, None

        while r < len(s):
            # print('In while 1')

            character = s[r]
            # print(f'character: {character}')
            # If the character doesn't exist in dict, 0
            window_counts[character] = window_counts.get(character, 0) + 1
            # print(f'window_counts: {window_counts}')

            # formed won't increment with the character in window which doesn't exist in t
            if character in dict_t and window_counts[character] == dict_t[character]:
                num_unique_s_for_t += 1

            # print(f'num_unique_s_for_t: {num_unique_s_for_t}')

            # With second condition True, window contains substring including characters in t
            # But we don't know whether it's minimum length
            while l <= r and num_unique_s_for_t == num_unique_t:
                # print(f'In while 2')
                character = s[l]
                # print(f'character: {character}')

                # r - l + 1 is window size
                # Save window size before contract the window size
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                # print(f'ans: {ans}')

                # Decrement before move left pointer
                window_counts[character] -= 1

                # Check if the window still contain all the t character and number of t character
                # If characters in window is not enough for t, decrement num_unique_s_for_t
                # and break out of this answer updating inner while loop, because it's not qualified
                if character in dict_t and window_counts[character] < dict_t[character]:
                    num_unique_s_for_t -= 1

                # print(f'num_unique_s_for_t: {num_unique_s_for_t}')
                l += 1

            r += 1

        return '' if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]


"""
Time complexity
Let S be the length of s and T be the length of t.
In worst case, first right pointer scan from most left to most right, and
left pointer scan from most left to most right, so
O(S + T)

Space complexity
O(S)
"""


s = "ADOBECODEBANC"
t = "ABC"
# s = "ADOBECODEBANCC"
# t = "ABCC"
print(f's: {s}, t: {t}')
print(Solution().minWindow(s, t))
