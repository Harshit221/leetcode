from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(self.areaOfIland(grid, i, j), maxArea)
        print(grid)
        return maxArea
        
    def areaOfIland(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return 0
        if grid[i][j] <= 0:
            return 0

        grid[i][j] = -1
        a = self.areaOfIland(grid, i-1, j)
        b = self.areaOfIland(grid, i+1, j)
        c = self.areaOfIland(grid, i, j-1)
        d = self.areaOfIland(grid, i, j+1)
        # print(a+a+b+c+d) 
        return 1+a+b+c+d
    
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))