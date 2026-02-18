class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary_string = bin(n)[2:]
        for char1, char2 in zip(binary_string[0:-1], binary_string[1:]):
            if char1 == char2:
                return False
        return True