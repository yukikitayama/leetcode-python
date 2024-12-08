class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i_s = 0
        i_t = 0

        while i_s < len(start) or i_t < len(target):

            while i_s < len(start) and start[i_s] == "_":
                i_s += 1

            while i_t < len(target) and target[i_t] == "_":
                i_t += 1

            # If one exhausted, the other also needs to exhaust
            if i_s == len(start) or i_t == len(target):
                return i_s == len(start) and i_t == len(target)

            # If not match, false
            if (
                    start[i_s] != target[i_t]
                    or (start[i_s] == "L" and i_s < i_t)
                    or (start[i_s] == "R" and i_s > i_t)
            ):
                return False

            i_s += 1
            i_t += 1

        return True