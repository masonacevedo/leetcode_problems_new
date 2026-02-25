from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        pairs = [(bin(x)[2:], x) for x in arr]

        # sort pairs according to number of 1s in the string
        # and then use the integer in the pair as the
        # tiebreaker.
        sorted_pairs = sorted(pairs,
                            key=lambda p: (
                                p[0].count("1"),
                                p[1]
                                )
                            )

        return [p[1] for p in sorted_pairs]


mySol = Solution()

arr_1 = [0,1,2,3,4,5,6,7,8]
ans_1 = mySol.sortByBits(arr_1)
print("ans_1:", ans_1)

arr_2 = [1024,512,256,128,64,32,16,8,4,2,1]
ans_2 = mySol.sortByBits(arr_2)

print("ans_2:", ans_2)