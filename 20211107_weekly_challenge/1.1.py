#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'
# 暴力 ac
# 5918
# 1 <= word.length <= 100


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        if len(word) < 5:
            return 0
        res = 0
        for i in range(4, len(word)):
            for j in range(i-3):
                rec = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
                isin = True
                for x in word[j:i+1]:
                    if x not in rec:
                        isin = False
                        break
                    rec[x] += 1
                for k in rec:
                    if rec[k] == 0:
                        isin = False
                if isin:
                    res += 1
        return res

print(Solution().countVowelSubstrings('cuaieuouac'))