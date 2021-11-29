class Solution:
    def kthSmallestPrimeFraction(self, arr, k: int):
        rec = []
        for i in range(len(arr)):
            for j in range(i):
                rec.append([arr[j], arr[i], arr[j] / arr[i]])
        sorted_rec = sorted(rec, key=lambda x: x[2])
        print(sorted_rec)
        return sorted_rec[k-1][:2]


Solution().kthSmallestPrimeFraction([1,2,3,5], 3)