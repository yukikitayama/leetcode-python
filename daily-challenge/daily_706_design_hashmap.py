class Bucket:
    def __init__(self):
        self.array = []

    def update(self, key: int, value: int):
        for i, kv in enumerate(self.array):
            if kv[0] == key:
                self.array[i] = (key, value)
                return
        self.array.append((key, value))

    def get(self, key: int) -> int:
        for kv in self.array:
            if kv[0] == key:
                return kv[1]
        return -1

    def delete(self, key: int):
        for i, kv in enumerate(self.array):
            if kv[0] == key:
                # print(f'before: {self.array}')
                self.array.pop(i)
                # print(f'i: {i}')
                # print(f'after: {self.array}')


class MyHashMap:
    def __init__(self):
        self.key_range = 1999
        self.hashmap = [Bucket() for _ in range(self.key_range)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.key_range
        self.hashmap[hash_key].update(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.key_range
        return self.hashmap[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.key_range
        self.hashmap[hash_key].delete(key)


if __name__ == '__main__':
    obj = MyHashMap()
    print(obj.put(1, 1))
    print(obj.put(2, 2))
    print(obj.get(1))
    print(obj.get(3))
    print(obj.put(2, 1))
    # print(obj.hashmap[2].array)
    print(obj.get(2))
    print(obj.remove(2))
    # print(obj.hashmap[2].array)
    print(obj.get(2))
