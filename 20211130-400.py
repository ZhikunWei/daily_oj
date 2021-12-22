class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9:
            return n
        dig_sum = 0
        mag = 0
        while dig_sum + 9 * (10 ** mag) * (mag+1) <= n:
            dig_sum += 9 * (10 ** mag) * (mag+1)
            mag += 1
        order = (n - dig_sum-1) // (mag+1)
        sub_order = (n - dig_sum-1) % (mag+1)
        number = 10 ** mag + order
        res = []
        while number > 0:
            res.append(number % 10)
            number = number // 10
        print(order, sub_order, res)
        return res[-sub_order-1]

t = Solution().findNthDigit(9)
print(t)
