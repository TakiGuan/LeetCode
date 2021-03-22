"""
Description: Wiggle Subsequence
Version: 1
Author: Taki Guan
Date: 2021-03-18 16:30:19
LastEditors: Taki Guan
LastEditTime: 2021-03-18 23:06:51
"""
#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = 1
        increase = None  # 大或者小
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and increase != True:
                length += 1
                increase = True
            if nums[i] < nums[i - 1] and increase != False:
                length += 1
                increase = False
        return length


# @lc code=end
