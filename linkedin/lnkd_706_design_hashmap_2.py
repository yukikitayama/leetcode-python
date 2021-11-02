"""
- https://www.youtube.com/watch?v=sfWyugl4JWA
- https://www.youtube.com/watch?v=KyUTuwz_b7Q
- https://medium.com/swlh/why-should-the-length-of-your-hash-table-be-a-prime-number-760ec65a75d1

- Hashmap is the idea that we create index from the given key
- and access the data by the index, not by the key.
- Thus accessing the key is faster
- Time complexity is O(n/m) with n the number of keys and m the size of array
  - Load factor, the ratio
- Closed addressing, or chaining, is adding array or linked list to array

- Hash functions calculate an integer from the key
- To ensure the integer in a range, do the integer % some number

- Use prime number because
  - Every integer that shares a common factor with the number will be
    hashed into an index that is a multiple of this factor.
"""


class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        # If this key is a new key, just append it to the current bucket
        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap:
    def __init__(self):
        # Length of array, large prime number
        self.key_space = 1999
        # Hash table is an array each element having reference pointing at
        # a specific Bucket object
        self.hash_table = [Bucket() for _ in range(self.key_space)]

    def put(self, key, value):
        hash_key = key % self.key_space
        # If the key does not exist in array in Bucket in array at hash_key,
        # then it appends a tuple (key, value) to the array
        # If exist, find the tuple (key, value) in the array in a Bucket,
        # then insert this tuple (key, value) there
        self.hash_table[hash_key].update(key, value)

    def get(self, key):
        hash_key = key % self.key_space
        # If the key does not exist in the array in the Bucket,
        # then it gives us -1
        return self.hash_table[hash_key].get(key)

    def remove(self, key):
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)


"""
- Let n be the number of all the possible keys, and k be the number of buckets, which
  is the same as self.key_space
- Time is O(n/k)
"""


