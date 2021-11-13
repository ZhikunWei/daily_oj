#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap_index = [False] * len(word)
        caps = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        for i in range(len(word)):
            cap_index[i] = word[i] in caps
        print(cap_index)
        if sum(cap_index) == len(cap_index) or sum(cap_index) == 0 or (
                cap_index[0] and sum(cap_index[1:]) == 0):
            return True
        else:
            return False

s = Solution()
print(s.detectCapitalUse('Leetcode'))