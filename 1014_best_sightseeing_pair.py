from typing import List


class Solution:
    def maxScoreSightseeingPair(self, nums: List[int]) -> int:
        a = nums[0]-1
        b = nums[1]
        ans = a+b
        def max2of3(a,b,c):
            if a<=b and a<=c:
                return b,c
            elif  b<=a and b <= c:
                return a,c
            else:
                return a, b
        for i in range(2, len(nums)):
            a -= 1
            b -= 1
            a,b = max2of3(a,b, nums[i])
            ans = max(ans, a+b)
        return ans
        
    
print(Solution().maxScoreSightseeingPair([1,3,5]))
# [2,7,7,2,1,7,10,4,3,3]
