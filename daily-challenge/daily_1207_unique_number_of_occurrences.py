class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        return len(set(counter.keys())) == len(set(counter.values()))