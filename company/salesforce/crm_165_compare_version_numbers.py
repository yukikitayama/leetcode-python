from typing import List


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)

        while p1 < n1 or p2 < n2:
            i1, p1 = self.get_next_chunk(version1, n1, p1)
            i2, p2 = self.get_next_chunk(version2, n2, p2)

            if i1 != i2:
                return 1 if i1 > i2 else -1

        return 0

    def get_next_chunk(self, version: str, n: int, p: int) -> List[int]:

        # End
        # get_next_chunk() returns next chunk beginning index as the second element in return
        # so p will be (n - 1) + 1
        # so by returning 0 to treat the version as 0 if version number is not specified (length is shorter)
        if p > n - 1:
            # print(f'    version: {version}, p: {p}')
            return [0, p]

        # Find the end of chunk
        p_end = p
        while p_end < n and version[p_end] != '.':
            p_end += 1

        # Retrieve chunk
        i = int(version[p:p_end])

        # Beginning of the next chunk
        p = p_end + 1
        return [i, p]


class Solution1:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = version1.split('.')
        list2 = version2.split('.')

        # print(f'version1: {list1}')
        # print(f'version2: {list2}')

        for i in range(max(len(list1), len(list2))):
            i1 = int(list1[i]) if i < len(list1) else 0
            i2 = int(list2[i]) if i < len(list2) else 0

            if i1 != i2:
                return 1 if i1 > i2 else -1

        return 0


version1 = "1.01"
version2 = "1.001"
version1 = '1.0'
version2 = '1.0.0'
print(Solution().compareVersion(version1, version2))
