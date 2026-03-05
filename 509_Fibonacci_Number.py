class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        DP = [0, 1]

        for i in range(2, n+1):
            DP.append(DP[i-1]+DP[i-2])
        return DP[-1]