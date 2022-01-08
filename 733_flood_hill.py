from typing import  List
from collections import Counter


class Solution:
    def floodFill(self, image: List[List[int]], i: int, j: int, newColor: int) -> List[List[int]]:
        if newColor == image[i][j]:
            return image   
        return self.recursiveFloodHill(image, i, j, image[i][j], newColor)
             
    
    def recursiveFloodHill(self, image, i, j, target, newColor):
        if i<0 or i>=len(image) or j < 0 or j >= len(image[0]):
            return image
        if image[i][j] != target:
            return image
        image[i][j] += newColor
        image = self.recursiveFloodHill(image, i+1,j, target, newColor)
        image = self.recursiveFloodHill(image, i-1,j, target, newColor)        
        image = self.recursiveFloodHill(image, i,j+1, target, newColor)        
        image = self.recursiveFloodHill(image, i,j-1, target, newColor)   
        return image
    
print(Solution().floodFill([[0,0,0],[0,1,1]],1,1,1))
