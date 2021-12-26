from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        m = (l+r)//2
        while l <= r:
            m = (l+r)//2
            
            if matrix[m][0] == target:
                return True
            elif target >= matrix[m][0] and target <= matrix[m][-1]:
                break
            elif target <= matrix[m-1][-1] and m > 0:
                r = m - 1
            elif m < len(matrix) - 1 and target >= matrix[m+1][0]:
                l = m + 1
            else:
                return False
        
        l,r = 0, len(matrix[m])-1
        while l<=r:
            m1 = (l+r)//2
            if target == matrix[m][m1]:
                return True
            elif target < matrix[m][m1]:
                r = m1-1
            else:
                l = m1+1
        return False
                
print(Solution().searchMatrix([[1],[3]], 3))