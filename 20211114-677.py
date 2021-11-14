#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'
class MapSum:

    def __init__(self):
        self.d = {}

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for k in self.d:
            if prefix == k[:len(prefix)]:
                res += self.d[k]
        return res


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
ops = ["MapSum","insert","sum","insert","sum","sum","insert","sum","sum","sum","insert","sum","sum","sum","sum","sum","insert","insert","insert","sum","sum","sum","sum","sum","sum","insert","sum","sum"]
data = [[],["aa",3],["a"],["aa",2],["a"],["aa"],["aaa",3],["aaa"],["bbb"],["ccc"],["aewfwaefjeoawefjwoeajfowajfoewajfoawefjeowajfowaj",111],["aa"],["a"],["b"],["c"],["aewfwaefjeoawefjwoeajfowajfoewajfoawefjeowajfowaj"],["bb",143],["cc",144],["aew",145],["bb"],["cc"],["aew"],["dddd"],["cdcd"],["aab"],["aab",33],["aab"],["ab"]]
for i in range(len(ops)):
    if ops[i] == 'insert':
        obj.insert(data[i][0], data[i][1])
    elif ops[i] == 'sum':
        print(obj.sum(data[i][0]))