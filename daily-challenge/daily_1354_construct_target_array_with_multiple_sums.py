import heapq


class Solution:
    def isPossible(self, target):

        # Edge case, when length of target is 1, [1] is only possible
        if len(target) == 1:
            return target == [1]

        total = sum(target)

        print(f'First total: {total}')

        # Python heapq is by default min-heap. We can have max-heap if we multiply -1 to each element
        max_heap = [-num for num in target]
        # Make max-heap
        heapq.heapify(max_heap)

        [print(i) for i in max_heap]
        print()

        # If the max in the max heap is negative, it's not possible. Multiply -1 because we store element by negative
        # values
        while -max_heap[0] > 1:

            # First element is max value, multiply -1 because it's stored as negative values
            max_value = -max_heap[0]

            sum_of_rest = total - max_value

            # Edge case
            if sum_of_rest == 1:
                return True

            # Get x by subtract sum except the max value (- (total - max_value)) from the max value
            # x = max_value - (total - max_value)
            x = max_value % sum_of_rest

            # We break [1, 1, ..., 1], so it's not possible
            # if x < 1:
            #     return False

            # x == max_value means if x didn't change
            if x == 0 or x == max_value:
                return False

            # heapq.heapreplace pops and returns the smallest item from the heap, and push the new item
            # We want to replace max value in max heap. We store elements as negative values. So max value is the smallest
            # value in the heap. So by heapq.heapreplace, we can replace max value in the max heap with the new max.
            heapq.heapreplace(max_heap, -x)

            [print(i) for i in max_heap]
            print()

            # Update sum of each element in target, by the previous max value (max_value) vanished but we pushed the new max
            # (x)
            total = total - max_value + x
            print(f'Updated total: {total}')

        return True


def main():

    # Test
    """
    test case: [1, 7, 13, 43]
    max heap: [43, 7, 13, 1]

    [1, 7, 13, x] -> [1, 7, 13, 43]
    43 = 1 + 7 + 13 + x
    x = 43 - 1 - 7 - 13
      = 43 - 21
      = 22
    """
    target = [1, 7, 13, 43]
    solution = Solution()
    answer = solution.isPossible(target=target)
    print(f'Answer: {answer}')

    target = [1, 5, 998]
    answer = solution.isPossible(target=target)
    print(f'Answer: {answer}')


if __name__ == '__main__':
    main()
