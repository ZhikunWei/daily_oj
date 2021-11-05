# ac
class Solution:
    def longestSubsequence(self, arr, difference: int) -> int:
        d = {}
        for i in range(len(arr)):
            if arr[i]-difference in d:
                d[arr[i]] = d[arr[i]-difference] + 1
            else:
                d[arr[i]] = 1
        res = 1
        for k in d:
            res = max(res, d[k])
        return res

s = Solution()
res = s.longestSubsequence([1,2,3,4], 1)
print(res)