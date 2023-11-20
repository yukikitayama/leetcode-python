"""
hashmap garbage for each house
iterate travel
"""

from typing import List
import collections


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        prefix_sum = [0] * (len(travel) + 1)
        for i in range(len(travel)):
            prefix_sum[i + 1] = prefix_sum[i] + travel[i]

        garbage_last_i = collections.defaultdict(int)
        garbage_count = collections.Counter()

        for i in range(len(garbage)):

            curr_count = collections.Counter(garbage[i])
            garbage_count = garbage_count + curr_count

            for ch in curr_count.keys():
                garbage_last_i[ch] = i

        # print(f"prefix_sum: {prefix_sum}")
        # print(f"garbage_last_i: {garbage_last_i}")
        # print(f"garbage_count: {garbage_count}")

        ans = 0

        for ch in garbage_count.keys():
            ans += garbage_count[ch]
            ans += prefix_sum[garbage_last_i[ch]]

        return ans


if __name__ == "__main__":
    garbage = ["G", "P", "GP", "GG"]
    travel = [2, 4, 3]
    print(Solution().garbageCollection(garbage, travel))
