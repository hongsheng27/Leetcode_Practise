class Twitter:
    def __init__(self):
        self.allTweets = defaultdict(list) # userId: [(time, userId, index, tweetId)]
        self.followMap = defaultdict(set) # userId: set(followeeId(#include himself))
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        index = len(self.allTweets[userId])
        self.allTweets[userId].append((self.time, userId, index, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []
        followeeIds = self.followMap.get(userId, set()) | {userId}
        for f in followeeIds:
            if f in self.allTweets and self.allTweets[f]:
                fNew = self.allTweets[f][-1]
                heapq.heappush(maxHeap, fNew)
        while len(res) < 10 and maxHeap:
            time, _userId, index, tweetId = heapq.heappop(maxHeap)
            res.append(tweetId)
            if self.allTweets[_userId] and index:
                fNextNew = self.allTweets[_userId][index - 1]
                heapq.heappush(maxHeap, fNextNew)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followMap[followerId]: return
        self.followMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)