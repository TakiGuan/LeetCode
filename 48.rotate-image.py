'''
Description: Rotate Image Solution
Version: 1
Author: Taki Guan
Date: 2020-12-29 14:26:20
LastEditors: Taki Guan
LastEditTime: 2020-12-30 09:19:37
'''
#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
#
# 1 2 3    1 4 7    7 4 1
# 4 5 6 -> 2 5 8 -> 8 5 2
# 7 8 9    3 6 9    9 6 3
#
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Flip the matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse the matrix row
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

# @lc code=end
