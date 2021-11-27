"""
- ord() to each letter in letters
  - if find bigger, return
  - if reaching the end of array, not yet return, return the first element

- Time is O(n), but it will be improved into O(logn) by binary search
"""


from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]
