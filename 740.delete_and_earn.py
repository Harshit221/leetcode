from typing import Counter, List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = {}
        for n in nums:
            if n in counter:
                counter[n] += n
            else:
                counter[n] = n
        cache = sorted(counter.items(), reverse=True)
        n = len(cache)
        result = [[0,0] for i in range(n)]
        result[0][0] = cache[0][1] 
        for i in range(1,n):
            if cache[i][0]+1 == cache[i-1][0]:
                result[i][0] = result[i-1][1]+cache[i][1]
            else:
                result[i][0] = cache[i][1]+max(result[i-1])
            
            result[i][1] = max(result[i-1])

        return max(result[-1])
import itertools
# print(Solution().deleteAndEarn([8,10,4,9,1,3,5,9,4,10]))
acc = list(itertools.accumulate([8,10,4,9,1,3,5,9,4,10]))
print(acc)