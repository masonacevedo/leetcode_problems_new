from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        inverted = [-1*num for num in nums]
        heapify(inverted)
        for _ in range(0, k):
            ans = heapq.heappop(inverted)
        return -1*ans