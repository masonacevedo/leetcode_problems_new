class Solution:
    def maxFrequencyElements(self, nums) -> int:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        freqs = sorted(freq_dict.values())
        return max(freqs) * freqs.count(max(freqs))

mySol = Solution()

ans = mySol.maxFrequencyElements([1,2,2,3,1,4])
print(ans)