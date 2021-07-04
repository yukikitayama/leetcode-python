class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0

        nums = self.radix_sort(nums)

        answer = 0
        for i in range(len(nums) - 1):
            answer = max(nums[i + 1] - nums[i], answer)

        return answer

    def radix_sort(self, arr):
        max_arr = max(arr)

        # Tracks which digit from the right we are currently
        exp = 1

        while max_arr / exp > 0:
            self.counting_sort(arr, exp)
            exp *= 10

        return arr

    def counting_sort(self, arr, exp):
        n = len(arr)

        # This output list will be the sorted list
        output = [0] * n

        count = [0] * 10

        # This counts how many we have to corresponding digit
        # e.g.
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # [0, 2, 0, 0, 1, 0, 0, 0, 0, 0] means we have 2 ones and 1 four
        for i in range(0, n):
            index = arr[i] / exp
            count[int(index % 10)] += 1

        # count list now shows position index in the output list
        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] / exp
            output[count[int(index % 10)] - 1] = arr[i]
            count[int(index % 10)] -= 1
            i -= 1

        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]


nums = [3, 6, 9, 1]
# nums = [10]
sol = Solution()
answer = sol.maximumGap(nums)
print(f'Answer: {answer}')
