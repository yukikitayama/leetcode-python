class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # print(input)
        ans = 0

        pathlen = {0: 0}

        # splitlines() splits by several representations, but one of them is \n
        # but \t is not included
        for line in input.splitlines():
            # print(f'line: {line}')

            # lstrip() returns a copy of string with leasing characters removed
            # If parameter is not specified, whitespaces are removed
            name = line.lstrip('\t')
            # print(f'name: {name}')

            # '\t' counts as 1 length string
            depth = len(line) - len(name)
            # print(f'depth: {depth}, len(line): {len(line)}, len(name): {len(name)}')

            # Having '.' means current name string is a file name
            if '.' in name:
                # name: \tfile.ext, depth: 2, pathlen[2]: 12, len(name): 8, ans: 20
                ans = max(ans, pathlen[depth] + len(name))

            else:
                # + 1 after len(name) is extra length for '/' e.g. dir/file.ext
                # e.g. name: dir, depth: 0, pathlen[1]: 0 + 3 + 1 = 4
                # name: \tsubdir1, depth: 1, pathlen[2]: 4 + 7 + 1 = 12
                # name: \tsubdir2, depth: 1, pathlen[2]: 4 + 7 + 1 = 12
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1

            # print()

        return ans


if __name__ == '__main__':
    input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    print(Solution().lengthLongestPath(input))
