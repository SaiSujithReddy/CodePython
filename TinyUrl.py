'''

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it
returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode
algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded
 to the original URL.

'''


class Codec:

    dict_url = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        dict[hash(longUrl)] = longUrl
        y = "http://tinyurl.com/" + hash(longUrl)
        print(y)
        return y


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        z = dict[shortUrl.replace("http://tinyurl.com/","")]
        print(z)
        return z



        # Your Codec object will be instantiated and called as such:
url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
codec.decode(codec.encode(url))

