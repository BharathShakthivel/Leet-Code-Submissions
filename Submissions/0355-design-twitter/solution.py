class Twitter:
    from collections import defaultdict
    '''
        ## 🧠 Mental Model: “Merge K Tweet Stacks”

        * Each user’s tweets = a **stack (newest on top)**
        * You follow multiple users → you have **K stacks**
        * Goal = get **top 10 most recent tweets across all stacks**

        ## ⚙️ How it works

        1. Put the **top tweet of each stack** into a heap
        2. Repeat:

        * Pop the **most recent tweet**
        * Add it to result
        * Push the **next tweet from that same user**

        ## 🔑 One-line intuition

        👉 *“Always keep one tweet per user in the heap, and refill from the same user after popping.”*


        ## 📌 Why it’s efficient

        * Heap size = number of followees (not total tweets)
        * Only processes up to **10 tweets**
        * Equivalent to **merge k sorted lists**


        ## 🧩 Trigger to recognize this pattern

        If you see:

        * Multiple sorted lists
        * Need top K results

        👉 Think: **Heap + incremental merge**



    '''
    def __init__(self):
        self.followMap = defaultdict(set)
        self.count = 0
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res, min_heap = [],[]
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                count,tweetId = self.tweetMap[followeeId][index]
                min_heap.append([count,tweetId,followeeId,index-1])
        heapq.heapify(min_heap)
        while min_heap and len(res)<10:
            count,tweetId,followeeId,index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index>=0:
                count,tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(min_heap,[count,tweetId,followeeId,index-1])
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
