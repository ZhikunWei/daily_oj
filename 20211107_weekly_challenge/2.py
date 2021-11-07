#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'
# 5919
# TLE

class Solution:
    def countVowels(self, word: str) -> int:
        dp = [0] * len(word)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        dp[0] = int(word[0] in vowels)
        for i in range(1, len(word)):
            if word[i] in vowels:
                dp[i] = dp[i-1]+ 1
            else:
                dp[i] = dp[i-1]
        dp = [0] + dp
        
        res = 0
        for i in range(1, len(dp)):
            for j in range(i):
                res += dp[i]-dp[j]
        return res

print(Solution().countVowels('noosabasboosa'))