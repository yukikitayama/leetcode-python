"""
"""


from typing import List
import collections


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        word_to_index = collections.defaultdict(int)
        for i, word in enumerate(list1):
            word_to_index[word] = i

        # print(f'{word_to_index}')

        ans = []
        min_sum = float('inf')
        i = 0
        while i < len(list2) and i <= min_sum:
            if list2[i] in word_to_index:
                sum_ = i + word_to_index[list2[i]]
                if sum_ < min_sum:
                    # Clear the list first because we found smaller
                    # otherwise the list contains older word which had small sum but not as small as the current sum
                    ans = []
                    ans.append(list2[i])
                    min_sum = sum_
                elif sum_ == min_sum:
                    ans.append(list2[i])
            i += 1

        return ans


"""
- Time is O(2n) = O(2)
- Space is O(n) for the hashmap
"""


list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# ['Shogun']
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
# ['Shogun']
print(Solution().findRestaurant(list1, list2))



