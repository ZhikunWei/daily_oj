#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        rec = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        meta = 'aeiou'
        i, j = 0, 0
        res = 0
        while i < len(word) and j < len(word):
            if word[i] in meta:
                rec[word[i]] += 1
                isin = True
                for k in rec:
                    if rec[k] == 0:
                        isin=False
                if isin:
                    res += 1
                print(j, i,word[j:i+1],res, rec)
            else:
                while j <= i:
                    if word[j] in meta:
                        rec[word[j]] -= 1
                        isin = True
                        for k in rec:
                            if rec[k] == 0:
                                isin=False
                        if isin:
                            res += 1
                    j += 1
                    print(j, i, word[j:i],res, rec)
                    
                for k in rec:
                    rec[k] = 0
            i += 1
        return res

print(Solution().countVowelSubstrings('cuaieuouac'))