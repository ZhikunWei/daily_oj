#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

class Solution:
    def findLHS(self, nums) -> int:
        d = {}
        for x in nums:
            if x not in d:
                d[x] = 0
            d[x] += 1
        if len(d) < 2:
            return 0
        sorted_d = sorted(d.items(), key=lambda x: x[0])
        res = 0
        for i in range(1, len(sorted_d)):
            if sorted_d[i-1][0] + 1 == sorted_d[i][0]:
                res = max(res, sorted_d[i-1][1] + sorted_d[i][1])
        return res
        
        
        