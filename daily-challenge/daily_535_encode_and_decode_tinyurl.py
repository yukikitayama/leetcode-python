import random


class Codec:
    def __init__(self):
        self.alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.map = {}
        self.encoded_url_length = 6
        self.key = self.get_rand()

    def get_rand(self):
        key = []
        for i in range(self.encoded_url_length):
            # randint(a, b), a <= n <= b
            random_integer = random.randint(0, len(self.alphabet) - 1)
            key.append(self.alphabet[random_integer])
        return ''.join(key)

    def encode(self, longUrl: str) -> str:
        while self.key in self.map:
            self.key = self.get_rand()

        self.map[self.key] = longUrl
        return f'http://tinyurl.com/{self.key}'

    def decode(self, shortUrl: str) -> str:
        key = shortUrl.replace('http://tinyurl.com/', '')
        return self.map[key]


class Codec1:
    """
    Range of URLs is limited by the range of int
    Length of encoded URL isn't necessarily shorter than long URL
    """
    def __init__(self):
        self.map = {}
        self.i = 0

    def encode(self, longUrl: str) -> str:
        self.map[self.i] = longUrl
        encoded = f'http://tinyurl.com/{self.i}'
        self.i += 1
        return encoded

    def decode(self, shortUrl: str) -> str:
        i = int(shortUrl[shortUrl.rfind('/') + 1:])
        return self.map[i]


if __name__ == '__main__':
    obj = Codec()
    longUrl = "https://leetcode.com/problems/design-tinyurl"
    encoded = obj.encode(longUrl)
    print(f'encoded: {encoded}')
    decoded = obj.decode(encoded)
    print(f'decoded: {decoded}')
