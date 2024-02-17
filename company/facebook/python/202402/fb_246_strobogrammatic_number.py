"""
0 -> 0
1 -> 1
6 -> 9
8 -> 8
9 -> 6

two pointers towards center from edges
  until left <= right break
    if left is right
      center character needs to be, 0, 1, 8
convert left charcater by hashmap
if not same character return false

after iteration, return true
"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        converter = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }

        left = 0
        right = len(num) - 1

        while left <= right:

            if left == right:
                if num[left] not in ["0", "1", "8"]:
                    return False

            elif num[left] not in converter:
                return False

            elif converter[num[left]] != num[right]:
                return False

            left += 1
            right -= 1

        return True
