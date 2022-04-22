"""
- Trie?
"""


import collections


class FileSystem:
    def __init__(self):
        self.paths = collections.defaultdict()

    def createPath(self, path: str, value: int) -> bool:
        # Basic path validation
        if path == '/' or len(path) == 0 or path in self.paths:
            return False

        # Check parent presence
        # rfind(string) return an start index of the last occurrence of the given string
        parent = path[:path.rfind('/')]

        # print(f'parent: "{parent}"')

        # For '/leet' gives us parent "", but it's valid to add
        # So we need len(parent) > 1 and to pass the root level path to add.
        if len(parent) > 1 and parent not in self.paths:
            return False

        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)


if __name__ == '__main__':
    obj = FileSystem()
    print(obj.createPath('/leet', 1))
    print(obj.createPath('/leet/code', 2))
    print(obj.get('/leet/code'))
    print(obj.createPath('/c/d', 1))
    print(obj.get('/c'))
