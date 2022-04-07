"""
- Only even integers
"""


from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        ans = []
        curr_even = 2
        if finalSum % 2 == 0:
            while curr_even <= finalSum:
                ans.append(curr_even)
                finalSum -= curr_even
                curr_even += 2

            # print(f'finalSum: {finalSum}, ans: {ans}, curr_even: {curr_even}')

            # Here
            # curr_even > finalSum
            # ans[-1] <= finalSum
            # so finalSum could be == ans[-1]
            # but we cannot make any more unique integer less than the remaining finalSum
            # so add the remaining to the largest integer in the answer list

            ans[-1] += finalSum

        return ans


if __name__ == '__main__':
    finalSum = 12
    # [2, 4, 6]
    finalSum = 28
    # [6, 8, 2, 12]
    print(Solution().maximumEvenSplit(finalSum))
