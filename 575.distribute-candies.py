"""
Description: 
Version: 1
Author: Taki Guan
Date: 2021-03-02 08:14:44
LastEditors: Taki Guan
LastEditTime: 2021-03-02 13:08:23
"""
#
# @lc app=leetcode id=575 lang=python3
#
# [575] Distribute Candies
#

# @lc code=start
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))


# @lc code=end
