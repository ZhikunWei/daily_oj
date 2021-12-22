#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1
        t = a
        res = 1
        while len(t) < len(b) * 3 or res < 2:
            t += a
            res += 1
            # print(t)
            if b in t:
                return res
        
        if b in t:
            return res
        else:
            return -1


Solution().repeatedStringMatch('aaaaaab', 'ba')
