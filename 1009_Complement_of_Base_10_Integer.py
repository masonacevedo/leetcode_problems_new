class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binaryString = bin(n)[2:]
        complementString = calculateComplement(binaryString)
        return int(complementString, 2)

def calculateComplement(s):
    complementChars = []
    for char in s:
        if char == '0':
            complementChars.append('1')
        else:
            complementChars.append('0')
    return ''.join(complementChars)