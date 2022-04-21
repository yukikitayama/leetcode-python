from typing import List
import collections


class Twitter:
    def __init__(self):
        self.tweets = collections.defaultdict(list)
        self.following = collections.defaultdict(set)
        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.order, tweetId))
        # -= because later we sort it by order, so smaller number (negative)
        # comes first, which is recent tweets
        self.order -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        for i in self.following[userId] | {userId}:
            for tweet in self.tweets[i]:
                tweets.append(tweet)
        return [id for order, id  in sorted(tweets)[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # When an element doesn't exist in the set,
        # discard() throws no error, but remove() throws error
        self.following[followerId].discard(followeeId)


if __name__ == '__main__':
    obj = Twitter()
    print(obj.postTweet(1, 5))
    print(obj.getNewsFeed(1))
    print(obj.follow(1, 2))
    print(obj.postTweet(2, 6))
    print(obj.getNewsFeed(1))
    print(obj.unfollow(1, 2))
    print(obj.getNewsFeed(1))
