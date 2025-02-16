from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False] * len(candies)
        max_value = max(candies)

        for i, c in enumerate(candies):
            res[i] = c + extraCandies >= max_value

        return res


sol = Solution()
print(sol.kidsWithCandies([2, 3, 5, 1, 3], 3))
