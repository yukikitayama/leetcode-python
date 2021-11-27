"""
- Get intersection
- Get index of the intersected string from each list
  - For loop
  - If min sum updated update the answer
"""


from typing import List
import collections


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        sum_to_word_list = collections.defaultdict(list)
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    sum_to_word_list[i + j].append(list1[i])

        # print(f'sum_to_word_list: {sum_to_word_list}')

        min_sum = min(sum_to_word_list.keys())
        return sum_to_word_list[min_sum]


"""
- Time is O(xyz) by x length list1, y length lis2, z average length of words
- Space is O(xyz) for the hashmap
"""


list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
print(Solution().findRestaurant(list1, list2))



