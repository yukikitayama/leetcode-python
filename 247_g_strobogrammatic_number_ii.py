from typing import List


class Solution:
    def __init__(self):
        self.odd_mid_candidate = ['0', '1', '8']
        self.even_mid_candidate = ['11', '69', '88', '96', '00']

    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1:
            return self.odd_mid_candidate
        if n == 2:
            return self.even_mid_candidate[:-1]
        # n >= 3 where n is odd, because 3 % 2 = 1 = True
        if n % 2:
            mid_candidate = self.odd_mid_candidate
            edge_numbers = self.findStrobogrammatic(n - 1)
            slicer = n // 2
        # n >= 4 where n is even
        else:
            mid_candidate = self.even_mid_candidate
            edge_numbers = self.findStrobogrammatic(n - 2)
            slicer = n // 2 - 1
        # slicer = (n - 1) // 2
        answers = [edge[:slicer] + can + edge[slicer:] for can in mid_candidate for edge in edge_numbers]

        return answers


print(Solution().findStrobogrammatic(n=1))
print(Solution().findStrobogrammatic(n=2))
print(Solution().findStrobogrammatic(n=3))
print(Solution().findStrobogrammatic(n=4))
print(Solution().findStrobogrammatic(n=5))
