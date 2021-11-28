class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # We could have different length. We can't make anagram, so return False immedietely
        if len(s) != len(t):
            return False

        # English has 26 letters, initialized with 0 counts
        counter = [0] * 26
        for i in range(len(s)):
            # ord converts a character to number,
            # e.g. ord('a') - ord('a') = 0, ord('b') - ord('a') = 1
            counter[ord(s[i]) - ord('a')] += 1
            # Decrement as well as increment, so we expect every characters is 0 if they are anagram after the for loop
            counter[ord(t[i]) - ord('a')] -= 1

        # Check each counter is 0 or not
        for count in counter:
            if count != 0:
                return False

        return True


"""
Time complexity
Let n the length of s and t. Counting takes O(n). Checking whether a counter is 0 or not takes O(n)
O(n) + O(n) = O(2N) = O(n)

Space complexity
We use space for counter. No matter how long s and t are going to be, counter length does not change because of English letters
so O(1) constant
"""


s = "anagram"
t = "nagaram"
s = "rat"
t = "car"
print(Solution().isAnagram(s, t))
