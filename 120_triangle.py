from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache = dict()
        def recursive(i, j):
            
            if i >= len(triangle) or j >= len(triangle[i]):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            cache[(i, j)] = res = triangle[i][j] + min(recursive(i+1, j), recursive(i+1, j+1))
            return res
        return recursive(0, 0)
    
print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))