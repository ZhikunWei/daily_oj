class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:
        res = 0
        for i in range(1, len(timeSeries)):
            res += min(duration, timeSeries[i] - timeSeries[i-1])
        if len(timeSeries) > 0:
            res += duration
        return res

print(Solution().findPoisonedDuration([1,2,3,4,5,6,7,8,9], 1))