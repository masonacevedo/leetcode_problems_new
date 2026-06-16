def p(n, DP, maxSize=None):
    if maxSize is None:
        maxSize = n

    if DP[n][maxSize] != -1:
        print("using memo!")
        return DP[n][maxSize]
    
    if n == 0 or n ==1:
        return 1
    if n < 0:
        return 0
    ans = 0
    for i in range(1, maxSize+1):
        ans = (ans + (p(n-i, DP, maxSize=i))) % 1_000_000
    
    DP[n][maxSize] = ans
    return ans


CEILING = 4_000
DP = [[None for _ in range(0, CEILING+1)] for _ in range(0, CEILING+1)]

for i in range(0, len(DP)):
    DP[0][i] = 1
    DP[i][0] = 0
    DP[i][1] = 1
    DP[1][i] = 1

DP[0][0] = 1
DP[2][2] = 2

# for row in DP:
#     print(row)
# print()

def nextCoord(coord):
    i,j = coord
    if i == CEILING and j == CEILING:
        return None
    elif j == CEILING:
        return (CEILING, i+1)

    elif i == 2:
        total = i+j
        return (i + j - 1, 2)
    

    return (i-1,j+1)

coords = (3,2)
i,j = coords
while coords is not None:
    i,j = coords
    if j > i:
        DP[i][j] = DP[i][i]
    else:
        DP[i][j] = sum([DP[i-x][x] for x in range(1,j+1)]) % 1_000_000
    
    # for row in DP:
    #     print(row)
    # print("coords:", coords)
    # print("next:  ", nextCoord(coords))
    # breakpoint()
    if (i == j):
        print(i, "done")
        if DP[i][i] == 0:

            print("found the number! enter to con")
            breakpoint()
    coords = nextCoord(coords)

print(DP[CEILING][CEILING])

# for i in range(0,CEILING):
#     a = p(i, DP)
#     print(i, ":", a)
#     if a == 0:
#         input("enter to continue!!")
