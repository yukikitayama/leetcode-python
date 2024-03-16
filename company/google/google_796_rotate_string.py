class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            # Python string slicing is T: O(N)
            # so this solution is T: O(N**2) overall
            if s[i:] + s[:i] == goal:
                return True
        return False
