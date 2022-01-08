from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        s0, s1 = -prices[0]-fee, 0
        for i in range(1, len(prices)):
            prevS0 = s0
            s0 = max(s0, s1 - prices[i] - fee)
            s1 = max(s1, prevS0+prices[i])
        return s1
    
print(Solution().maxProfit([1,3,2,8,4,9],2))