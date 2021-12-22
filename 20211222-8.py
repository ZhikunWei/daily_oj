#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'


class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 0
        minus = False
        numbers = '0 1 2 3 4 5 6 7 8 9'.split()
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return 0
        if s[i] not in numbers + ['+', '-']:
            return 0
        if s[i] == '-':
            minus = True
            i += 1
        elif s[i] == '+':
            i += 1
        while i < len(s) and s[i] in numbers:
            res = res * 10 + int(s[i])
            i += 1
        if minus:
            return max(-res, -2 ** 31)
        return min(res, 2 ** 31 - 1)


t = Solution().myAtoi('    -42')
print(t)
