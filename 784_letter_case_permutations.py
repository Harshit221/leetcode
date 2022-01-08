from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if len(s) == 0:
            return ['']
        perms = self.letterCasePermutation(s[1:])
        print(perms)
        temp = [s[0], s[0].upper()] if isChar(s[0]) else [s[0]]
        result = []
        for perm in perms:
            for c in temp:
                result.append(c+perm)
        return result
        
def isChar(s):
    return 'a' <= s <= 'z'

print(Solution().letterCasePermutation('a1b2'))