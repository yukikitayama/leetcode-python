# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        left = 0
        length = reader.length()

        while length > 1:

            length //= 2

            # If length is even, [l:r] and [x:y] have the same number of elements
            # If length is odd, left: 0, length: 3, length //= 2: 1,
            # [l:r] is 0 only, [x:y] is 1 only, and left and right halves still have the same number of elements
            # But the rightmost is excluded if odd
            cmp = reader.compareSub(
                l=left,
                # -1 because original length didn't subtract 1
                r=left + length - 1,
                x=left + length,
                y=left + 2 * length - 1
            )

            # If left half and right half have the same sum, rightmost excluded element is the different number
            if cmp == 0:
                return left + 2 * length

            # If right half contain the target
            elif cmp < 0:
                left += length

            # Why doesn't care cmp > 0?
            # Because right below while statement, we cut half the length
            # so right half is automatically cut

        # When only single element left
        return left

