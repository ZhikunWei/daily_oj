#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'
class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s) < len(p):
            return []
        rec = {}
        for x in p:
            if x not in rec:
                rec[x] = 0
            rec[x] += 1
        s_rec = {}
        for i in range(len(p)):
            if s[i] not in s_rec:
                s_rec[s[i]] = 0
            s_rec[s[i]] += 1
        res = []
        print(rec, s_rec)
        for i in range(len(s) - len(p)+1):
            if len(rec) == len(s_rec):
                isgood = True
                for x in rec:
                    if x not in s_rec or rec[x] != s_rec[x]:
                        isgood = False
                        break
                if isgood:
                    res.append(i)
            # print(s[i:i + len(p)], s_rec)
            if i+len(p) < len(s):
                s_rec[s[i]] -= 1
                if s_rec[s[i]] == 0:
                    del s_rec[s[i]]
                if s[i+len(p)] not in s_rec:
                    s_rec[s[i+len(p)]] = 0
                s_rec[s[i + len(p)]] += 1
        return res

s = Solution().findAnagrams("cbaebabacd", "abc")
        