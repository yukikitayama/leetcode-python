from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        # Implement binary tree by an array
        if len(nums) > 0:
            n = len(nums)
            # tree[0] won't be used/ tree[1] is the top of the binary tree
            self.tree = [0] * (2 * n)
            self.n = n

            # print(f'tree before build_tree:')
            # print(self.tree)

            self.build_tree(nums)

    def update(self, index: int, val: int) -> None:
        # For printing
        tmp_index = index

        # The raw data is in the second half of the array binary tree, so += n
        index += self.n
        # Update a value by index
        self.tree[index] = val

        # print(f'Update with array tree index: {index} and val: {val}')
        # print(self.tree)

        # Rebuild binary tree
        while index > 1:
            left = index
            right = index

            # If the index is even, update index for 2*i + 1 (right)
            if index % 2 == 0:
                right = index + 1
            # If the index is odd, update index for 2*i (left)
            else:
                left = index - 1

            self.tree[index // 2] = self.tree[left] + self.tree[right]

            # print(f'index // 2: {index // 2}, left: {left}, right: {right}')

            index //= 2

        # print(f'Rebuilt binary tree array with index: {tmp_index} and val: {val}')
        # print(self.tree)

        return None

    def sumRange(self, left: int, right: int) -> int:
        # +n to go to the raw data part in binary tree array
        # Get leaf value of left and right. After that, we get sum by bottom-up
        left += self.n
        right += self.n

        # print(f'sumRange before while loop with left: {left} and right: {right}')

        sum = 0

        while left <= right:
            # If left is the left child of its parent, left % 2 is 0
            if left % 2 == 1:
                # If current left is right child, we don't need parent value
                # so add tree[left] to sum
                sum += self.tree[left]
                # Go to lower level in binary tree and be left child
                left += 1

            # If right is the right child of its parent, right % 2 is 1
            if right % 2 == 0:
                # In this case, right is the left child of its parent
                sum += self.tree[right]
                # Decrement it to be right child
                right -= 1

            # Go to higher level
            left //= 2
            right //= 2

        return sum

    def build_tree(self, nums: List[int]):
        # Second half of array format binary tree contains the raw data
        i = len(nums)
        j = 0
        while i < 2 * len(nums):
            self.tree[i] = nums[j]
            i += 1
            j += 1

        # print(f'tree after while loop:')
        # print(self.tree)

        # First half of array format binary tree contains the aggregated values
        i = len(nums) - 1
        while i > 0:
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
            i -= 1

        # print(f'tree after second while loop:')
        # print(f'Initialized the binary tree with sum node')
        # print(self.tree)


"""
Time: 
Let n be the length of nums. Initialization takes O(n), update() and sumRange() takes O(logn) 
because it uses binary tree

Space: 
O(n) for binary tree
"""


nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))
# obj.update(1, 4)
# obj.update(2, 2)
