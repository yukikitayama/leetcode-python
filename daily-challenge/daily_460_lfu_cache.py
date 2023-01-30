import collections


class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key2node = collections.defaultdict(Node)
        self.count2node = collections.defaultdict(collections.OrderedDict)
        self.minCount = None

    def get(self, key):
        if key not in self.key2node:
            return -1

        node = self.key2node[key]

        del self.count2node[node.count][key]

        if not self.count2node[node.count]:
            del self.count2node[node.count]

        node.count += 1
        self.count2node[node.count][key] = node

        #
        if not self.count2node[self.minCount]:
            self.minCount += 1

        return node.val

    def put(self, key, value):
        if not self.cap:
            return

        if key in self.key2node:
            self.key2node[key].val = value
            # Update count2node
            self.get(key)
            return None

        if len(self.key2node) == self.cap:
            # last=False gives us the oldest item
            k, n = self.count2node[self.minCount].popitem(last=False)
            del self.key2node[k]

        self.count2node[1][key] = Node(key, value, 1)
        self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        return None


if __name__ == "__main__":
    lfu = LFUCache(2)
    print(lfu.get(1))
    print(lfu.put(1, 1))
    print(lfu.cache, lfu.frequencies)
    print(lfu.get(1))
