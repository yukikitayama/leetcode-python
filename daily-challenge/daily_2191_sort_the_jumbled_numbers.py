from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_num_index = []

        for i in range(len(nums)):
            curr_num = nums[i]

            # Edge case
            if curr_num == 0:
                mapped_num_index.append([mapping[curr_num], i])
                continue

            mapped_num = 0
            place = 1

            while curr_num != 0:
                mapped_num += place * mapping[curr_num % 10]
                place *= 10
                curr_num //= 10

            mapped_num_index.append([mapped_num, i])

        mapped_num_index.sort()
        ans = [nums[i] for _, i in mapped_num_index]
        return ans

    def sortJumbled1(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_num_index = []
        for i in range(len(nums)):
            curr = []
            for digit_str in str(nums[i]):
                mapped_digit_str = str(mapping[int(digit_str)])
                curr.append(mapped_digit_str)
            mapped_num_index.append([int("".join(curr)), i])

        mapped_num_index.sort()
        # print(mapped_num_index)

        ans = []
        for mapped_num, i in mapped_num_index:
            ans.append(nums[i])
        return ans
