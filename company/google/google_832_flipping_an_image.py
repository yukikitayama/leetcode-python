from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        for row in image:
            # n: 2, (n + 1) // 2: 1
            # n: 3, (n + 1) // 2: 2
            # n + 1 because we wanna access mid element too when row is odd length
            # flip doesn't matter, but we wanna invert it
            for i in range((n + 1) // 2):

                # print(f'i: {i}')

                # Flip by A, B = B, A
                # Invert by ^1
                # 1^1: 0, 0^1: 1
                row[i], row[n - 1 - i] = row[n - 1 - i] ^ 1, row[i] ^ 1

        return image


if __name__ == '__main__':
    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    # [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
    print(Solution().flipAndInvertImage(image))
