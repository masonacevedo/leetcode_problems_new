from typing import List

class customNum:
    def __init__(self, x):
        self.x = x
    
    def __lt__(self, other):
        self_string = bin(self.x)[2:]
        other_string = bin(other.x)[2:]
        
        if self_string.count("1") < other_string.count("1"):
            return True
        elif self_string.count("1") > other_string.count("1"):
            return False
        else:
            return self.x < other.x

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda n: customNum(n))



mySol = Solution()

arr_1 = [0,1,2,3,4,5,6,7,8]
ans_1 = mySol.sortByBits(arr_1)
print("ans_1:", ans_1)

arr_2 = [1024,512,256,128,64,32,16,8,4,2,1]
ans_2 = mySol.sortByBits(arr_2)

print("ans_2:", ans_2)