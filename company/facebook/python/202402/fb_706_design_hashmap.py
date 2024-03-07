"""
array to
"""


class Bucket:
    def __init__(self):
        # [(k, v), ...]
        self.bucket = []

    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i in range(len(self.bucket)):
            if key == self.bucket[i][0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i in range(len(self.bucket)):
            if key == self.bucket[i][0]:
                # T: O(N)
                del self.bucket[i]
                break

        # for i, kv in enumerate(self.bucket):
        #     if key == kv[0]:
        #         del self.bucket[i]


class MyHashMap:

    def __init__(self):
        self.key_space = 2069
        self.hash_table = [Bucket() for _ in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        hash_ = key % self.key_space
        self.hash_table[hash_].update(key, value)

    def get(self, key: int) -> int:
        hash_ = key % self.key_space
        return self.hash_table[hash_].get(key)

    def remove(self, key: int) -> None:
        hash_ = key % self.key_space
        self.hash_table[hash_].remove(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)