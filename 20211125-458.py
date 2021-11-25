#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

# 其实香农已经在《信息论》（信息熵）中给过我们结论了——我们一共可以进行n轮实验（n = minutesToTest / minutesToDie）：
#
# 经过所有实验，一只小猪能有多少种状态？第一轮就死、第二轮死、...、第n轮死，以及生还，所以一共有n + 1种状态
# n + 1种状态所携带的信息为log_2(n + 1)比特，这也是一只小猪最多提供的信息量
# 而”buckets瓶液体中哪一瓶是毒“这件事，也有buckets种可能性，所以需要的信息量是log_2(buckets)
# 注：以上所有事件、状态都是先验等概的，所以可以直接对2取对数得到信息熵
#
# 因此一定存在一种“合理设计”的实验，使得我们只要有k只猪猪：满足 k * log_2(n + 1) >= log_2(buckets)时，则我们一定能得到足够的信息量去判断哪一瓶是毒。


class Solution:
    
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        import math
        states = minutesToTest // minutesToDie + 1
        return math.ceil(math.log(buckets) / math.log(states))
    