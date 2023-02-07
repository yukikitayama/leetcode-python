from typing import List
import collections


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        basket = collections.defaultdict(int)
        ans = 0
        left = 0

        for right in range(len(fruits)):

            basket[fruits[right]] += 1

            # print(f'left: {left}, right: {right}, basket: {basket}')

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

                # print(f'  left: {left}, right: {right}, basket: {basket}')

            ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    print(Solution().totalFruit(fruits))
