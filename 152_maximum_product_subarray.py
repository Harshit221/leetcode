from typing import List
import sys

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        tempMin = nums[0]
        cmax = tempMax = nums[0]
        i = 1
        n = len(nums)
        while i < n:
            if nums[i] == 0 and i < n-1:
                tempMin = nums[i+1]
                tempMax = max(nums[i+1], 0)
                cmax= max(cmax, tempMax)
                i += 2
            else:
                tempMin, tempMax= min(nums[i], tempMin * nums[i], tempMax * nums[i]),  max(nums[i], tempMin * nums[i], tempMax * nums[i])
                cmax = max(tempMax, cmax)
                i += 1
        return cmax
    
    def maxProduct1(self, nums):
        cmin, cmax = 1,1
        res = max(nums)
        for n in nums:
            if n == 0:
                cmin = cmax = 1
                continue
            else:
                cmin, cmax = min(n, cmin*n, cmax*n), max(n, cmin*n, cmax*n)
                res = max(cmax, res)
        return res
    
print(Solution().maxProduct1([-2,0]))