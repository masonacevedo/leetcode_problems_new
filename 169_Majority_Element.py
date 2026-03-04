class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        return max(freqs.items(), key=lambda item: item[1])[0]