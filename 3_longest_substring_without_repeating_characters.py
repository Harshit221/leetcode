class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = [-1]*128
        ans = -1
        start = -1
        for i, c in enumerate(s):
            if cache[ord(c)] > start:
                start = cache[ord(c)]
            cache[ord(c)] = i
            ans = max(ans, i-start)
                
        return ans
                  
print(Solution().lengthOfLongestSubstring("abcabcbb"))