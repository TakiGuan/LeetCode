'''
Description: Valid Sudoku Solution
Version: 1
Author: Taki Guan
Date: 2020-12-29 08:50:31
LastEditors: Taki Guan
LastEditTime: 2020-12-29 14:32:24
'''
#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sodoku = []
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell != '.':
                    sodoku += (i, cell), (cell, j), (i//3, j//3, cell)
        # print(sodoku)
        return len(sodoku) == len(set(sodoku))

        # @lc code=end
