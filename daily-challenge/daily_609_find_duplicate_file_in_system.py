from typing import List
import collections


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = collections.defaultdict(list)

        for line in paths:

            data = line.split()

            # print(f'data: {data}')

            root = data[0]

            for file in data[1:]:

                # print(f'  file: {file}, file.partition(): {file.partition("(")}, file.split(): {file.split("(")}')

                name, content = file.split('(')

                # :-1 because the end always includes ')'
                content_to_paths[content[:-1]].append(f'{root}/{name}')

        # print(content_to_paths)

        return [files for files in content_to_paths.values() if len(files) > 1]


if __name__ == '__main__':
    paths = [
        "root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)",
        "root/c/d 4.txt(efgh)",
        "root 4.txt(efgh)"
    ]
    # [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
    print(Solution().findDuplicate(paths))
