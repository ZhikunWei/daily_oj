#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

class Solution:

    def __init__(self, nums):
        self.original = nums.copy()
        self.nums = nums

    def reset(self):
        return self.original

    def shuffle(self):
        import random
        random.shuffle(self.nums)
        return self.nums
        



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()