from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        data1 = {}
        for i, n in enumerate(nums):
            if n not in data:
                data[n] = i
            else:
                data1[n] = i
        
        for k,v in data.items():  
            if  (k == target-k):
                if k in data1:
                    return sorted([v, data1[k]])
            elif target - k in data:
                return sorted([v, data[target-k]])
            
        return []
    
