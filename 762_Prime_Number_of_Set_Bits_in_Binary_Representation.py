import math

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        left_string = bin(left)[2:]
        right_string = bin(right)[2:]

        ans = 0
        for num in range(left, right+1):
            num_as_bin_string = bin(num)[2:]
            set_bits = num_as_bin_string.count("1")
            if isPrime(set_bits):
                ans += 1
        return ans

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (float(n)/float(i)) == (n//i):
            return False
    return True

mySol = Solution()
ans = mySol.countPrimeSetBits(990, 1048)
