import sys, copy
from typing import Deque, List

class Solution:
    def orangesRotting(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        days = -1
        visited = 0
        cache = set()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        queue = Deque()
        totalFruits = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    continue
                if mat[i][j] == 2:
                    queue.append((i,j))
                    cache.add((i,j))
                totalFruits += 1

        def isValid(position):
            if position[0] < 0 or position[0] >= rows or position[1] < 0 or position[1] >= cols:
                return False
            return position not in cache and mat[position[0]][position[1]] == 1
        while queue:
            size = len(queue)
            for x in range(size):
                fruit = queue.popleft()
                visited += 1
                for a,b in dirs:
                    if isValid((fruit[0]+a, fruit[1]+b)):
                        queue.append((fruit[0]+a, fruit[1]+b))                        
                        cache.add((fruit[0]+a, fruit[1]+b))
            days += 1
        if visited != totalFruits:
            return -1
        
        if totalFruits == 0:
            return 0
        return days        

print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))