#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

class Solution:
    def missingNumber(self, nums) -> int:
        rec = [0] * (len(nums)+1)
        for x in nums:
            rec[x] = 1
        for i in range(len(rec)):
            if rec[i] == 0:
                return i