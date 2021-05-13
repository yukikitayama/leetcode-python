class Solution:
    def runningSum(self, nums):
        running_sum = []

        for i in range(1, len(nums) + 1):
            print(f'nums[0:i]: {nums[0:i]}')
            total = sum(nums[0:i])
            running_sum.append(total)

        return running_sum

"""
[1, 2, 3, 4]
[1, 3, 6, 10]
"""
test_case = [1, 2, 3, 4]
sol = Solution()
answer = sol.runningSum(test_case)
print(f'Answer: {answer}')
