import heapq
from collections import OrderedDict, defaultdict
class Twitter:
    
    def __init__(self):
        self.follow_list = defaultdict(set)
        self.post_list = defaultdict(list)
        self.time_stamp = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_list[userId].append((self.time_stamp, tweetId))
        self.time_stamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        q = list(self.post_list[userId])
        heapq.heapify(q)
        while len(q) > 10:
            heapq.heappop(q)
        for person in self.follow_list[userId]:
            q += self.post_list[person]
            heapq.heapify(q)
            while len(q) > 10:
                heapq.heappop(q)
        ans = []
        while q:
            ans.append(heapq.heappop(q)[1])
        return ans[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.follow_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_list[followerId]:
            self.follow_list[followerId].remove(followeeId)

