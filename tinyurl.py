import random
import string


class Codec:
    def __init__(self):
        self.urls = {}

    def encode(self, longUrl: str) -> str:
        url = "".join([random.choice(string.ascii_lowercase) for _ in range(5)])
        self.urls[url] = longUrl
        return url

    def decode(self, shortUrl: str) -> str:
        return self.urls[shortUrl]


if __name__ == "__main__":
    codec = Codec()
    codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl"))
