def last_stone(stones):
    stones.sort()

    while len(stones) > 1:
        y = stones.pop()
        x = stones.pop()

        if x != y:
            stones.append(y - x)
            stones.sort()

    return stones[0] if stones else 0


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums

    def add(self, val):
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]


class Twitter:
    def __init__(self):
        self.tweets = []
        self.following = {}

    def postTweet(self, userId, tweetId):
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId):
        result = []
        follows = self.following.get(userId, set())
        follows.add(userId)

        for user, tweet in reversed(self.tweets):
            if user in follows:
                result.append(tweet)
            if len(result) == 10:
                break

        return result

    def follow(self, followerId, followeeId):
        self.following.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
            
def least_interval(tasks, n):
    counts = {}

    for task in tasks:
        counts[task] = counts.get(task, 0) + 1

    max_count = max(counts.values())
    number_of_max = list(counts.values()).count(max_count)

    result = (max_count - 1) * (n + 1) + number_of_max

    return max(len(tasks), result)


def find_kth_largest(nums, k):
    nums = nums.copy()
    nums.sort(reverse=True)
    return nums[k - 1]


def k_closest(points, k):
    points = points.copy()

    points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)

    return points[:k]


class MedianFinder:
    def __init__(self):
        self.data = []

    def addNum(self, num):
        self.data.append(num)
        self.data.sort()

    def findMedian(self):
        n = len(self.data)
        middle = n // 2

        if n % 2 == 1:
            return self.data[middle]
        else:
            return (self.data[middle - 1] + self.data[middle]) / 2


mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())
mf.addNum(3)
print(mf.findMedian())
