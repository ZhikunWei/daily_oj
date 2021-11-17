class Solution:
    def maxProduct(self, words) -> int:
        res = 0
        for i in range(len(words)):
            word_i_set = set(words[i])
            for j in range(i, len(words)):
                if len(set(words[j]).intersection(word_i_set)) == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res