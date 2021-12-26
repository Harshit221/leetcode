class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        sol = [[0 for i in range(c)] for j in range(r)]
        # sol[0][0] = mat[0][0]
        for x in range(m*n):
            i1 = (x - x%c)//c
            j1 = x % c
            i2 = (x - x%n)//n
            j2 = x % n
            # print([i1, j2], [i2, j2])
            sol[i1][j1] = mat[i2][j2]
        return sol
print(Solution().matrixReshape([[1,2],[3,4],[5,6]],6,1))
# r, c = 6, 1
# for i in range(r*c):
# 	print(i - i//r,i//r)

# for i in range(r):
# 	for j in range(c):
# 		x = i*c+j
# 		print(i,j,(x-x%c)//c,x%c)