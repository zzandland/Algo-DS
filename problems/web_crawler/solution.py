# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from collections import deque

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        no_protocol = startUrl[7:] if startUrl[:7] == 'http://' else startUrl
        hostname = no_protocol.split('/')[0]
        seen = set()
        res = []
        q = deque([startUrl])
        while q:
            cur_url = q.popleft()
            if cur_url in seen: continue
            res.append(cur_url)
            seen.add(cur_url)
            q += [url for url in htmlParser.getUrls(cur_url) if url.find(hostname) != -1]
        return res