from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        self.count = 0
        @lru_cache()
        def decode(i):
            if i >= len(s):
                
                return 1
            if s[i] == '0':
                return 0
            self.count += 1
            res = decode(i+1)
            if i < len(s)-1 and ((s[i] == '1') or (s[i] == '2' and '0' <= s[i+1] <= '6')):
                res += decode(i+2)
            return res
                         
        ans = decode(0)
        print(self.count)
        return ans

print(Solution().numDecodings("2611055971756562")) #