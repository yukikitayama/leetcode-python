"""
- Initialize ans list of string
- In for loop, each time append to the list
  - when '.' append '[.]'
- Return joined
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return ''.join('[.]' if ad == '.' else ad for ad in address)


if __name__ == '__main__':
    address = '1.1.1.1'
    print(Solution().defangIPaddr(address))
