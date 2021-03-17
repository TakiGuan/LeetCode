"""
Description: Encode and Decode TinyURL
Version: 1
Author: Taki Guan
Date: 2021-03-16 08:22:07
LastEditors: Taki Guan
LastEditTime: 2021-03-16 16:19:58
"""
#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
import string
import random


class Codec:

    alphabet = string.ascii_letters + string.digits

    def __init__(self):
        self.code2url = {}
        self.url2code = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        while longUrl not in self.url2code:
            code = "".join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return "http://tinyurl.com/" + self.url2code[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.code2url[shortUrl[-6:]]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end
