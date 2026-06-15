import copy

f_name = "keylog.txt"
with open(f_name, "r+") as f:
    lines = f.readlines()


clean_lines = [line.replace("\n", "") for line in lines]

DIGITS = [str(i) for i in range(0, 4)]
DIGITS += [str(i) for i in range(6,10)]
# print(DIGITS)
def generatePasswords(n):
    if n == 0:
        return [""]
    
    shorterPasswords = generatePasswords(n-1)
    ans = []
    for d in DIGITS:
        newPasswords = [d + p for p in shorterPasswords]
        ans += newPasswords
    return ans

def breaksRule(p, line):
    # a password can break the rule by either
    # not having a character it should, or by 
    # only having the given characters out of order.
    for char in line:
        if char not in p:
            return True
    
    for i in range(0, len(line)):
        for j in range(i+1, len(line)):
            char1 = line[i]
            char2 = line[j]
            # breakpoint()

            if p.index(char1) > p.index(char2):
                return True
    return False
    

# ans = breaksRule("43219", "319")
# print("ans:", ans)

def validPassword(p):
    for line in clean_lines:
        if breaksRule(p, line):
            return False
    return True

CEILING = 99999999
import time
lastTime = time.time()
for i in range(100, CEILING+1):
    if time.time() - lastTime > 5:
        lastTime = time.time()
        print('i:',i)
        print(f"{i/CEILING}")
    
    if validPassword(str(i)):
        print(i)
        input('enter to con')
    # else:
    #     print(i,"invalid")
