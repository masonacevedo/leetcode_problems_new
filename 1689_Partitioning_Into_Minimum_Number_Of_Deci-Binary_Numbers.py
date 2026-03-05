class Solution:
    def minPartitions(self, n: str) -> int:
        maxInt = float('-inf')
        for char in n:
            maxInt = max(int(char), maxInt)
        return maxInt