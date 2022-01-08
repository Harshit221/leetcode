from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def get(nums):
            start = 0
            neg = None
            ans = 0
            for i, n in enumerate(nums):
                if n == 0:
                    tmax = max(neg-start, i-neg-1) if neg is not None else i-start
                    ans = max(ans,tmax)
                    start = i+1
                    neg = None
                elif n < 0:
                    if neg is None:
                        neg = i
                    else:
                        neg = None
            i += 1
            tmax = max(neg-start, i-neg-1) if neg is not None else i-start
            ans = max(ans,tmax)
            return ans
        return max(get(nums), get(nums[::-1]))
    
print(Solution().getMaxLen([5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]))    