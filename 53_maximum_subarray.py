from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur = nums[0]
        
        for i in range(1, len(nums)):
            cur = max(nums[i], nums[i] + cur)
            ans = max(ans, cur)
        
        return ans


print(Solution().maxSubArray([-1,1,2,1]))