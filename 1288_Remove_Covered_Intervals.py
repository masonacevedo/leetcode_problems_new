from typing import List
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        covered_set = set([])
        for i in range(0, len(intervals)):
            for j in range(i+1, len(intervals)):
                if covered(intervals[i], intervals[j]):
                    covered_set.add(tuple(intervals[i]))
                elif covered(intervals[j], intervals[i]):
                    covered_set.add(tuple(intervals[j]))
        
        return len(intervals) - len(covered_set)

def covered(interval_1, interval_2):

    a,b = interval_1
    c,d = interval_2

    return ((c <= a) and (b <= d))



s = Solution()


intervals = [
    [10, 20],
    [15, 25],
    [16,17]
]

ans = s.removeCoveredIntervals(intervals)
print("ans:", ans)