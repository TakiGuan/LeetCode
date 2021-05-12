"""
Description: Range Sum Query 2D - Immutable
Version: 1
Author: Taki Guan
Date: 2021-05-12 15:13:28
LastEditors: Taki Guan
LastEditTime: 2021-05-12 15:14:36
"""
#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sum = [[0] * (n + 1) for _ in range(m + 1)]
        # sum[i][j]是(i, j)到(0, 0)之间所有元素的和
        # i, j均从1开始计算
        # sum[i][j]等于相邻元素和的相加减去相交区域再加上matrix[i][j]本身
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                self.sum[r][c] = (
                    self.sum[r][c - 1]
                    + self.sum[r - 1][c]
                    - self.sum[r - 1][c - 1]
                    + matrix[r - 1][c - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return (
            self.sum[r2][c2]
            - self.sum[r2][c1 - 1]
            - self.sum[r1 - 1][c2]
            + self.sum[r1 - 1][c1 - 1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
