"""
Description: Shortest Unsorted Continuous Subarray
Version: 1
Author: Taki Guan
Date: 2021-02-25 21:11:18
LastEditors: Taki Guan
LastEditTime: 2021-02-25 21:11:45
"""
#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        res = [i for (i, (a, b)) in enumerate(zip(nums, sorted(nums))) if a != b]
        return 0 if not res else res[-1] - res[0] + 1


# @lc code=end
