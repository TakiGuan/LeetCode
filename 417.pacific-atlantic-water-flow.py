"""
Description: Pacific Atlantic Water Flow
Version: 1
Author: Taki Guan
Date: 2021-03-26 08:34:01
LastEditors: Taki Guan
LastEditTime: 2021-03-26 08:34:37
"""
#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        pacific_land = set()
        atlantic_land = set()
        row, column = len(matrix), len(matrix[0])

        def spread(i, j, land):
            land.add((i, j))
            for x, y in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                if (
                    0 <= x < row
                    and 0 <= y < column
                    and matrix[x][y] >= matrix[i][j]
                    and (x, y) not in land
                ):
                    spread(x, y, land)

        for i in range(row):
            spread(i, 0, pacific_land)
            spread(i, column - 1, atlantic_land)
        for j in range(column):
            spread(0, j, pacific_land)
            spread(row - 1, j, atlantic_land)

        return list(pacific_land & atlantic_land)


# @lc code=end
