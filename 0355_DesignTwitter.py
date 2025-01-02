class Twitter:
    '''
    Approach
    1. Use defaultdict(list) to store tweetId. key=userId, val=[timestamp, tweetId]
    2. Use defaultdict(set) to store user and its followee. key=userId, val=[followee]
    3. Newsfeed need to be sorted in most recent:
       - need timestamp to monitor
       - use heap to get the most recent timestamp and tweetId
    '''

    def __init__(self):
        self.userTweetId = defaultdict(list) # key: userId, val: [timestamp, tweetId]
        self.userFollowee = defaultdict(set) # key: userId, val: [followeeId]
        self.timestamp = 0                   # to monitor most recent tweet

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweetId[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Adds own userId
        self.userFollowee[userId].add(userId)

        # Populate newsfeed to maxHeap
        newsfeed = []
        for user in self.userFollowee[userId]:
            for ti, tw in self.userTweetId[user]:
                heapq.heappush(newsfeed, [ti, tw])
        
        # Pop maxHeap to get most recent newsfeed
        res = []
        i = 10
        while newsfeed and i > 0:
            ti, tw = heapq.heappop(newsfeed)
            res.append(tw)
            i -= 1
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Boundary condition
        if (
            followerId not in self.userFollowee or
            followeeId not in self.userFollowee[followerId]
        ):
            return
        
        # Remove followee
        self.userFollowee[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
