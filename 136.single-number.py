'''
Description: Single Number Solution
Version: 1
Author: Taki Guan
Date: 2020-12-27 21:12:19
LastEditors: Taki Guan
LastEditTime: 2020-12-27 22:11:21
'''
#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ls = sum(nums)
        # ss = sum(set(nums))
        # return ls - 2*(ls - ss)
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]

# @lc code=end
