"""
map
0 -> 0
1 -> 1
2 -> 5?
5 -> 2?
6 -> 9
8 -> 8
9 -> 6

"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        if len(num) == 1 and num not in ['0', '1', '8']:
            return False

        map_ = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        for i in range(len(num) // 2 + 1):

            if num[i] not in map_ or map_[num[i]] != num[-(i + 1)]:
                return False

        return True


if __name__ == '__main__':
    num = '69'
    num = '88'
    num = '962'
    num = '205'
    num = '101'
    num = '2'
    num = '8'
    num = '25'
    print(Solution().isStrobogrammatic(num))
