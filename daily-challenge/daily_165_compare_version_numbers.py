"""
Split by "."
If length 2
  append 0 to left
If lenth 1
  append two 0s to left
Convert all elements to integers
iterate the array
  Do -1 or 1 comparison
If iteration finish,
  return 0

"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        def get_chunk(version, p):
            if p >= len(version):
                return 0, p

            p_end = p
            while p_end < len(version) and version[p_end] != ".":
                p_end += 1

            num = int(version[p:p_end])

            return num, p_end + 1

        p1 = p2 = 0

        while p1 < len(version1) or p2 < len(version2):
            num1, p1 = get_chunk(version1, p1)
            num2, p2 = get_chunk(version2, p2)

            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1

        return 0

    def compareVersion2(self, version1: str, version2: str) -> int:
        array1 = version1.split(".")
        array2 = version2.split(".")

        for i in range(max(len(array1), len(array2))):

            num1 = int(array1[i]) if i < len(array1) else 0
            num2 = int(array2[i]) if i < len(array2) else 0

            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1

        return 0

    def compareVersion1(self, version1: str, version2: str) -> int:

        def convert(version: str, maxlen):
            array = version.split(".")
            diff = maxlen - len(array)
            while diff:
                array = array + ["0"]
                diff -= 1
            array = [int(e) for e in array]
            return array

        maxlen = max(version1.count("."), version2.count(".")) + 1

        array1 = convert(version1, maxlen)
        array2 = convert(version2, maxlen)

        # print(array1)
        # print(array2)

        for i in range(len(array1)):
            if array1[i] < array2[i]:
                return -1
            elif array1[i] > array2[i]:
                return 1

        return 0
