class Solution:
    def originalDigits(self, s: str) -> str:
        words = {'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}
        rec = {}
        for k in words:
            for kk in k:
                rec[kk] = 0
        for x in s:
            rec[x] += 1

        nums = [0] * 10
        nums[0] = rec['z']
        nums[6] = rec['x']
        nums[7] = rec['s'] - rec['x']
        nums[5] = rec['v'] - nums[7]
        nums[4] = rec['f'] - nums[5]
        nums[8] = rec['g']
        nums[3] = rec['h'] - nums[8]
        nums[2] = rec['w']
        nums[1] = rec['o'] - nums[0] - nums[2] - nums[4]
        nums[9] = rec['i'] - nums[5] - nums[6] - nums[8]
        res = ''
        for i in range(10):
            res += str(i) * nums[i]
        return res

