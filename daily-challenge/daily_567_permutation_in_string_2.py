class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Edge case
        if len(s1) > len(s2):
            return False

        s1map = [0] * 26
        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord('a')] += 1

        # print(s1map)
        # print(len(s2) - len(s1))

        # i is starting index of each substring of s2
        for i in range(len(s2) - len(s1) + 1):

            print(f'i: {i}')

            s2map = [0] * 26

            # j is index to scan the substring of s2 for the s1 length
            for j in range(len(s1)):

                print(f'  j: {j}')

                # Find substring of s2 and count characters for permutation
                s2map[ord(s2[i + j]) - ord('a')] += 1

            print(f'  s2map: {s2map}')

            if self.match(s1map, s2map):
                return True

        return False

    def match(self, s1map, s2map):
        for i in range(26):
            if s1map[i] != s2map[i]:
                return False
        return True


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"

    s1 = "adc"
    s2 = "dcda"
    # True

    print(Solution().checkInclusion(s1, s2))
