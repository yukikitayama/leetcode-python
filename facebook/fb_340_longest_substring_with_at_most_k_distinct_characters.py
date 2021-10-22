import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        # if s is empty or asking k: 0 distinct substring, it's impossible so return 0
        if n * k == 0:
            return 0

        left = 0
        right = 0

        hashmap = collections.defaultdict()
        # It's safe to initialize answer to be 1,
        # because the above already checked the length 0 case
        max_len = 1

        while right < n:

            hashmap[s[right]] = right
            right += 1

            # if it observed more than k distinct characters, remove it
            if len(hashmap) == k + 1:
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]

                left = del_idx + 1

            # No need to +1 to the difference between right and left
            # because when substring length is 1, right index is already 1 and left index is 0
            max_len = max(max_len, right - left)

        return max_len


s = "eceba"
k = 2
s = "aa"
k = 1
print(Solution().lengthOfLongestSubstringKDistinct(s, k))


