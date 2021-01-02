'''
Description: Squares of a Sorted Array Solution
Version: 1
Author: Taki Guan
Date: 2020-12-26 16:41:58
LastEditors: Taki Guan
LastEditTime: 2020-12-29 14:53:58
'''
#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        l, r = 0, len(nums)-1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                result.append(left * left)
                l += 1
            else:
                result.append(right * right)
                r -= 1
        return result[::-1]

# @lc code=end
