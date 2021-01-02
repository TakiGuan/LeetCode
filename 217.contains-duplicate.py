'''
Description: Duplicate Check Solution
Version: 1
Author: Taki Guan
Date: 2020-12-27 20:56:41
LastEditors: Taki Guan
LastEditTime: 2020-12-27 21:06:14
'''
#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

# @lc code=end
