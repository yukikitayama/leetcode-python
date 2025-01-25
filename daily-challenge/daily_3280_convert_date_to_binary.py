"""
bin()

T: O(1), S: O(1)
"""


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # T: O(10)
        nums = date.split("-")
        ans = []
        # T: O(3)
        for num in nums:
            bin_num = bin(int(num))
            # 0bXXXX
            ans.append(bin_num[2:])
        # T: O(3)
        return "-".join(ans)
