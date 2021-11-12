#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        f = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                f[i][j] = min(k + max(f[i][k - 1], f[k + 1][j]) for k in range(i, j))
        return f[1][n]

    # 没有考虑right中可能会加多次j的情况
    # def getMoneyAmount_wa(self, n: int) -> int:
    #     if n == 1:
    #         return 0
    #     dp = [0] * (n+1)
    #     dp[2] = 1
    #     for i in range(3, n+1):
    #         t = []
    #         for j in range(1, i+1):
    #             left = dp[j-1]
    #             right = dp[i-j] if j <= i else 0
    #             if i-j > 1:
    #                 right += j
    #             t.append(max(left, right) + j)
    #             if i == 12:
    #                 print('dp[0,%d]=%d, j=%d, dp[%d, %d]=%d, c=%d' % ((j-1), left, j, j+1, i, right, max(left, right) + j))
    #         # print(i, min(t), t)
    #         dp[i] = min(t)
    #     print(dp)
    #     return dp[n]
    
    
t = Solution()
print(t.getMoneyAmount(12))
