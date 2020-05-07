from uuid import uuid4
import base64

class Codec:
    def __init__(self):
        self.s = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        uuid = base64.urlsafe_b64encode(uuid4().bytes).decode('utf-8').rstrip('=')
        if uuid not in self.s: self.s[uuid] = longUrl
        return 'https://tinyurl.com/' + uuid

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        uuid = shortUrl.split('https://tinyurl.com/')[1]
        return self.s[uuid] if uuid in self.s else ''
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))