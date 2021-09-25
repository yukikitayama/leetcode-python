class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # First ugly number is 1
        ugly = [1]
        i2 = i3 = i5 = 0

        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
                # print(f'i2: {i2}')
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
                # print(f'i3: {i3}')
            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1
                # print(f'i5: {i5}')

            # print(f'ugly[i2] * 2: {ugly[i2] * 2}, '
            #       f'ugly[i3] * 3: {ugly[i3] * 3}, '
            #       f'ugly[i5] * 5: {ugly[i5] * 5}')
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
            # print(f'ugly: {ugly}')

        return ugly[-1]


print(Solution().nthUglyNumber(10))
