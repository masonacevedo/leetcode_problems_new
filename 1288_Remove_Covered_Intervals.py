from typing import List
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = len(intervals)
        for i in range(0, len(intervals)):
            for j in range(i+1, len(intervals)):
                print("intervals[i]:", intervals[i])
                print("intervals[j]:", intervals[j])
                breakpoint()
                if covered(intervals[i], intervals[j]):
                    ans -= 1
        
        return ans

def covered(interval_1, interval_2):

    a,b = interval_1
    c,d = interval_2

    return ((c <= a) and (b <= d)) or (a <= c) and (d <= b)



s = Solution()
intervals = [[1,4],[3,6],[2,8]]

ans = s.removeCoveredIntervals(intervals)
print("ans:", ans)