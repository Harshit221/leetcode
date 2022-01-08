from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        sol = [[0 for i in range(len(mat[0]))] for i in range(len(mat))]
        def get(data, i,j):
            if i < 0 or i >= len(data) or j < 0 or j >= len(data[i]):
                print(i, j, 0)
                return 0
            print(i, j, data[i][j])
            return data[i][j]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                sol[i][j] = mat[i][j] + get(sol, i-1, j) - get(sol, i-1-k, j) + get(sol, i, j-1) - get(sol, i,j-1-k) - get(mat, i-1, j-1)
        return sol

print(Solution().matrixBlockSum([[1,2,3], [4,5,6],[7,8,9]], 1))