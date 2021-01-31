"""
Description: Next Permutation
Version: 1
Author: Taki Guan
Date: 2021-01-31 19:49:04
LastEditors: Taki Guan
LastEditTime: 2021-01-31 19:49:24
"""
#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        # nums数组是从大到小排列的
        if i == 0:
            nums.reverse()
            return
        # 找到最后一个升序的位置
        k = i - 1
        # 将k位置的元素与k位置后最小的元素互换位置
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        # 将k位置后的数组逆序
        l, r = k + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


# @lc code=end
