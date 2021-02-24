"""
Description: Search a 2D Matrix II
Version: 1
Author: Taki Guan
Date: 2021-02-23 22:01:43
LastEditors: Taki Guan
LastEditTime: 2021-02-24 08:47:30
"""
#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        for row in matrix:
            if row[0] <= target <= row[-1]:
                if target in row:
                    return True
        return False


# @lc code=end
