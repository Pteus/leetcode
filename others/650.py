from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue

            can_place_left = (i == 0) or flowerbed[i - 1] == 0
            can_place_right = (i == len(flowerbed) - 1) or flowerbed[i + 1] == 0

            if can_place_left and can_place_right:
                count += 1
                flowerbed[i] = 1
                if count >= n:
                    return True

        return count >= n


sol = Solution()
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))
