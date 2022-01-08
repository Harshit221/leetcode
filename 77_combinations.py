from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combination([i for i in range(1,n+1)], k)
        
        

def combination(nums, k):
    if k > len(nums):
        return []
    if k == 1:
        return [ [n] for n in nums]
    if k == len(nums):
        return [nums]
    result = []
    while len(nums) > k-1:
        n = nums.pop(0)
        print('popped', n)
        combs = combination(nums.copy(), k-1)
        for i in range(len(combs)):
            combs[i] = [n] + combs[i]
        # nums.append(n)
        result.extend(combs)
    return result

print(Solution().combine(5,3))