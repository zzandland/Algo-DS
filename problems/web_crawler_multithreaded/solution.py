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
from concurrent.futures import ThreadPoolExecutor
from collections import deque

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        getHost = lambda x: x.split('/')[2]
        seen = {startUrl}
        with ThreadPoolExecutor() as e:
            tasks = [e.submit(htmlParser.getUrls, startUrl)]
            while tasks:
                for url in tasks.pop().result():
                    if url not in seen and getHost(url) == getHost(startUrl):
                        seen.add(url)
                        tasks.append(e.submit(htmlParser.getUrls, url))
                
        return list(seen)