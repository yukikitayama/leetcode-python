from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str = min(strs, key=len)

        print(f'shortest_str: {shortest_str}')

        for i, char in enumerate(shortest_str):
            for other in strs:
                if other[i] != char:
                    # Stop expanding shortest string once we find a different character
                    return shortest_str[:i]
        # If shortest string is shared by all the str in strs
        return shortest_str


strs = ["flower", "flow", "flight"]
strs = ["dog","racecar","car"]
print(Solution().longestCommonPrefix(strs))
print(min(strs))

