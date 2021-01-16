"""
Description: Kth Largest Element in an Array
Version: 1
Author: Taki Guan
Date: 2021-01-16 20:58:42
LastEditors: Taki Guan
LastEditTime: 2021-01-16 21:01:18
"""
#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]


# @lc code=end
