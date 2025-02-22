from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (n * 2 - 1)
        is_number_used = [False] * (n + 1)

        def backtracking(index):
            if index == len(ans):
                return True

            # Move on if current position is already filled
            if ans[index] != 0:
                return backtracking(index + 1)

            for num in range(n, 0, -1):

                # Ignore if this number was already used
                if is_number_used[num]:
                    continue

                # Fill current
                is_number_used[num] = True
                ans[index] = num

                if num == 1:
                    if backtracking(index + 1):
                        return True

                # Use if in the bound and not filled yet
                elif index + num < len(ans) and ans[index + num] == 0:

                    # Fill pair
                    ans[index + num] = num

                    if backtracking(index + 1):
                        return True

                    # Backtrack pair
                    ans[index + num] = 0

                # Backtrack current
                ans[index] = 0
                is_number_used[num] = False

            return False

        backtracking(0)

        return ans