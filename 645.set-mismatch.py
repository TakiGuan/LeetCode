"""
Description: Set Mismatch
Version: 1
Author: Taki Guan
Date: 2021-03-03 08:17:31
LastEditors: Taki Guan
LastEditTime: 2021-03-03 09:27:17
"""
#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [
            sum(nums) - sum(set(nums)),
            sum(range(1, len(nums) + 1)) - sum(set(nums)),
        ]


# @lc code=end
