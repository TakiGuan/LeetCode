'''
Description: Intersection 2 Arrays Solution
Version: 1
Author: Taki Guan
Date: 2020-12-28 08:39:20
LastEditors: Taki Guan
LastEditTime: 2020-12-29 14:41:11
'''
#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [* (Counter(nums1) & Counter(nums2)).elements()]

# @lc code=end
