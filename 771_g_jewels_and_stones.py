class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_set = set(jewels)
        return sum(stone in j_set for stone in stones)


"""
Time complexity
Let n the length of jewels, m the length of stones
O(n) to create jewel set, and O(m) to for loop stones, so O(n + m)

Space complexity
O(n) for jewel set
"""


jewels = "aA"
stones = "aAAbbbb"
print(Solution().numJewelsInStones(jewels, stones))
