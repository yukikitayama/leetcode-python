class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case
        if len(s1) > len(s2):
            return False

        s1map = [0] * 26
        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord('a')] += 1

        # print(f's1map: {s1map}')

        # Make permutation from s2
        for i in range(len(s2) - len(s1) + 1):
            s2map = [0] * 26
            for j in range(len(s1)):
                s2map[ord(s2[i + j]) - ord('a')] += 1

            # print(f'  s2map: {s2map}')
            if self.matches(s1map, s2map):
                return True

        return False

    def matches(self, s1map, s2map):
        for i in range(26):
            if s1map[i] != s2map[i]:
                return False
        return True


class Solution6:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case
        if len(s1) > len(s2):
            return False

        s1map = [0] * 26
        s2map = [0] * 26

        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord('a')] += 1
            s2map[ord(s2[i]) - ord('a')] += 1

        print(f's1map: {s1map}')
        print(f's2map: {s2map}')

        count = 0
        for i in range(26):
            if s1map[i] == s2map[i]:
                count += 1




if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    print(Solution().checkInclusion(s1, s2))
