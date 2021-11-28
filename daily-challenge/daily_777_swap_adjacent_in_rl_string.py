class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False

        if start.replace('X', '') != end.replace('X', ''):
            return False

        n = len(start)
        l_starts = [i for i in range(n) if start[i] == 'L']
        l_ends = [i for i in range(n) if end[i] == 'L']
        r_starts = [i for i in range(n) if start[i] == 'R']
        r_ends = [i for i in range(n) if end[i] == 'R']
        for l_start, l_end in zip(l_starts, l_ends):
            # l_end index should be smaller because l goes to left in replacing, otherwise strange
            if l_start < l_end:
                return False

        for r_start, r_end in zip(r_starts, r_ends):
            # r_end index should be larger because r goes to right in replace,
            if r_end < r_start:
                return False

        return True


start = "RXXLRXRXL"
end = "XRLXXRRLX"
start = "X"
end = "L"
print(Solution().canTransform(start, end))
