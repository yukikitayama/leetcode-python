from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        # Initialize sum_ as sum of even numbers
        sum_ = sum(num for num in nums if num % 2 == 0)

        ans = []

        for val, index in queries:

            # We update the sum_ only when the current number is even
            # Okay to remove the amount of even number because if that number stays even
            # after a query, we will add back in
            if nums[index] % 2 == 0:
                sum_ -= nums[index]

            # Query is always exercised
            nums[index] += val

            if nums[index] % 2 == 0:
                sum_ += nums[index]

            ans.append(sum_)

        return ans


class Solution1:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        ans = []

        for query in queries:

            val, index = query

            nums[index] += val

            curr = 0

            for num in nums:

                if num % 2 == 0:

                    curr += num

            ans.append(curr)

        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    # [8, 6, 2, 4]
    # nums = [1]
    # queries = [[4, 0]]
    # [0]
    print(Solution().sumEvenAfterQueries(nums, queries))
