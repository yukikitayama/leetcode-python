import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        max_count = max(counter.values())
        buckets = [[] for _ in range(max_count + 1)]
        for k, v in counter.items():
            buckets[v].append(k)

        # print(buckets)

        ans = []
        for i in range(len(buckets) - 1, -1, -1):
            chars = buckets[i]
            for char in chars:
                ans.append(char * i)

        return ''.join(ans)


class Solution1:
    def frequencySort(self, s: str) -> str:

        counter = collections.Counter(s)
        ans = sorted(counter.keys(), key=lambda x: -counter[x])
        # print(ans)
        return ''.join([a * counter[a] for a in ans])


if __name__ == '__main__':
    s = 'tree'
    # s = 'cccaaa'
    print(Solution().frequencySort(s))
