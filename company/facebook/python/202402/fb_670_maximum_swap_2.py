"""
9793
  9973

9937
  9973

If descending sort
  2736 -> 7632
    because 2 is not 7 at 1st index, swap 2 and 7
      to swap, i need to know 7's index in advance

Hashmap
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        # num_str = list(str(num))
        # digit_to_indices = collections.defaultdict(list)
        # for i in range(len(num_str)):
        #     digit_to_indices[num_str[i]].append(i)

        # desc_sorted_digits = sorted(list(num_str), reverse=True)

        # for i in range(len(num_str)):
        #     if num_str[i] != desc_sorted_digits[i]:
        #         # By popping, move rightmost bigger digit to left
        #         # eg. 9793, we wanna rightmost 9 to 7's place, not swapping with leftmost 9
        #         j = digit_to_indices[desc_sorted_digits[i]].pop()
        #         num_str[i], num_str[j] = num_str[j], num_str[i]
        #         break

        # return int("".join(num_str))

        ans = num
        num_str = list(str(num))

        for i in range(len(num_str)):
            for j in range(i + 1, len(num_str)):
                curr = num_str[:]
                curr[i], curr[j] = curr[j], curr[i]
                curr_num = int("".join(curr))
                ans = max(ans, curr_num)

        return ans