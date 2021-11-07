#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = 0
        for i in range(len(word)):
            if word[i] in vowels:
                res += (i+1)*(len(word)-i)
        return res

print(Solution().countVowels('abc'))