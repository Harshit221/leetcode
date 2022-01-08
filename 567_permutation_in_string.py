class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s1) == 0:
            return True
        l1 = len(s1)
        l2 = len(s2)
        cache1 = [0] * 26
        cache2 = [0] * 26

        base = ord('a')
        for c in s1:
            cache1[ord(c)-base] += 1
        for i in range(l1):
            cache2[ord(s2[i])-base] += 1
        res = 0
        for i in range(26):
            if cache1[i] == cache2[i]:
                res += 1
        if res == 26:
            return True
        for i in range(l1, l2):
            removed = ord(s2[i-l1]) -base
            added = ord(s2[i])-base
            if cache1[added] == cache2[added]:
                res -= 1
            cache2[added] += 1
            if cache1[added] == cache2[added]:
                res += 1
            if cache2[removed] == cache1[removed]:
                res -= 1
            cache2[removed] -= 1
            if cache2[removed] == cache1[removed]:
                res += 1
            
            if res == 26:
                return True
        
        return res == 26

    def checkInclusion1(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s1) == 0:
            return True
        l1 = len(s1)
        l2 = len(s2)
        cache1 = [0] * 26
        cache2 = [0] * 26

        base = ord('a')
        for c in s1:
            cache1[ord(c)-base] += 1
        for i in range(l1):
            cache2[ord(s2[i])-base] += 1
            
        if cache1 == cache2:
            return True
        for i in range(l1, l2):
            cache2[ord(s2[i])-base] += 1
            cache2[ord(s2[i-l1])-base] -= 1
            if cache1 == cache2:
                return True
        
        return cache1 == cache2
            
print(Solution().checkInclusion("ab","eidbaooo"))
