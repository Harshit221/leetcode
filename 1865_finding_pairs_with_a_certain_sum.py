from typing import List


class FindSumPairs:
    
    def __init__(self, num1: List[int], num2: List[int]):
        map1 = {}
        map2 = {}
        for n in num1:
            if n in map1:
                map1[n] += 1
            else:
                map1[n] = 1 
                
        for n in num2:
            if n in map2:
                map2[n]+=1
            else:
                map2[n] = 1
        self.map1 = map1
        self.map2 = map2
        self.num1 = num1
        self.num2 = num2

                        

    def add(self, index: int, val: int) -> None:
        if index >= len(self.num2):
            return
        self.map2[self.num2[index]]-=1
        self.num2[index] += val
        if self.num2[index] in self.map2:
            self.map2[self.num2[index]] += 1
        else:
            self.map2[self.num2[index]] = 1
        print()
        

    def count(self, tot: int) -> int:
        sol = 0
        for n1, c1 in self.map1.items():
            if tot - n1 in self.map2:
                sol += c1 * self.map2[tot-n1]
                
        return sol
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

commands = ["FindSumPairs","count","add","count","count","add","add","count"]
values = [[[1,1,2,2,2,3],[1,4,5,2,5,4]],[7],[3,2],[8],[4],[0,1],[1,1],[7]]

obj = FindSumPairs(values[0][0], values[0][1])

def call(name, args):
    if name == "count":
        return obj.count(args[0])
    else:
        return obj.add(args[0], args[1])
res = [call(commands[i], values[i]) for i in range(1, len(commands))]

print(res)
print([None,8,None,2,1,None,None,11])