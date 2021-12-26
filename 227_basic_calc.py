
class Solution:
    def calculate(self, s: str) -> int:
        data = []
        num = ''
        signs = ['+', '-', '*', '/']
        for c in s:
            if c == ' ':
                continue
            elif c in signs:
                data.append(int(num))
                data.append(c)
                num = ''
            else:
                num += c
        data.append(int(num))
        return data
         
         

print(Solution().calculate("123+3455/445*12-545"))