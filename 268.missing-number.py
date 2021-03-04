"""
Description: Missing Number
Version: 1
Author: Taki Guan
Date: 2021-03-04 14:37:27
LastEditors: Taki Guan
LastEditTime: 2021-03-04 15:52:36
"""
#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _len = len(nums)
        return _len * (_len + 1) // 2 - sum(nums)


# @lc code=end
