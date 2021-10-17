"""
Algorithm
- split s into a list
- Initialize ans empty list
- Iterate each word in the list
  - reverse it
  - append it
- join the list with ' '

Complexity
- Let n be the number of word in s
- Time is O(n) to split, O(n) to iterate each word, O(n) to join it
- Space is O(2n) for word list and reversed list
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        ans = []
        for word in s_list:
            ans.append(word[::-1])

        ans = ' '.join(ans)
        return ans


s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))
