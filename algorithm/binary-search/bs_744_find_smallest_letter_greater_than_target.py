"""
- Time is O(logN)
- Space is O(1)
- right pointer is len(letters) and while loop end condition is left == right
  because we need to find the smallest
- Because problem says letters wrap around, it needs extra left index post-processing.
"""


from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        # No -1 to len(letters).
        # When len(letters) is 1, the below while loop doesn't run
        right = len(letters)

        # End when left == right. At the end, left is smallest
        while left < right:

            mid = (left + right) // 2

            curr = letters[mid]

            if curr > target:
                right = mid
            else:
                left = mid + 1

        # When target is greater than or equal to the last element in letters,
        # left is len(letters) so it will throw index out of bound error
        if left < len(letters):
            return letters[left]
        # Problem says letters wrap around
        else:
            return letters[0]


if __name__ == '__main__':
    letters = ["c", "f", "j"]
    target = "a"
    # c
    # letters = ["c", "f", "j"]
    # target = "c"
    # f
    letters = ["c", "f", "j"]
    target = "d"
    # f
    letters = ["c", "f", "j"]
    target = "j"
    # c
    # Because the letters wrap around
    print(Solution().nextGreatestLetter(letters, target))
