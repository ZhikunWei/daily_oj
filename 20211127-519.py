#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.visited = set()

    def flip(self):
        import random
        i = random.randint(0, self.m-1)
        j = random.randint(0, self.n-1)
        if (i, j) not in self.visited:
            self.visited.add((i,j))
            return [i, j]
        else:
            return self.flip()

    def reset(self) -> None:
        self.visited = set()
    


# Your Solution object will be instantiated and called as such:
obj = Solution(10000, 10000)
param_1 = obj.flip()
obj.reset()