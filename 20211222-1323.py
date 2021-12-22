#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'


class Solution:
    def maximum69Number(self, num: int) -> int:
        t = str(num)
        str_num = []
        for x in t:
            str_num.append(x)
        for i in range(len(str_num)):
            if str_num[i] == '6':
                str_num[i] = '9'
                return int(''.join(str_num))
        return num


t = Solution().maximum69Number(9996)
