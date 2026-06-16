class Twitter:
    def __init__(self):
        self.tweetMap = defaultdict(list) # (time, tweetId)
        self.followMap = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        users = self.followMap[userId] | {userId}
        maxHeap = [] # (time, i ,userId, tweetId)
        for user in users:
            if self.tweetMap[user]:
                time, tweetId = self.tweetMap[user][-1]
                heapq.heappush(maxHeap, (time, len(self.tweetMap[user]) - 1, user, tweetId))
        # get top 10
        for _ in range(10):
            if not maxHeap: break
            time, i, userId, tweetId = heapq.heappop(maxHeap)
            res.append(tweetId)
            if i - 1 >= 0:
                time, tweetId = self.tweetMap[userId][i - 1]
                heapq.heappush(maxHeap, (time, i - 1, userId, tweetId))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)