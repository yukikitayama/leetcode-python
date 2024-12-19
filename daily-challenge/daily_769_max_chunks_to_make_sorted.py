from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for i in range(len(arr)):

            # New chunk
            if not stack or arr[i] > stack[-1]:
                stack.append(arr[i])

            # Merge chunk
            else:
                max_element = stack[-1]
                while stack and arr[i] < stack[-1]:
                    stack.pop()
                stack.append(max_element)

        return len(stack)