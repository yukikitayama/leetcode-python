"""
- Initialize ans to 0
- Initialize left and right to 0
- Curernt is left,
  - If the next has two rights, no need to insert
- Current is right,
  - If the next is right, and previouly there was left, no need to insert
  - If left is 0 and next is right, increment ans by 1
  - If left is 0 and next is not right, increment ans by 2


- Count
- Position
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        i = 0
        open = 0
        ans = 0

        while i < len(s):

            if s[i] == '(':
                open += 1
                i += 1

            else:
                cur = i

                # e.g. ()), i: 1, while: T, i: 2, while: T, i: 3, while: F
                # e.g. ())))(, i: 1, ... i: 5, while: F
                # When getting out of while loop, i is the index after )
                while i < len(s) and s[i] == ')':
                    i += 1

                # closing_ct is the length of valid closing '))'
                # e.g. closing_ct: 2, there's one valid closing
                # e.g. closing_ct: 4, there are two valid closings
                # cur: 1, i: 3, closing_ct: 2
                # cur: 1, i: 5, closing_ct: 4
                closing_ct = i - cur

                # // 2 because 2 )s makes one closing
                if closing_ct // 2 >= open:

                    # ans won't be incremented if one ( and two )
                    # but e.g. one (, four ), increment ans
                    ans += closing_ct // 2 - open

                    # if the length of ')' is odd, the above leaves one ),
                    # so need to append ( and )
                    if closing_ct % 2 != 0:
                        ans += 2

                    open = 0

                    # No need to update itration index i because the above while
                    # loop already updated

                # If currently it has more openings than closings
                else:

                    # Decrement open by whatver amount of closings it has
                    open -= closing_ct // 2

                    # If the length of closing was odd, the above leaves one ) and
                    # additional (, so we can finish opening by inserting one )
                    if closing_ct % 2 != 0:
                        open -= 1
                        ans += 1

        # If at the end open remains, insert the double amount of )s to close it
        ans += open * 2
        return ans


"""
open: 2, closing_ct: 3, closing_ct // 2: 1, 
open -= closing_ct // 2: open -= 1, open: 1,
closing_ct % 2: 1, 
"""

s = "(()))"
print(Solution().minInsertions(s))


