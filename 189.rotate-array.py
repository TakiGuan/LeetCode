'''
Description: Rotate Array Solution
Version: 1
Author: Taki Guan
Date: 2020-12-26 17:36:01
LastEditors: Taki Guan
LastEditTime: 2020-12-29 14:33:30
'''
#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]

# @lc code=end
