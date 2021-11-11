# ac

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        rec = [1]
        for i in range(2, n+1):
            # print('rec', rec)
            pre_sum = [0]
            for j in range(len(rec)):
                pre_sum.append(pre_sum[-1] + rec[j])
            t = []
            for j in range(min(len(rec)+i-1, k+2)):
                # print('min(j, len(pre_sum)-1)', min(j, len(pre_sum)-2)+1, 'max(j-i, 0)', max(j-i+1, 0))
                t.append(pre_sum[min(j+1, len(pre_sum)-1)] - pre_sum[max(j-i+1, 0)])
            rec = t
        print('rec', rec)
        if k >= len(rec):
            return 0
        return rec[k] % 1000000007


t = Solution()
print(t.kInversePairs(1, 1))
