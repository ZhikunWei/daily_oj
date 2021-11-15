class Solution:
    # 吐了，求n以内的完全平方数即可，只有完全平方数的灯最后会亮
    def bulbSwitch(self, n: int) -> int:
        import math
        return int(math.sqrt(n))

    # TLE case: n=9999999
    # def bulbSwitch(self, n: int) -> int:
    #     dp = [0] * (n+1)
    #     if n == 0 or n == 1:
    #         return n
    #
    #     for i in range(2, n+1):
    #         dp[i] += 1
    #         for j in range(2, n//i+1):
    #             dp[i+j] += 1
    #     res = 0
    #     for i in range(1, n+1):
    #         if dp[i] % 2 == 0:
    #             res += 1
    #     # print(dp)
    #     return res


t = Solution().bulbSwitch(12)
print(t)
