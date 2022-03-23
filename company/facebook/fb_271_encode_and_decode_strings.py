"""
- Chunked transfer encoding
  - length:string,length:string,...
"""


class Codec:
    def encode(self, strs: [str]) -> str:
        ans = ''
        for s in strs:
            ans += f'{len(s)}:{s}'
        return ans

    def decode(self, s: str) -> [str]:
        ans = []
        i = 0
        while i < len(s):

            # Python STRING.find(value, start=0, end=END_OF_STRING)
            j = s.find(':', i)
            # int(s[i:j]): length
            # j: colon index
            # i: colon index + length + 1 is the next starting index
            i = j + int(s[i:j]) + 1
            # String is after j: colon index and before i: next starting index
            curr = s[j + 1:i]

            ans.append(curr)

        return ans


class Codec1:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if len(strs) == 0:
            return chr(258)

        return chr(257).join(x for x in strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """

        if s == chr(258):
            return []

        return s.split(chr(257))


if __name__ == '__main__':
    codec = Codec()
    encoded = codec.encode(["Hello", "World"])
    print(f'encoded: {encoded}')
    decoded = codec.decode(encoded)
    print(f'decoded: {decoded}')