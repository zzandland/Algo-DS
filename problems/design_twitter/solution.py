from collections import defaultdict, deque
from heapq import heapify, heappop

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.fer2fee = defaultdict(set) # follower to followees
        self.fee2fer = defaultdict(set) # followee to follower
        self.u2t = defaultdict(list) # user's posted tweets
        self.cache = defaultdict(deque) # cache of newsfeeds
        self.id = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.follow(userId, userId)
        self.u2t[userId].append((self.id, tweetId))
        for uid in self.fee2fer[userId]:
            self.cache[uid].appendleft(tweetId)
        self.id -= 1
        
    def _assembleNewsFeed(self, userId: int) -> None:
        tmp = []
        for uid in self.fer2fee[userId]:
            tmp += self.u2t[uid]
        heapify(tmp)
        res = []
        for _ in range(10):
            if not tmp: break
            res.append(heappop(tmp)[1])
        self.cache[userId] = deque(res)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        return list(self.cache[userId])[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.fer2fee[followerId].add(followeeId)
        self.fee2fer[followeeId].add(followerId)
        self._assembleNewsFeed(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId and followeeId in self.fer2fee[followerId]:
            self.fer2fee[followerId].remove(followeeId)
            self.fee2fer[followeeId].remove(followerId)
            self._assembleNewsFeed(followerId)
            
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)