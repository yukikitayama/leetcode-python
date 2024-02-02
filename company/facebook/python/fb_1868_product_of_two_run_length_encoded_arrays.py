"""
- Expand both
- Iterate both and product
- Compress product into run-length encoded way

- Two pointers
"""


from typing import List


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        ans = []
        idx1 = 0
        idx2 = 0

        while idx1 < len(encoded1) and idx2 < len(encoded2):

            # Get current values and frequencies
            val1, freq1 = encoded1[idx1]
            val2, freq2 = encoded2[idx2]

            # Compute current product
            val_product = val1 * val2
            freq_product = min(freq1, freq2)

            # Overwrite the given lists to indicate that we used up some of it by product
            encoded1[idx1][1] -= freq_product
            encoded2[idx2][1] -= freq_product

            # If used up frequency, move forward index
            if encoded1[idx1][1] == 0:
                idx1 += 1
            if encoded2[idx2][1] == 0:
                idx2 += 1

            # If first time to append to answer or we got the different product value
            if not ans or ans[-1][0] != val_product:
                ans.append([val_product, freq_product])
            # Otherwise modify recorded frequency
            else:
                ans[-1][1] += freq_product

        return ans


if __name__ == '__main__':
    encoded1 = [[1, 3], [2, 3]]
    encoded2 = [[6, 3], [3, 3]]
    print(Solution().findRLEArray(encoded1, encoded2))
