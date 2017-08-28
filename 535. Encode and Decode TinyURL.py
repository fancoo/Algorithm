class Codec:
    def __init__(self):
        self.urls2codes = {}
        self.codes2urls = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.urls2codes:
            self.urls2codes[longUrl] = len(self.urls2codes)
            self.codes2urls[len(self.urls2codes) - 1] = longUrl
        return "http://tinyurl.com/" + str(self.urls2codes[longUrl])

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        relUrl = int(shortUrl.replace("http://tinyurl.com/", ""))
        if relUrl in self.codes2urls:
            return self.codes2urls[relUrl]
        return None

    '''To be improved: use number mixed character to store more:(10+26*2)**6'''

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(url))