def p(n, memo, maxSize=None):
    if maxSize is None:
        maxSize = n
    memoKey = (n, maxSize)
    if memoKey in memo:
        # print("using memo!")
        return memo[memoKey]
    
    if n == 0 or n ==1:
        return 1
    if n < 0:
        return 0
    ans = 0
    for i in range(1, maxSize+1):
        ans += p(n-i, memo, maxSize=i)
    
    memo[memoKey] = ans
    return ans

memo = {}
for i in range(0,10000):
    a = p(i, memo)
    print(i, ":", a)
    if a % 1_000_000 == 0:
        input("enter to continue!!")
