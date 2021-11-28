from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) == 0 or (r * c != len(mat) * len(mat[0])):
            return mat

        queue = []
        # Row
        for i in range(len(mat)):
            # Column
            for j in range(len(mat[0])):
                queue.append(mat[i][j])

        print(f'queue: {queue}')

        answer = [[0 for _ in range(c)] for _ in range(r)]
        print(f'Before answer: {answer}')

        # Row
        for i in range(r):
            # Column
            for j in range(c):
                answer[i][j] = queue.pop(0)
                print(f'During answer: {answer} with i: {i}, j: {j}, answer[i]: {answer[i]}, queue: {queue}')

        return answer


# mat = [[1,2],[3,4]]
# r = 1
# c = 4
# mat = [[1,2],[3,4]]
# r = 2
# c = 4
mat = [[1,2],[3,4]]
r = 4
c = 1
answer = Solution().matrixReshape(mat, r, c)
for row in answer:
    print(row)
