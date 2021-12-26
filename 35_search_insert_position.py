from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums)-1
        while(i<=j):
            m = (i+j)//2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                j = m-1
            else:
                i = m+1

        return i
    
print(Solution().searchInsert([1,3], 4))