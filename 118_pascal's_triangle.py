from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sol = [1]
        for i in range(1, numRows):
            tmp = [1]
            for j in range(1,i):
                tmp.append(sol[-1][j-1]+sol[-1][j])
            tmp.append(1)
            sol.append(tmp)
            
        return sol
    
print(Solution().generate(5))