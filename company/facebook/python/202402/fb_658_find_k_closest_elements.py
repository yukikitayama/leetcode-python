"""
Binary search to find x in arr
  if x is outside of leftmost,
    return array from beginning to kth element
  if x is outside of rightmost
    return array from end to kth element
      arr: [1, 2, 3, 4], k: 2, x: 5, ans: [3, 4]
      bisect_left(arr, x): 4?
Use two pointers to expand range until the range contains k elements
  When expand, always start from left pointer to expand
    This satifies a is closer than b condition
Use two pointers to extract answer array from arr

Edge
  if k is 1, return arr at binary search index
"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        index_x = bisect.bisect_left(arr, x)

        # Edge case
        if index_x == 0:
            return arr[0:k]
        elif index_x == len(arr):
            return arr[-k:]
        elif k == 1:
            return [arr[index_x]]

        # eg arr: [0,1,1,1,2,3,6,7,8,9], x: 4
        if arr[index_x] > x:
            index_x -= 1

        left = index_x
        right = index_x
        # For current element
        k -= 1

        while 0 <= left and right < len(arr):
            if left > 0:
                left -= 1
            else:
                right += 1
            k -= 1

            if k == 0:
                break

            if right < len(arr) - 1:
                right += 1
            else:
                left -= 1
            k -= 1

            if k == 0:
                break

        print(left, right)

        return arr[left:right + 1]
