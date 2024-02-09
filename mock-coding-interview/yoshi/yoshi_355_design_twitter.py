import collections
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.user_to_tweet = collections.defaultdict(list)
        self.follower_to_followee = collections.defaultdict(set)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_tweet[userId].append((self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.follower_to_followee[userId]
        followees.add(userId)

        heap = []
        heapq.heapify(heap)

        for user_id in followees:
            # [(1, 10), (3, 20)]
            tweets = self.user_to_tweet[user_id]

            for tweet in tweets:
                heapq.heappush(heap, tweet)

        ans = []

        for _ in range(len(heap)):
            counter, tweet_id = heapq.heappop(heap)
            ans.append(tweet_id)

        ans.reverse()

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_to_followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower_to_followee[followerId].remove(followeeId)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))