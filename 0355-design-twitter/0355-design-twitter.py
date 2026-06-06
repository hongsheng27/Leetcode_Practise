class Twitter:
    def __init__(self):
        self.allTweets = {} # userId: [(time, userId, index, tweetId)]
        self.followMap = {} # userId: set(followeeId(#include himself))
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.allTweets:
            self.allTweets[userId] = [(self.time, userId, 0, tweetId)]
            self.follow(userId, userId) # init: follow himself
        else:
            index = len(self.allTweets[userId])
            self.allTweets[userId].append((self.time, userId, index, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []
        if userId not in self.followMap: return []
        followeeIds = self.followMap[userId]
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
        if followerId not in self.followMap:
            self.followMap[followerId] = set([followeeId])
        else:
            self.followMap[followerId].add(followeeId)
        print(self.followMap)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap or followeeId not in self.followMap[followerId]: return
        self.followMap[followerId].remove(followeeId)
        print(self.followMap)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)