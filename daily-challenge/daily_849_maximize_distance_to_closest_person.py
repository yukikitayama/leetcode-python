from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        people = (i for i, seat in enumerate(seats) if seat == 1)

        # print(f'people: {people}')

        # Previous index whose seat is occupied
        prev = None
        # Next index whose seat is occupied
        future = next(people)

        # print(f'prev: {prev}, future: {future}')

        ans = 0

        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                # future < i because if future is behind current i, future needs to be updated to
                # be the future index
                while future is not None and future < i:
                    # None is returned if the iterator is exhausted
                    future = next(people, None)

                # i - prev is the distance between current and left occupied seat
                left = float('inf') if prev is None else i - prev
                # future - i is the distance between current and right occupied seat
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))

                # print(f'  left: {left}, right: {right}')

            # print(f'i: {i}, seat: {seat}, prev: {prev}, future: {future}')

        return ans


class Solution1:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        # [n] for min() at the end
        # [0] won't work
        left = [n] * n
        right = [n] * n

        for i in range(n):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i - 1] + 1

        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < n - 1:
                right[i] = right[i + 1] + 1

        print(f'left: {left}')
        print(f'right: {right}')

        return max(min(left[i], right[i]) for i, seat in enumerate(seats) if seat == 0)


if __name__ == '__main__':
    seats = [1, 0, 0, 0, 1, 0, 1]
    # 2
    # seats = [1, 0, 0, 0]
    # 3
    seats = [0, 0, 0, 1, 0, 1]
    print(Solution().maxDistToClosest(seats))
