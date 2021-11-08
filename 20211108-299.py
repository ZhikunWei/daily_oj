#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        B = 0
        s = {}
        g = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                if secret[i] not in s:
                    s[secret[i]] = 0
                s[secret[i]] += 1
                if guess[i] not in g:
                    g[guess[i]] = 0
                g[guess[i]] += 1
        for x in s:
            if x in g:
                B += min(s[x], g[x])
        return '%dA%dB' % (A, B)