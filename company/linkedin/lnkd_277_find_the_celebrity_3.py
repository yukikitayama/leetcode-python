def knows(a: int, b: int):
    return True


class Solution:
    def findCelebrity(self, n: int) -> int:

        def is_celebrity(i):
            for j in range(n):
                if i == j:
                    continue
                elif knows(i, j) or not knows(j, i):
                    return False
            return True

        celebrity_candidate = 0

        for i in range(1, n):

            if knows(celebrity_candidate, i):
                celebrity_candidate = i

        if is_celebrity(celebrity_candidate):
            return celebrity_candidate
        else:
            return -1


