#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'
# ac

class Solution:
    def maxCount(self, m: int, n: int, ops) -> int:
        min_a = m
        min_b = n
        for a, b in ops:
            min_a = min(a, min_a)
            min_b = min(b, min_b)
        return (min_a) * (min_b)