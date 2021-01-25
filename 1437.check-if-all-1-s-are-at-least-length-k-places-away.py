"""
Description: Check If All 1's Are at Least Length K Places Away
Version: 1
Author: Taki Guan
Date: 2021-01-25 19:53:27
LastEditors: Taki Guan
LastEditTime: 2021-01-25 19:54:00
"""
#
# @lc app=leetcode id=1437 lang=python3
#
# [1437] Check If All 1's Are at Least Length K Places Away
#

# @lc code=start
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        idx = -1
        l = len(nums)
        for i in range(l):
            if nums[i] == 1:
                if idx != -1 and (i - idx - 1) < k:
                    return False
                idx = i
        return True


# @lc code=end
