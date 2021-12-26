class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        z = 0
        nz = 0
        
        length = len(nums)
        def nextZero(z):
            while z < length:
                if nums[z] == 0:
                    return z
                z += 1
            return z
        def nextNonZero(z):
            while z < length:
                if nums[z] != 0:
                    return z
                z += 1
            return z
        z = nextZero(z)
        nz = nextNonZero(z)
        while nz < len(nums):
            nums[z] = nums[nz]
            nums[nz] = 0
            z = nextZero(z)
            nz = nextNonZero(nz)
            
        return nums

print(Solution().moveZeroes([0,1,0,2,0,3,0]))