from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        sum_stones = sum(stones)

        if sum_stones % 3 == 0 and len(stones) % 2 != 0:
            return False
        elif sum_stones % 3 == 0 and len(stones) % 2 == 0:
            return True
        elif sum_stones % 3 != 0 and len(stones) % 2 != 0:
            return False
        elif sum_stones % 3 != 0 and len(stones) % 2 == 0:
            return True


stones = [5,1,2,4,3]
stones = [2,1]
stones = [2]
stones = [2,3]  # false
print(Solution().stoneGameIX(stones))



